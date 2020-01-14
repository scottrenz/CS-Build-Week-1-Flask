import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request, render_template
from pusher import Pusher
from decouple import config

from room import Room
from player import Player
from world import World

from item import Clothing, Riches

# Look up decouple for config variables
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

world = World()
clothing = ' pants skirt shoes shirt '
riches = ' pearl  sapphire photo painting silver gold diamond ruby  emerald '
app = Flask(__name__)


def get_player_by_header(world, auth_header):
    if auth_header is None:
        return None
    auth_key = auth_header.split(" ")
    if auth_key[0] != "Token" or len(auth_key) != 2:
        return None

    player = world.get_player_by_auth(auth_key[1])
    return player


@app.route('/api/registration/', methods=['POST'])
def register():
    values = request.get_json()
    required = ['username', 'password1', 'password2']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    username = values.get('username')
    password1 = values.get('password1')
    password2 = values.get('password2')

    response = world.add_player(username, password1, password2)
    if 'error' in response:
        return jsonify(response), 500
    else:
        return jsonify(response), 200

@app.route('/api/login/', methods=['POST'])
def login():
    # IMPLEMENT THIS
    values = request.get_json()
    required = ['username', 'password']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    username = values.get('username')
    password = values.get('password')
    print('you entered username',username)
    response = world.authenticate_user(username, password)
    if 'error' in response:
        return jsonify(response), 500
    else:
        return jsonify(response), 200


@app.route('/api/adv/init/', methods=['GET'])
def init():
    auth_head = request.headers.get("Authorization")
#    return auth_head
    player = get_player_by_header(world, auth_head)
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500

    response = {
        'title': player.current_room.name,
        'description': player.current_room.description,
        "player_items": "", "room_items": ""
        }
    response["player_items"] = player.items
    response["room_items"] = player.current_room.items
    return jsonify(response), 200


@app.route('/api/adv/move/', methods=['POST'])
def move():
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500

    values = request.get_json()
    required = ['direction']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    direction = values.get('direction')
    if player.travel(direction):
        response = {
            'title': player.current_room.name,
            'description': player.current_room.description,
            "player_items": "", "room_items": ""
        }
        player.items = player.items.replace('  ',' ')
        player.current_room.items = player.current_room.items.replace('  ',' ')
        response["player_items"] = player.items
        response["room_items"] = player.current_room.items
        if response['title'] == "Nasus' Statue":
            response['description'] = 'You dare to arrive not fully clothed?'            
        if response['title'] == "Nasus' Statue":
            if ' shirt ' in player.current_room.items and ' shoes ' in player.current_room.items:
                if ' skirt ' in player.current_room.items or ' pants ' in player.current_room.items:
                    response['description'] = 'Congratualations, you are well dressed and have arrived to the goal!'
                    return jsonify(response), 200
        return jsonify(response), 200
    else:
        response = {
            'error': "You cannot move in that direction.",
        }
        return jsonify(response), 500


@app.route('/api/adv/take/', methods=['POST'])
def take_item():
    # IMPLEMENT THIS
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500
    values = request.get_json()
    required = ['take']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    take = ' ' + values.get('take').strip() + ' '
    if player.current_room.items.strip():
        if take in riches and player.current_room.name != 'The Replicator Room"':
            if take in player.current_room.items:
                player.items = player.items + take
                player.current_room.items = player.current_room.items.replace(take, ' ')
                response = {"player_items": "", "room_items": ""}    
                response["player_items"] = player.items
                response["room_items"] = player.current_room.items
                return jsonify(response), 200

    response = {'error': "The item is not available"}
    return jsonify(response), 400

@app.route('/api/adv/drop/', methods=['POST'])
def drop_item():
    # IMPLEMENT THIS
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500
    values = request.get_json()
    required = ['drop']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    drop = ' ' + values.get('drop').strip() + ' '
    if player.items.strip():
        if drop in riches:
            if drop in player.items:
                player.current_room.items = player.current_room.items + drop
                player.items = player.items.replace(drop, ' ')
                response = {"player_items": "", "room_items": ""}    
                response["player_items"] = player.items
                response["room_items"] = player.current_room.items
                return jsonify(response), 200

    response = {'error': "The item is not available"}
    return jsonify(response), 400

@app.route('/api/adv/inventory/', methods=['GET'])
def inventory():
    # IMPLEMENT THIS
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500
    response = {"player_items": "", "room_items": ""}    
    if player.items.strip():
        response["player_items"] = player.items
    else:
        response["player_items"] = 'no items'
    if player.current_room.items.strip():
        response["room_items"] = player.current_room.items
    else:
        response["room_items"] = 'no items'

    return jsonify(response), 200

    response = {'error': "Not implement3"}
    return jsonify(response), 400

@app.route('/api/adv/buy/', methods=['POST'])
def buy_item():
    # IMPLEMENT THIS
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500
    values = request.get_json()
    required = ['buy', 'sell']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    buy = ' ' + values.get('buy').strip() + ' '
    sell = ' ' + values.get('sell').strip() + ' '
    if player.current_room.items.strip() and player.items.strip() and buy in clothing and buy in player.current_room.items:
        if sell in riches and sell in player.items:
            player.items = player.items.replace(sell, buy)
            player.current_room.items = player.current_room.items.replace(buy, sell)
            response = {"player_items": "", "room_items": ""}    
            response["player_items"] = player.items
            response["room_items"] = player.current_room.items
            return jsonify(response), 200

    response = {'error': "The item is not available"}
    return jsonify(response), 400

@app.route('/api/adv/sell/', methods=['POST'])
def sell_item():
    # IMPLEMENT THIS
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500
    values = request.get_json()
    required = ['buy', 'sell']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    buy = ' ' + values.get('buy').strip() + ' '
    sell = ' ' + values.get('sell').strip() + ' '
    if player.current_room.items.strip() and player.items.strip() and buy in clothing and buy in player.current_room.items:
        if sell in riches and sell in player.items:
            player.items = player.items.replace(sell, buy)
            player.current_room.items = player.current_room.items.replace(buy, sell)
            response = {"player_items": "", "room_items": ""}    
            response["player_items"] = player.items
            response["room_items"] = player.current_room.items
            return jsonify(response), 200

    response = {'error': "The item is not available"}
    return jsonify(response), 400

@app.route('/api/adv/rooms/', methods=['GET'])
def rooms():
    # IMPLEMENT THIS
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500
    x = []
    # print(world.rooms)
    n = 1
    for rm in world.rooms:
        y = world.rooms.get(rm).get_coords()
        z = "id="+str(n)+" x="+str(y[0])+" y="+str(y[1])
        n += 1
        x.append({rm: z})
    response = x
    return jsonify(response), 200

    response = {'error': "Not implement6"}
    return jsonify(response), 400


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
