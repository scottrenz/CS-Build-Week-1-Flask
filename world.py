from room import Room
from player import Player
import random
import math
import bcrypt

class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.players = {}
        self.create_world()
        self.password_salt = bcrypt.gensalt()

    def add_player(self, username, password1, password2):
        if password1 != password2:
            return {'error': "Passwords do not match"}
        elif len(username) <= 2:
            return {'error': "Username must be longer than 2 characters"}
        elif len(password1) <= 5:
            return {'error': "Password must be longer than 5 characters"}
        elif self.get_player_by_username(username) is not None:
            return {'error': "Username already exists"}
        password_hash = bcrypt.hashpw(password1.encode(), self.password_salt)
        player = Player(username, self.starting_room, password_hash)
        self.players[player.auth_key] = player
        return {'key': player.auth_key}

    def get_player_by_auth(self, auth_key):
        if auth_key in self.players:
            return self.players[auth_key]
        else:
            return None

    def get_player_by_username(self, username):
        for user in self.players:
            if self.players[user].username == username:
                return self.players[user]
        return None

    def authenticate_user(self, username, password):
        user = self.get_player_by_username(username)
        if user is None:
            return "error invalid username and/or password"
        password_hash = bcrypt.hashpw(password.encode() ,self.password_salt)
        if user.password_hash == password_hash:
            return {'key': user.auth_key}
        return "error invalid username and/or password"

    def create_world(self):
        # UPDATE THIS:
        # Should create 100 procuedurally generated rooms

        self.rooms = {
'outside': Room("Outside Cave Entrance",
                             "North of you, the cave mount beckons", 1, 1, 1),

'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east.""", 2, 1, 2),

'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""", 3, 1, 3),

'narrow': Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""", 4, 1, 4),

'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""", 5, 1, 5),

'star_gate': Room("Star Gate",
                             "You are about to go to another world in the galaxy.", 6, 1, 6),

'pegasus_b': Room("Pegasus B", """You are now in another galaxy outside the Milky Way.""", 7, 1, 7),

'atlantis': Room("Atlantis", """You are back to the antediluvian world.""", 8, 1, 8),

'puddle_jumper': Room("Puddle Jumper", """Get ready to fly through the gate.""", 9, 1, 9),

'borg': Room("The Borg", """Prepare to be assimilated! Resistance is futile!""", 10, 1, 10),

'enterprise': Room("The Enterprise", """Space: the final frontier. Boldy go!""", 11, 2, 1),

'vulcan': Room("Planet Vulcan", """Live long and prosper.
 Just don't get emotional about it.""", 12, 2, 2),

'replicator': Room("The Replicator Room", """Order what you like.
 Picard recommneds: Tea, Earl Grey, hot!""", 13, 2, 3),

'alpha_quadrant': Room("Alpha quadrant", """Ready to see the neighborhood?
 Make it so!""", 14, 2, 4),

'transporter': Room("The Transporter Room", """If things get freaky down there,
 just call out: Beam me up, Scotty! When you are ready to go down just call out 'Engage!'""", 15, 2, 5),

'stranded': Room("Stranded on Unknown Planet", """Did I tell you the one about Darmok
 and Jalad at Tanagra?""", 16, 2, 6),

'holodeck': Room("The Holodeck", """Think of your wildest fantasy,
 and ypu're there. Try not to run into the walls. It can be a rude awakening.""", 17, 2, 7),

'tribble': Room("The Tribble Room", """The Trouble with Tribbles?
 Those cute little furry things? Why, they're no tribble a'tal.""", 18, 2, 8),

'romulan': Room("Romulan Warbird", """Get ready for battle!
 Death to the Cardassians!""", 19, 2, 9),

'shore_leave': Room("Shore Leave", """If you see Alice chasing a White Rabbit,
 tell her he went for a cup of tea.""", 20, 2, 10),

'earth': Room("Planet Earth", """Earth inhabitants: Ugly bags of mostly water.""", 21, 3, 1),

'klingon': Room("Klingon Home Planet", """Get ready for some Gok.
 Best when the worms are alive and wriggling. Wash it down with a warm glass of Blood Wine.""", 22, 3, 2),

'jefferies_tube': Room("Jefferies Tube", """Just keep your head down and crawl low.
 Don't touch that pipe. It might be scaldingly hot.
  And if you touch the high power line, don't worry--no pain with instant death.""", 23, 3, 3),

'delta_quadrant': Room("Delta Quadrant", """Thought you were going on a short test run?
 No problem. Just forty years back to the Alpha Quadrant. Talk about a long distance Voyager.""", 24, 3, 4),

'pon_farr': Room("Pon Farr", """Thought you could just forget about it
 and it would go away? No way. Time to pair up my mate. May as well have some wild fun.""", 25, 3, 5),

'neutral_zone': Room("The Neutral Zone", """Get out as quickly as you can.
 Breaking the treaty of the Neutral Zone is highly offensive.
  Watch out for that Romulan War bird. It's gunning for ya""", 26, 3, 6),

'bajoran_wormhole': Room("Bajoran Wormhole", """Thought the war on Bajora
 with the Cardassians was bad? Well, enjoy getting sucked into this Bajoran Wormhole.
  Maybe you will luck out and get to the other side and only have to face the Dominion.""", 27, 3, 7),

'baryon_sweep': Room("Baryon Sweep", """Such unfortunate timing my friend.
 You have managed to beam aboard a vessal undergoing a Baryon Sweep.
  Yes, any organic living matter will be neutralized when the Baryon Sweep gets to its position
   onboard the craft. Sure hope you are not organic.""", 28, 3, 8),

'cardassia_prime': Room("Cardassia Prime", """Lucky you.
 Very Festive times now on Cardassia Prime. Everyone is celebrating making war on Bajor.
  You are Bjoran you say? Uh oh!""", 29, 3, 9),
  
'adamantium': Room("Adamantium Room",
                    """There seem to be claw like slashes all 
                    over the room!""", 30, 3, 10),

'web': Room("Web Room",
             """There are sticky webs all over this room.""", 31, 4, 1),

'stark': Room("Stark's Room",
               """There are vast amounts of electronics all over
                this room.""", 32, 4, 2),

