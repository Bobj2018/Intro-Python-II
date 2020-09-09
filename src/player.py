# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        super().__init__()
        self.name = name
        self.current_room = current_room

    def announce(self, room):
        print(f"You enter the {room.name}")
        print(f"{room.description}")

    def move(self, direction):
        if (direction == "n"):
            if (self.current_room.n_to):
                self.current_room = self.current_room.n_to
                self.announce(self.current_room)
        elif(direction == "s"):
            if (self.current_room.s_to):
                self.current_room = self.current_room.s_to
                self.announce(self.current_room)
        elif(direction == "e"):
            if (self.current_room.e_to):
                self.current_room = self.current_room.e_to
                self.announce(self.current_room)
        elif(direction == "w"):
            if (self.current_room.w_to):
                self.current_room = self.current_room.w_to
                self.announce(self.current_room)
        else:
            print("invalid command: please try again!")
