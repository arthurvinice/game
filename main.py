from room import Room
from character import Enemy
from character import Merchant

kitchen = Room('Kitchen')
kitchen.set_description("A cold and dirty place. Looks like power is down...Seems like I'm all alone in here... I must keep going.")

dinner_room = Room('Dinner Room')
dinner_room.set_description("A big room with a large table and chairs. The walls are decorated with pictures and golden items. There is a person in the left corner... Should I talk to him?")

party_room = Room('Party Room')
party_room.set_description("A wide room with shine wood floor, with large candlesticks guarding the entrance and a chandelier int the middle. Looks like I'm not alone in here... What would happen if I type 'chat'? ")

kitchen.connect_room(dinner_room, 'south')
dinner_room.connect_room(kitchen, 'north')
dinner_room.connect_room(party_room, 'east')
party_room.connect_room(dinner_room, 'west')

current_room = kitchen
enemy = Enemy('Bob', 'A weird skeletal figure draped in tattered, writhing, shadowy robes.')
merchant = Merchant('Ludwig', "An old and short man with grey hair and long beard. He carries a backpack.")

while True:
    print()
    current_room.details()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "chat":
        if current_room == kitchen:
            current_room.details()
            command = input("> ")
            current_room = current_room.move(command)
            current_room.details()
        if current_room == dinner_room and merchant != None:
            merchant.describe()
            merchant.set_speech("Time's river flows, but its wisdom lingers in the tales of the road.")
            merchant.chat()
            check_item = merchant.get_item()
            merchant = None
        if current_room == party_room and enemy != None:
            current_room.details()
            enemy.describe()
            enemy.set_speech("Embrace the void, for I am the whisper in your nightmares...")
            enemy.chat()
            enemy.set_weakness('solar relic')
            print('What item will you use? ')
            fight_item = input('> ')
            if enemy.fight(fight_item):
                print(f'You defeated Bob! \nYOU WON!!')
                enemy = None
                continue
            else:
                print(f'You just died! \nGAME OVER!')
                break
        if enemy == None:
            party_room.set_description("A wide room with shine wood floor, with large candlesticks guarding the entrance and a chandelier int the middle. There's a dead monster and it smells terrible... Nothing to do here..")
        if merchant == None:
            dinner_room.set_description("A big room with a large table and chairs. The walls are decorated with pictures and golden items. There is no one here..")
            continue

            
        
            
            
            
    
        
