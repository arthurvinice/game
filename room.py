class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.connected_rooms = {}
        self.char = None

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def connect_room(self, room_to_connect, direction):
        self.connected_rooms[direction] = room_to_connect
        
    def set_chat(self, new_char):
        self.char = new_char
        

    def details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction in self.connected_rooms:
            room = self.connected_rooms[direction]
            print(f'The {room.get_name()} is to the {direction}')

    def move(self, direction):
        if direction in self.connected_rooms:
            return self.connected_rooms[direction]
        else:
            print("You can't go that way!!")
            return self