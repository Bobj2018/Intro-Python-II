# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        super().__init__()
        self.name = name
        self.current_room = current_room

    def announce(self):
        print(f"You enter the {self.current_room.name}")
        print(f"{self.current_room.description}")

    def move(self, direction):
        if (direction == "n"):
            if (self.current_room.n_to):
                self.current_room = self.current_room.n_to
                self.announce()
        elif(direction == "s"):
            if (self.current_room.s_to):
                self.current_room = self.current_room.s_to
                self.announce()
        elif(direction == "e"):
            if (self.current_room.e_to):
                self.current_room = self.current_room.e_to
                self.announce()
        elif(direction == "w"):
            if (self.current_room.w_to):
                self.current_room = self.current_room.w_to
                self.announce()
        else:
            print("invalid command: please try again!")

    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"
