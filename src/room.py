# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        super().__init__()

        self.name = name
        self.description = description
        self.items = items

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None



    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"