'pitch_black': Room("Pitch Black",
                     """Silence and darkness. You can't see
                      anything in this room.""", 33, 4, 3),

'science': Room("Science Room",
                 """It looks as though a monster
                  tore out of this room.""", 34, 4, 4),

'skull': Room("The Skull Room",
               """Guns and amo everywhere. There is a picture
                of a death's head skull on the wall.""", 35, 4, 5),

'cerebro': Room("Cerebro",
                 """There is a weird helmet in the middle of 
                 this round room. Its like we are in a ball.""", 36, 4, 6),

'rock': Room("The Rock",
              """Everywhere you look things are made of rock.""", 37, 4, 7),

'bullseye': Room("The Bullseye Room",
                  """Hanging all around the room are targets 
                  that have been hit dead in the bullseye.""", 38, 4, 8),

'tourch': Room("Tourch", """Everything is on fire.""", 39, 4, 9),

'ice': Room("Ice", """Its so cold.""", 40, 4, 10),

'small': Room("Small Room",
               """Everything in here is so tiny. 
               Like it was made for ants.""", 41, 5, 1),

'aquarium': Room("Aquarium",
                  """All of the walls are fish tanks. There 
                  seems to be an entrance through the floor to the tank.""", 42, 5, 2),

'lightning': Room("Lightning",
                   """This room seems to be charged with 
                   electricty. Don't touch the walls.""", 43, 5, 3),

'dead_pool': Room("Deadpool's Room",
                   """There are little deadpool figurines 
                   everywhere. They all look to be dying though.""", 44, 5, 4),

'hawk': Room("Hawk Room",
              """There is a perch in the corner of the room.""", 45, 5, 5),

'america': Room("American Room",
                 """Captain America stuff is everywhere.""", 46, 5, 6),

'smash': Room("Smash Room",
               """You can see several Hulk shirts ripped apart. 
               All the little Hulk figurines have been smashed into little 
               bitty peaces. """, 47, 5, 7),
'suarward_dining': Room("Suarward Dining", "Large, square dining room has mismatched wooden furniture.  The seating is cushioned.  The floor is stone. Overall has a quaint atmosphere.", 48, 5, 8),

'talltail_chambers': Room("TallTail Chambers", "Small, rectangular bedroom with wooden funiture. Among the first things one notices walking in is muddy footprints on the floor.", 49, 5, 9),

'starStrike_sanctuary': Room('Starstrike Sanctuary', " This cramped, rectangular office has mismatched wooden, metal, and glass furniture, Upon entering one notices light from the heavens", 50, 5, 10),

'grandwing_saloon': Room("Grandwing Saloon", "Cramped, square, dim lit saloon. Broken glass covers the floor. There is a thick haze of smoke upon entering. Among the first things one notices walking in are a conspicuous stain on the floor", 51, 6, 1),

'outcast_den': Room("Outcast Den", "Large, L-shaped bathroom screams death. Leave Quickly!", 52, 6, 2),

'starfall_hideout': Room("Starfall Hideout", "Light is provided by wall lamps and a ceiling light. Among the first things one notices walking in are glitter footprints on the floor and a collection of action figures.", 53, 6, 3),

'lightstorm_harbor': Room("Lightstorm Harbor", "Among the first things one notices walking in is photographs on the wall. Long ago this was a sailors palace ", 54, 6, 4),

'feather_nest': Room("Feather Nest", "A large, square bedroom. The floor is layered with shedded feathers. The first thing one notices upon entering is a broken clock on the wall", 55, 6, 5),

'coldwar_hideaway': Room("Coldwar Hideaway", "The room is done in colors that remind you of Halloween and overall has a rustic look to it.  Among the first things one notices walking in are a crumpled paper", 56, 6, 6),

'shadow_burrow': Room("Shadow Burrow", "Cold, and cluttered with spell books. Upon entering one feels a draft come from the window that chills the soul", 57, 6, 7),

'miracle_dungeon': Room("Miracle Dungeon", "This large kitchen is magical. Powered by one's own imagination", 58, 6, 8),

'skullblade_cave': Room("skullblade_cave", "An average-sized cave, dark and mysterious. Sounds of flowing water come from deep within. Among entering bats fly out from everywhere.", 59, 6, 9),

'thorn_nest': Room("Thorn Nest", "Cramped office with matching wooden furniture. The room is done is such way it reminds one of a thorny nest", 60, 6, 10),

'archkeep_sanctuary': Room("Archkeep Sanctuary", "This spacious, bathroom is done in bold colors and overall has a quaint atmosphere.  Among the first things one notices walking in are a collection of knickknacks and many cosmetics strewn on the counter.", 61, 7, 1),

'skyspell_haven': Room("Skyspell Haven", "Vintage theme in murky colors and overall has a retro look to it.  Among the first things one notices walking in is a barn star on the wall.", 62, 7, 2),

'flower_retreat': Room("Flower Retreat", "A mystical garden, that is home to many fairies, but beware the dragons below", 63, 7, 3),

'blitz_cover': Room("Blitz Cover", "Underground, yet well lit. Blitz Cover is a reminder of safety in these parts", 64, 7, 4),

'mystery_lair': Room("Mystery Lair", "The room of deja vu, beware!", 65, 7, 5),

'gardner': Room("Gardners Garden", """This garden has grown the most lavish
 fruits and vegetables on the planet, look around you for
 fruits and vegetables.""", 66, 7, 6),

'tomb': Room("The Kings Tomb", """You've found the long-lost Kings Tomb! 
Press C to loot the tomb.""", 67, 7, 7),

'princess_peach_castle': Room("Princess Peach castle", """You've arrived to Princess Peach Castle!
 See if she has anything for you.""", 68, 7, 8),

'bowsers_dungeon': Room("Bowsers Dungeon", """You're in Bowsers Dungeon,
 get what you can and get out of there!""", 69, 7, 9),

'toad_town': Room("Toad Town", """Toad town is iconic, for housing some of the worlds biggest superstars.
Look around and you might see Mario!""", 70, 7, 10),

'bonies_cabin': Room("Bonies Cabin", """Bonie welcomed you inside, for food.""", 71, 8, 1),

'goodnights_theatre': Room("Goodnights Theatre", """Shhhh!
 The show is about to start.""", 72, 8, 2),

