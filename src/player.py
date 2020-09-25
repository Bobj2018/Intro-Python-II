# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def announce(self):
        itm = []
        msg = "The room contains: "
        print(f"You enter the {self.current_room.name}")
        print(f"{self.current_room.description}")
        for item in self.current_room.items:
            itm.append(item.name)
        for i in itm:
            msg += f"{i}, "
        print(msg)

    def add_item(self, item):
        self.items.append(item)
        self.current_room.remove_item(item)
        pass

    def action(self, command):
        cmds = command.split(" ", 1)
        if (len(cmds) > 1):
            if (cmds[0].lower() == "take"):
                    self.add_item(self.current_room.get_item(cmds[1].lower()))
                    print(self.items)
            if (cmds[0].lower() == "go"):
                if (cmds[1].lower() == "north"):
                    if (self.current_room.n_to):
                        self.current_room = self.current_room.n_to
                        self.announce()
                elif(cmds[1].lower() == "south"):
                    if (self.current_room.s_to):
                        self.current_room = self.current_room.s_to
                        self.announce()
                elif(cmds[1].lower() == "east"):
                    if (self.current_room.e_to):
                        self.current_room = self.current_room.e_to
                        self.announce()
                elif(cmds[1].lower() == "west"):
                    if (self.current_room.w_to):
                        self.current_room = self.current_room.w_to
                        self.announce()
                else:
                    print("invalid command: please try again!")
        else:
            print("invalid command: please try again!")

    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"
