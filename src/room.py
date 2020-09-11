# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_item(self, item):
        for i in self.items:
            if(i.name.lower() == item.lower()):
                return(i)

    def remove_item(self, item):
        self.items.remove(item)
        print(self.items)

    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"