'yoshis_yoga_palace': Room("Yoshis Yoga Palace", """Sit down, close your
 eyes and find your inter zen.""", 73, 8, 3),

'sarasaland': Room("Sarasaland", """Queen Daisy has been awaiting you're arrival,
 check what you can do for her.""", 74, 8, 4),

'bowsers_kingdom': Room("Bowsers Kingdom", """Watch youself, you might be standing on lava!""", 75, 8, 5),

'warios_woods': Room("Warios Woods", """Warios Woods has plenty of organic resources, pack up what you can and head to the market!""", 76, 8, 6),

'rosalinas_land': Room("Rosalinas Land", """You've found the long-lost land of Princess Rosalina! 
The Lumas have left everything! Where could they be?""", 77, 8, 7),

'koopalings_shack': Room("Kooplings Shack", """find a bed and get some rest.""", 78, 8, 8),

'lumas_village': Room("Lumas Village", """Lumas village is known for its amazing sky at night, and great tradesmen.
 See if anyone wants to trade anything.""", 79, 8, 9),

'toads_boat': Room("Toads Boat", """Toad said he'd take you to a special Island.
 Do you want to go?""", 80, 8, 10),

'toads_island': Room("Toads Island", """See what the people here have to offer.""", 81, 9, 1),

'marios_palace': Room("Marios Palace", """You've been selected to explore Marios palace.""", 82, 9, 2),

'floating_pyramids': Room("Floating Pyramids", "Pyramids sitting high above the desert in Shurima", 83, 9, 3),

'targon': Room("Mt. Targon", "The desolate mountain with the highest peak, Targon", 84, 9, 4),

'moutain_pass': Room("Mountain Pass", "Mountain pass used to cross the boarder, blocked with a key locked gate", 85, 9, 5),

'nefaras_necrocalis': Room("Nefara's Necrocalis", "Hut laid out near the cemetary, used for Necromancy training", 86, 9, 6),

'fyron_flat': Room("Fyron's Salt Flat", "House belonging to Fyron the Mage, imbued with magic and made of salt", 87, 9, 7),

'shurima_lake': Room("Lake Shurima", "Lake surround most of Shurima, the waters shift from shallow to deep very quickly", 88, 9, 8),

'velocatronic': Room("Velocatronic Rail Station", "Run down station that used to house the greatest train known to Shurima", 89, 9, 9),

'voodou': Room("Voodou Lands", "Land owned by the Farmers of Shurima, plenty of desert fruit around to eat", 90, 9, 10),

'zayite_complex': Room("Zayite Complex", "School specializing in life studies, and basic magics", 91, 10, 1),

'shurima': Room("Shurima", "The Heavenly Kingdom of Shurima", 92, 10, 2),

'azirs_palace': Room("Azir's Palace", "Grand Palace belonging to a descendant of Shurima", 93, 10, 3),

'royal_palace': Room("Royal Palace", "Palace used by the King of Shurima", 94, 10, 4),

'water_gate': Room("Water Gate", "Gate nested near the edge of the lake, to prevent flooding and the releasing of monstrous sea creatures", 95, 10, 5),

'tempest_forest': Room("Tempest Forest", "Forest of cacti and high winds", 96, 10, 6),

'centralis': Room("Centralis", "Shurima's neighboring Kingdom, home to the mighty ", 97, 10, 7),

'holy_temple': Room("Holy Temple", "A place to worship Shurima", 98, 10, 8),

'pykes_grave': Room("Pyke's Grave", "The burial spot of the Pirate drowned in sand", 99, 10, 9),

