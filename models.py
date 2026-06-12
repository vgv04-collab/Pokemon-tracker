# models.py

class PokemonState:
    def __init__(self, name):
        self.name = name
        self.item = "unknown"
        self.moves = set()
        self.status = "none"

    def to_dict(self):
        return {
            "name": self.name,
            "item": self.item,
            "moves": list(self.moves),
            "status": self.status
        }