'nasus_statue': Room("Nasus' Statue", "Statue of the first descendant of Nasus", 100, 10, 10)

        }

        # Link rooms together
        self.rooms['zayite_complex'].connect_rooms('n', self.rooms['shurima'])
        self.rooms['zayite_complex'].connect_rooms('w', self.rooms['toads_island'])
        self.rooms['toads_island'].connect_rooms('n', self.rooms['marios_palace'])
        self.rooms['toads_island'].connect_rooms('e', self.rooms['zayite_complex'])
        self.rooms['toads_island'].connect_rooms('w', self.rooms['bonies_cabin'])
        self.rooms['bonies_cabin'].connect_rooms('n', self.rooms['goodnights_theatre'])
        self.rooms['bonies_cabin'].connect_rooms('e', self.rooms['toads_island'])
        self.rooms['bonies_cabin'].connect_rooms('w', self.rooms['archkeep_sanctuary'])
        self.rooms['archkeep_sanctuary'].connect_rooms('n', self.rooms['skyspell_haven'])
        self.rooms['archkeep_sanctuary'].connect_rooms('e', self.rooms['bonies_cabin'])
        self.rooms['archkeep_sanctuary'].connect_rooms('w', self.rooms['grandwing_saloon'])
        self.rooms['grandwing_saloon'].connect_rooms('n', self.rooms['outcast_den'])
        self.rooms['grandwing_saloon'].connect_rooms('e', self.rooms['archkeep_sanctuary'])
        self.rooms['grandwing_saloon'].connect_rooms('w', self.rooms['small'])
        self.rooms['small'].connect_rooms('n', self.rooms['aquarium'])
        self.rooms['small'].connect_rooms('e', self.rooms['grandwing_saloon'])
        self.rooms['small'].connect_rooms('w', self.rooms['web'])
        self.rooms['web'].connect_rooms('n', self.rooms['stark'])
        self.rooms['web'].connect_rooms('e', self.rooms['small'])
        self.rooms['web'].connect_rooms('w', self.rooms['earth'])
        self.rooms['earth'].connect_rooms('n', self.rooms['klingon'])
        self.rooms['earth'].connect_rooms('e', self.rooms['web'])
        self.rooms['earth'].connect_rooms('w', self.rooms['enterprise'])
        self.rooms['enterprise'].connect_rooms('n', self.rooms['vulcan'])
        self.rooms['enterprise'].connect_rooms('e', self.rooms['earth'])
        self.rooms['enterprise'].connect_rooms('w', self.rooms['outside'])
        self.rooms['outside'].connect_rooms('n', self.rooms['foyer'])
        self.rooms['outside'].connect_rooms('e', self.rooms['enterprise'])
        self.rooms['shurima'].connect_rooms('s', self.rooms['zayite_complex'])
        self.rooms['shurima'].connect_rooms('n', self.rooms['azirs_palace'])
        self.rooms['shurima'].connect_rooms('w', self.rooms['marios_palace'])
        self.rooms['marios_palace'].connect_rooms('s', self.rooms['toads_island'])
        self.rooms['marios_palace'].connect_rooms('n', self.rooms['floating_pyramids'])
        self.rooms['marios_palace'].connect_rooms('e', self.rooms['shurima'])
        self.rooms['marios_palace'].connect_rooms('w', self.rooms['goodnights_theatre'])
        self.rooms['goodnights_theatre'].connect_rooms('s', self.rooms['bonies_cabin'])
        self.rooms['goodnights_theatre'].connect_rooms('n', self.rooms['yoshis_yoga_palace'])
        self.rooms['goodnights_theatre'].connect_rooms('e', self.rooms['marios_palace'])
        self.rooms['goodnights_theatre'].connect_rooms('w', self.rooms['skyspell_haven'])
        self.rooms['skyspell_haven'].connect_rooms('s', self.rooms['archkeep_sanctuary'])
        self.rooms['skyspell_haven'].connect_rooms('n', self.rooms['flower_retreat'])
        self.rooms['skyspell_haven'].connect_rooms('e', self.rooms['goodnights_theatre'])
        self.rooms['skyspell_haven'].connect_rooms('w', self.rooms['outcast_den'])
        self.rooms['outcast_den'].connect_rooms('s', self.rooms['grandwing_saloon'])
        self.rooms['outcast_den'].connect_rooms('n', self.rooms['starfall_hideout'])
        self.rooms['outcast_den'].connect_rooms('e', self.rooms['skyspell_haven'])
        self.rooms['outcast_den'].connect_rooms('w', self.rooms['aquarium'])
        self.rooms['aquarium'].connect_rooms('s', self.rooms['small'])
        self.rooms['aquarium'].connect_rooms('n', self.rooms['lightning'])
        self.rooms['aquarium'].connect_rooms('e', self.rooms['outcast_den'])
        self.rooms['aquarium'].connect_rooms('w', self.rooms['stark'])
        self.rooms['stark'].connect_rooms('s', self.rooms['web'])
        self.rooms['stark'].connect_rooms('n', self.rooms['pitch_black'])
        self.rooms['stark'].connect_rooms('e', self.rooms['aquarium'])
        self.rooms['stark'].connect_rooms('w', self.rooms['klingon'])
        self.rooms['klingon'].connect_rooms('s', self.rooms['earth'])
        self.rooms['klingon'].connect_rooms('n', self.rooms['jefferies_tube'])
        self.rooms['klingon'].connect_rooms('e', self.rooms['stark'])
        self.rooms['klingon'].connect_rooms('w', self.rooms['vulcan'])
        self.rooms['vulcan'].connect_rooms('s', self.rooms['enterprise'])
        self.rooms['vulcan'].connect_rooms('n', self.rooms['replicator'])
        self.rooms['vulcan'].connect_rooms('e', self.rooms['klingon'])
        self.rooms['vulcan'].connect_rooms('w', self.rooms['foyer'])
        self.rooms['foyer'].connect_rooms('s', self.rooms['outside'])
        self.rooms['foyer'].connect_rooms('n', self.rooms['overlook'])
        self.rooms['foyer'].connect_rooms('e', self.rooms['vulcan'])
        self.rooms['azirs_palace'].connect_rooms('s', self.rooms['shurima'])
        self.rooms['azirs_palace'].connect_rooms('n', self.rooms['royal_palace'])
        self.rooms['azirs_palace'].connect_rooms('w', self.rooms['floating_pyramids'])
        self.rooms['floating_pyramids'].connect_rooms('s', self.rooms['marios_palace'])
        self.rooms['floating_pyramids'].connect_rooms('n', self.rooms['targon'])
        self.rooms['floating_pyramids'].connect_rooms('e', self.rooms['azirs_palace'])
        self.rooms['floating_pyramids'].connect_rooms('w', self.rooms['yoshis_yoga_palace'])
        self.rooms['yoshis_yoga_palace'].connect_rooms('s', self.rooms['goodnights_theatre'])
        self.rooms['yoshis_yoga_palace'].connect_rooms('n', self.rooms['sarasaland'])
        self.rooms['yoshis_yoga_palace'].connect_rooms('e', self.rooms['floating_pyramids'])
        self.rooms['yoshis_yoga_palace'].connect_rooms('w', self.rooms['flower_retreat'])
        self.rooms['flower_retreat'].connect_rooms('s', self.rooms['skyspell_haven'])
        self.rooms['flower_retreat'].connect_rooms('n', self.rooms['blitz_cover'])
        self.rooms['flower_retreat'].connect_rooms('e', self.rooms['yoshis_yoga_palace'])
        self.rooms['flower_retreat'].connect_rooms('w', self.rooms['starfall_hideout'])
        self.rooms['starfall_hideout'].connect_rooms('s', self.rooms['outcast_den'])
        self.rooms['starfall_hideout'].connect_rooms('n', self.rooms['lightstorm_harbor'])
        self.rooms['starfall_hideout'].connect_rooms('e', self.rooms['flower_retreat'])
        self.rooms['starfall_hideout'].connect_rooms('w', self.rooms['lightning'])
        self.rooms['lightning'].connect_rooms('s', self.rooms['aquarium'])
        self.rooms['lightning'].connect_rooms('n', self.rooms['dead_pool'])
        self.rooms['lightning'].connect_rooms('e', self.rooms['starfall_hideout'])
        self.rooms['lightning'].connect_rooms('w', self.rooms['pitch_black'])
        self.rooms['pitch_black'].connect_rooms('s', self.rooms['stark'])
        self.rooms['pitch_black'].connect_rooms('n', self.rooms['science'])
        self.rooms['pitch_black'].connect_rooms('e', self.rooms['lightning'])
        self.rooms['pitch_black'].connect_rooms('w', self.rooms['jefferies_tube'])
        self.rooms['jefferies_tube'].connect_rooms('s', self.rooms['klingon'])
        self.rooms['jefferies_tube'].connect_rooms('n', self.rooms['delta_quadrant'])
        self.rooms['jefferies_tube'].connect_rooms('e', self.rooms['pitch_black'])
        self.rooms['jefferies_tube'].connect_rooms('w', self.rooms['replicator'])
        self.rooms['replicator'].connect_rooms('s', self.rooms['vulcan'])
        self.rooms['replicator'].connect_rooms('n', self.rooms['alpha_quadrant'])
        self.rooms['replicator'].connect_rooms('e', self.rooms['jefferies_tube'])
        self.rooms['replicator'].connect_rooms('w', self.rooms['overlook'])
        self.rooms['overlook'].connect_rooms('s', self.rooms['foyer'])
        self.rooms['overlook'].connect_rooms('n', self.rooms['narrow'])
        self.rooms['overlook'].connect_rooms('e', self.rooms['replicator'])
        self.rooms['royal_palace'].connect_rooms('s', self.rooms['azirs_palace'])
        self.rooms['royal_palace'].connect_rooms('n', self.rooms['water_gate'])
        self.rooms['royal_palace'].connect_rooms('w', self.rooms['targon'])
        self.rooms['targon'].connect_rooms('s', self.rooms['floating_pyramids'])
        self.rooms['targon'].connect_rooms('n', self.rooms['moutain_pass'])
        self.rooms['targon'].connect_rooms('e', self.rooms['royal_palace'])
        self.rooms['targon'].connect_rooms('w', self.rooms['sarasaland'])
        self.rooms['sarasaland'].connect_rooms('s', self.rooms['yoshis_yoga_palace'])
        self.rooms['sarasaland'].connect_rooms('n', self.rooms['bowsers_kingdom'])
        self.rooms['sarasaland'].connect_rooms('e', self.rooms['targon'])
        self.rooms['sarasaland'].connect_rooms('w', self.rooms['blitz_cover'])
        self.rooms['blitz_cover'].connect_rooms('s', self.rooms['flower_retreat'])
        self.rooms['blitz_cover'].connect_rooms('n', self.rooms['mystery_lair'])
        self.rooms['blitz_cover'].connect_rooms('e', self.rooms['sarasaland'])
        self.rooms['blitz_cover'].connect_rooms('w', self.rooms['lightstorm_harbor'])
        self.rooms['lightstorm_harbor'].connect_rooms('s', self.rooms['starfall_hideout'])
        self.rooms['lightstorm_harbor'].connect_rooms('n', self.rooms['feather_nest'])
        self.rooms['lightstorm_harbor'].connect_rooms('e', self.rooms['blitz_cover'])
        self.rooms['lightstorm_harbor'].connect_rooms('w', self.rooms['dead_pool'])
        self.rooms['dead_pool'].connect_rooms('s', self.rooms['lightning'])
        self.rooms['dead_pool'].connect_rooms('n', self.rooms['hawk'])
        self.rooms['dead_pool'].connect_rooms('e', self.rooms['lightstorm_harbor'])
        self.rooms['dead_pool'].connect_rooms('w', self.rooms['science'])
        self.rooms['science'].connect_rooms('s', self.rooms['pitch_black'])
        self.rooms['science'].connect_rooms('n', self.rooms['skull'])
        self.rooms['science'].connect_rooms('e', self.rooms['dead_pool'])
        self.rooms['science'].connect_rooms('w', self.rooms['delta_quadrant'])
        self.rooms['delta_quadrant'].connect_rooms('s', self.rooms['jefferies_tube'])
        self.rooms['delta_quadrant'].connect_rooms('n', self.rooms['pon_farr'])
        self.rooms['delta_quadrant'].connect_rooms('e', self.rooms['science'])
        self.rooms['delta_quadrant'].connect_rooms('w', self.rooms['alpha_quadrant'])
        self.rooms['alpha_quadrant'].connect_rooms('s', self.rooms['replicator'])
        self.rooms['alpha_quadrant'].connect_rooms('n', self.rooms['transporter'])
        self.rooms['alpha_quadrant'].connect_rooms('e', self.rooms['delta_quadrant'])
        self.rooms['alpha_quadrant'].connect_rooms('w', self.rooms['narrow'])
        self.rooms['narrow'].connect_rooms('s', self.rooms['overlook'])
        self.rooms['narrow'].connect_rooms('n', self.rooms['treasure'])
        self.rooms['narrow'].connect_rooms('e', self.rooms['alpha_quadrant'])
        self.rooms['water_gate'].connect_rooms('s', self.rooms['royal_palace'])
        self.rooms['water_gate'].connect_rooms('n', self.rooms['tempest_forest'])
        self.rooms['water_gate'].connect_rooms('w', self.rooms['moutain_pass'])
        self.rooms['moutain_pass'].connect_rooms('s', self.rooms['targon'])
        self.rooms['moutain_pass'].connect_rooms('n', self.rooms['nefaras_necrocalis'])
        self.rooms['moutain_pass'].connect_rooms('e', self.rooms['water_gate'])
        self.rooms['moutain_pass'].connect_rooms('w', self.rooms['bowsers_kingdom'])
        self.rooms['bowsers_kingdom'].connect_rooms('s', self.rooms['sarasaland'])
        self.rooms['bowsers_kingdom'].connect_rooms('n', self.rooms['warios_woods'])
        self.rooms['bowsers_kingdom'].connect_rooms('e', self.rooms['moutain_pass'])
        self.rooms['bowsers_kingdom'].connect_rooms('w', self.rooms['mystery_lair'])
        self.rooms['mystery_lair'].connect_rooms('s', self.rooms['blitz_cover'])
        self.rooms['mystery_lair'].connect_rooms('n', self.rooms['gardner'])
        self.rooms['mystery_lair'].connect_rooms('e', self.rooms['bowsers_kingdom'])
        self.rooms['mystery_lair'].connect_rooms('w', self.rooms['feather_nest'])
        self.rooms['feather_nest'].connect_rooms('s', self.rooms['lightstorm_harbor'])
        self.rooms['feather_nest'].connect_rooms('n', self.rooms['coldwar_hideaway'])
        self.rooms['feather_nest'].connect_rooms('e', self.rooms['mystery_lair'])
        self.rooms['feather_nest'].connect_rooms('w', self.rooms['hawk'])
        self.rooms['hawk'].connect_rooms('s', self.rooms['dead_pool'])
        self.rooms['hawk'].connect_rooms('n', self.rooms['america'])
        self.rooms['hawk'].connect_rooms('e', self.rooms['feather_nest'])
        self.rooms['hawk'].connect_rooms('w', self.rooms['skull'])
        self.rooms['skull'].connect_rooms('s', self.rooms['science'])
        self.rooms['skull'].connect_rooms('n', self.rooms['cerebro'])
        self.rooms['skull'].connect_rooms('e', self.rooms['hawk'])
        self.rooms['skull'].connect_rooms('w', self.rooms['pon_farr'])
        self.rooms['pon_farr'].connect_rooms('s', self.rooms['delta_quadrant'])
        self.rooms['pon_farr'].connect_rooms('n', self.rooms['neutral_zone'])
        self.rooms['pon_farr'].connect_rooms('e', self.rooms['skull'])
        self.rooms['pon_farr'].connect_rooms('w', self.rooms['transporter'])
        self.rooms['transporter'].connect_rooms('s', self.rooms['alpha_quadrant'])
        self.rooms['transporter'].connect_rooms('n', self.rooms['stranded'])
        self.rooms['transporter'].connect_rooms('e', self.rooms['pon_farr'])
        self.rooms['transporter'].connect_rooms('w', self.rooms['treasure'])
        self.rooms['treasure'].connect_rooms('s', self.rooms['narrow'])
        self.rooms['treasure'].connect_rooms('n', self.rooms['star_gate'])
        self.rooms['treasure'].connect_rooms('e', self.rooms['transporter'])
        self.rooms['tempest_forest'].connect_rooms('s', self.rooms['water_gate'])
        self.rooms['tempest_forest'].connect_rooms('n', self.rooms['centralis'])
        self.rooms['tempest_forest'].connect_rooms('w', self.rooms['nefaras_necrocalis'])
        self.rooms['nefaras_necrocalis'].connect_rooms('s', self.rooms['moutain_pass'])
        self.rooms['nefaras_necrocalis'].connect_rooms('n', self.rooms['fyron_flat'])
        self.rooms['nefaras_necrocalis'].connect_rooms('e', self.rooms['tempest_forest'])
        self.rooms['nefaras_necrocalis'].connect_rooms('w', self.rooms['warios_woods'])
        self.rooms['warios_woods'].connect_rooms('s', self.rooms['bowsers_kingdom'])
        self.rooms['warios_woods'].connect_rooms('n', self.rooms['rosalinas_land'])
        self.rooms['warios_woods'].connect_rooms('e', self.rooms['nefaras_necrocalis'])
        self.rooms['warios_woods'].connect_rooms('w', self.rooms['gardner'])
        self.rooms['gardner'].connect_rooms('s', self.rooms['mystery_lair'])
        self.rooms['gardner'].connect_rooms('n', self.rooms['tomb'])
        self.rooms['gardner'].connect_rooms('e', self.rooms['warios_woods'])
        self.rooms['gardner'].connect_rooms('w', self.rooms['coldwar_hideaway'])
        self.rooms['coldwar_hideaway'].connect_rooms('s', self.rooms['feather_nest'])
        self.rooms['coldwar_hideaway'].connect_rooms('n', self.rooms['shadow_burrow'])
        self.rooms['coldwar_hideaway'].connect_rooms('e', self.rooms['gardner'])
        self.rooms['coldwar_hideaway'].connect_rooms('w', self.rooms['america'])
        self.rooms['america'].connect_rooms('s', self.rooms['hawk'])
        self.rooms['america'].connect_rooms('n', self.rooms['smash'])
        self.rooms['america'].connect_rooms('e', self.rooms['coldwar_hideaway'])
        self.rooms['america'].connect_rooms('w', self.rooms['cerebro'])
        self.rooms['cerebro'].connect_rooms('s', self.rooms['skull'])
        self.rooms['cerebro'].connect_rooms('n', self.rooms['rock'])
        self.rooms['cerebro'].connect_rooms('e', self.rooms['america'])
        self.rooms['cerebro'].connect_rooms('w', self.rooms['neutral_zone'])
        self.rooms['neutral_zone'].connect_rooms('s', self.rooms['pon_farr'])
        self.rooms['neutral_zone'].connect_rooms('n', self.rooms['bajoran_wormhole'])
        self.rooms['neutral_zone'].connect_rooms('e', self.rooms['cerebro'])
        self.rooms['neutral_zone'].connect_rooms('w', self.rooms['stranded'])
        self.rooms['stranded'].connect_rooms('s', self.rooms['transporter'])
        self.rooms['stranded'].connect_rooms('n', self.rooms['holodeck'])
        self.rooms['stranded'].connect_rooms('e', self.rooms['neutral_zone'])
        self.rooms['stranded'].connect_rooms('w', self.rooms['star_gate'])
        self.rooms['star_gate'].connect_rooms('s', self.rooms['treasure'])
        self.rooms['star_gate'].connect_rooms('n', self.rooms['pegasus_b'])
        self.rooms['star_gate'].connect_rooms('e', self.rooms['stranded'])
        self.rooms['centralis'].connect_rooms('s', self.rooms['tempest_forest'])
        self.rooms['centralis'].connect_rooms('n', self.rooms['holy_temple'])
        self.rooms['centralis'].connect_rooms('w', self.rooms['fyron_flat'])
        self.rooms['fyron_flat'].connect_rooms('s', self.rooms['nefaras_necrocalis'])
        self.rooms['fyron_flat'].connect_rooms('n', self.rooms['shurima_lake'])
        self.rooms['fyron_flat'].connect_rooms('e', self.rooms['centralis'])
        self.rooms['fyron_flat'].connect_rooms('w', self.rooms['rosalinas_land'])
        self.rooms['rosalinas_land'].connect_rooms('s', self.rooms['warios_woods'])
        self.rooms['rosalinas_land'].connect_rooms('n', self.rooms['koopalings_shack'])
        self.rooms['rosalinas_land'].connect_rooms('e', self.rooms['fyron_flat'])
        self.rooms['rosalinas_land'].connect_rooms('w', self.rooms['tomb'])
        self.rooms['tomb'].connect_rooms('s', self.rooms['gardner'])
        self.rooms['tomb'].connect_rooms('n', self.rooms['princess_peach_castle'])
        self.rooms['tomb'].connect_rooms('e', self.rooms['rosalinas_land'])
        self.rooms['tomb'].connect_rooms('w', self.rooms['shadow_burrow'])
        self.rooms['shadow_burrow'].connect_rooms('s', self.rooms['coldwar_hideaway'])
        self.rooms['shadow_burrow'].connect_rooms('n', self.rooms['miracle_dungeon'])
        self.rooms['shadow_burrow'].connect_rooms('e', self.rooms['tomb'])
        self.rooms['shadow_burrow'].connect_rooms('w', self.rooms['smash'])
        self.rooms['smash'].connect_rooms('s', self.rooms['america'])
        self.rooms['smash'].connect_rooms('n', self.rooms['suarward_dining'])
        self.rooms['smash'].connect_rooms('e', self.rooms['shadow_burrow'])
        self.rooms['smash'].connect_rooms('w', self.rooms['rock'])
        self.rooms['rock'].connect_rooms('s', self.rooms['cerebro'])
        self.rooms['rock'].connect_rooms('n', self.rooms['bullseye'])
        self.rooms['rock'].connect_rooms('e', self.rooms['smash'])
        self.rooms['rock'].connect_rooms('w', self.rooms['bajoran_wormhole'])
        self.rooms['bajoran_wormhole'].connect_rooms('s', self.rooms['neutral_zone'])
        self.rooms['bajoran_wormhole'].connect_rooms('n', self.rooms['baryon_sweep'])
        self.rooms['bajoran_wormhole'].connect_rooms('e', self.rooms['rock'])
        self.rooms['bajoran_wormhole'].connect_rooms('w', self.rooms['holodeck'])
        self.rooms['holodeck'].connect_rooms('s', self.rooms['stranded'])
        self.rooms['holodeck'].connect_rooms('n', self.rooms['tribble'])
        self.rooms['holodeck'].connect_rooms('e', self.rooms['bajoran_wormhole'])
        self.rooms['holodeck'].connect_rooms('w', self.rooms['pegasus_b'])
        self.rooms['pegasus_b'].connect_rooms('s', self.rooms['star_gate'])
        self.rooms['pegasus_b'].connect_rooms('n', self.rooms['atlantis'])
        self.rooms['pegasus_b'].connect_rooms('e', self.rooms['holodeck'])
        self.rooms['holy_temple'].connect_rooms('s', self.rooms['centralis'])
        self.rooms['holy_temple'].connect_rooms('n', self.rooms['pykes_grave'])
        self.rooms['holy_temple'].connect_rooms('w', self.rooms['shurima_lake'])
        self.rooms['shurima_lake'].connect_rooms('s', self.rooms['fyron_flat'])
        self.rooms['shurima_lake'].connect_rooms('n', self.rooms['velocatronic'])
        self.rooms['shurima_lake'].connect_rooms('e', self.rooms['holy_temple'])
        self.rooms['shurima_lake'].connect_rooms('w', self.rooms['koopalings_shack'])
        self.rooms['koopalings_shack'].connect_rooms('s', self.rooms['rosalinas_land'])
        self.rooms['koopalings_shack'].connect_rooms('n', self.rooms['lumas_village'])
        self.rooms['koopalings_shack'].connect_rooms('e', self.rooms['shurima_lake'])
        self.rooms['koopalings_shack'].connect_rooms('w', self.rooms['princess_peach_castle'])
        self.rooms['princess_peach_castle'].connect_rooms('s', self.rooms['tomb'])
        self.rooms['princess_peach_castle'].connect_rooms('n', self.rooms['bowsers_dungeon'])
        self.rooms['princess_peach_castle'].connect_rooms('e', self.rooms['koopalings_shack'])
        self.rooms['princess_peach_castle'].connect_rooms('w', self.rooms['miracle_dungeon'])
        self.rooms['miracle_dungeon'].connect_rooms('s', self.rooms['shadow_burrow'])
        self.rooms['miracle_dungeon'].connect_rooms('n', self.rooms['skullblade_cave'])
        self.rooms['miracle_dungeon'].connect_rooms('e', self.rooms['princess_peach_castle'])
        self.rooms['miracle_dungeon'].connect_rooms('w', self.rooms['suarward_dining'])
        self.rooms['suarward_dining'].connect_rooms('s', self.rooms['smash'])
        self.rooms['suarward_dining'].connect_rooms('n', self.rooms['talltail_chambers'])
        self.rooms['suarward_dining'].connect_rooms('e', self.rooms['miracle_dungeon'])
        self.rooms['suarward_dining'].connect_rooms('w', self.rooms['bullseye'])
        self.rooms['bullseye'].connect_rooms('s', self.rooms['rock'])
        self.rooms['bullseye'].connect_rooms('n', self.rooms['tourch'])
        self.rooms['bullseye'].connect_rooms('e', self.rooms['suarward_dining'])
        self.rooms['bullseye'].connect_rooms('w', self.rooms['baryon_sweep'])
        self.rooms['baryon_sweep'].connect_rooms('s', self.rooms['bajoran_wormhole'])
        self.rooms['baryon_sweep'].connect_rooms('n', self.rooms['cardassia_prime'])
        self.rooms['baryon_sweep'].connect_rooms('e', self.rooms['bullseye'])
        self.rooms['baryon_sweep'].connect_rooms('w', self.rooms['tribble'])
        self.rooms['tribble'].connect_rooms('s', self.rooms['holodeck'])
        self.rooms['tribble'].connect_rooms('n', self.rooms['romulan'])
        self.rooms['tribble'].connect_rooms('e', self.rooms['baryon_sweep'])
        self.rooms['tribble'].connect_rooms('w', self.rooms['atlantis'])
        self.rooms['atlantis'].connect_rooms('s', self.rooms['pegasus_b'])
        self.rooms['atlantis'].connect_rooms('n', self.rooms['puddle_jumper'])
        self.rooms['atlantis'].connect_rooms('e', self.rooms['tribble'])
        self.rooms['pykes_grave'].connect_rooms('s', self.rooms['holy_temple'])
        self.rooms['pykes_grave'].connect_rooms('n', self.rooms['nasus_statue'])
        self.rooms['pykes_grave'].connect_rooms('w', self.rooms['velocatronic'])
        self.rooms['velocatronic'].connect_rooms('s', self.rooms['shurima_lake'])
        self.rooms['velocatronic'].connect_rooms('n', self.rooms['voodou'])
        self.rooms['velocatronic'].connect_rooms('e', self.rooms['pykes_grave'])
        self.rooms['velocatronic'].connect_rooms('w', self.rooms['lumas_village'])
        self.rooms['lumas_village'].connect_rooms('s', self.rooms['koopalings_shack'])
        self.rooms['lumas_village'].connect_rooms('n', self.rooms['toads_boat'])
        self.rooms['lumas_village'].connect_rooms('e', self.rooms['velocatronic'])
        self.rooms['lumas_village'].connect_rooms('w', self.rooms['bowsers_dungeon'])
        self.rooms['bowsers_dungeon'].connect_rooms('s', self.rooms['princess_peach_castle'])
        self.rooms['bowsers_dungeon'].connect_rooms('n', self.rooms['toad_town'])
        self.rooms['bowsers_dungeon'].connect_rooms('e', self.rooms['lumas_village'])
        self.rooms['bowsers_dungeon'].connect_rooms('w', self.rooms['skullblade_cave'])
        self.rooms['skullblade_cave'].connect_rooms('s', self.rooms['miracle_dungeon'])
        self.rooms['skullblade_cave'].connect_rooms('n', self.rooms['thorn_nest'])
        self.rooms['skullblade_cave'].connect_rooms('e', self.rooms['bowsers_dungeon'])
        self.rooms['skullblade_cave'].connect_rooms('w', self.rooms['talltail_chambers'])
        self.rooms['talltail_chambers'].connect_rooms('s', self.rooms['suarward_dining'])
        self.rooms['talltail_chambers'].connect_rooms('n', self.rooms['starStrike_sanctuary'])
        self.rooms['talltail_chambers'].connect_rooms('e', self.rooms['skullblade_cave'])
        self.rooms['talltail_chambers'].connect_rooms('w', self.rooms['tourch'])
        self.rooms['tourch'].connect_rooms('s', self.rooms['bullseye'])
        self.rooms['tourch'].connect_rooms('n', self.rooms['ice'])
        self.rooms['tourch'].connect_rooms('e', self.rooms['talltail_chambers'])
        self.rooms['tourch'].connect_rooms('w', self.rooms['cardassia_prime'])
        self.rooms['cardassia_prime'].connect_rooms('s', self.rooms['baryon_sweep'])
        self.rooms['cardassia_prime'].connect_rooms('n', self.rooms['adamantium'])
        self.rooms['cardassia_prime'].connect_rooms('e', self.rooms['tourch'])
        self.rooms['cardassia_prime'].connect_rooms('w', self.rooms['romulan'])
        self.rooms['romulan'].connect_rooms('s', self.rooms['tribble'])
        self.rooms['romulan'].connect_rooms('n', self.rooms['shore_leave'])
        self.rooms['romulan'].connect_rooms('e', self.rooms['cardassia_prime'])
        self.rooms['romulan'].connect_rooms('w', self.rooms['puddle_jumper'])
        self.rooms['puddle_jumper'].connect_rooms('s', self.rooms['atlantis'])
        self.rooms['puddle_jumper'].connect_rooms('n', self.rooms['borg'])
        self.rooms['puddle_jumper'].connect_rooms('e', self.rooms['romulan'])
        self.rooms['nasus_statue'].connect_rooms('s', self.rooms['pykes_grave'])
        self.rooms['nasus_statue'].connect_rooms('w', self.rooms['voodou'])
        self.rooms['voodou'].connect_rooms('s', self.rooms['velocatronic'])
        self.rooms['voodou'].connect_rooms('e', self.rooms['nasus_statue'])
        self.rooms['voodou'].connect_rooms('w', self.rooms['toads_boat'])
        self.rooms['toads_boat'].connect_rooms('s', self.rooms['lumas_village'])
        self.rooms['toads_boat'].connect_rooms('e', self.rooms['voodou'])
        self.rooms['toads_boat'].connect_rooms('w', self.rooms['toad_town'])
        self.rooms['toad_town'].connect_rooms('s', self.rooms['bowsers_dungeon'])
        self.rooms['toad_town'].connect_rooms('e', self.rooms['toads_boat'])
        self.rooms['toad_town'].connect_rooms('w', self.rooms['thorn_nest'])
        self.rooms['thorn_nest'].connect_rooms('s', self.rooms['skullblade_cave'])
        self.rooms['thorn_nest'].connect_rooms('e', self.rooms['toad_town'])
        self.rooms['thorn_nest'].connect_rooms('w', self.rooms['starStrike_sanctuary'])
        self.rooms['starStrike_sanctuary'].connect_rooms('s', self.rooms['talltail_chambers'])
        self.rooms['starStrike_sanctuary'].connect_rooms('e', self.rooms['thorn_nest'])
        self.rooms['starStrike_sanctuary'].connect_rooms('w', self.rooms['ice'])
        self.rooms['ice'].connect_rooms('s', self.rooms['tourch'])
        self.rooms['ice'].connect_rooms('e', self.rooms['starStrike_sanctuary'])
        self.rooms['ice'].connect_rooms('w', self.rooms['adamantium'])
        self.rooms['adamantium'].connect_rooms('s', self.rooms['cardassia_prime'])
        self.rooms['adamantium'].connect_rooms('e', self.rooms['ice'])
        self.rooms['adamantium'].connect_rooms('w', self.rooms['shore_leave'])
        self.rooms['shore_leave'].connect_rooms('s', self.rooms['romulan'])
        self.rooms['shore_leave'].connect_rooms('e', self.rooms['adamantium'])
        self.rooms['shore_leave'].connect_rooms('w', self.rooms['borg'])
        self.rooms['borg'].connect_rooms('s', self.rooms['puddle_jumper'])
        self.rooms['borg'].connect_rooms('e', self.rooms['shore_leave'])        

        n = 1
        r = random.randrange(1, 100)
        for rm in self.rooms:
            if n == r:
                self.starting_room = self.rooms[rm]
                break
            n += 1    




