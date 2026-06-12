# state.py

from models import PokemonState

class BattleState:
    def __init__(self):
        self.pokemon = {}

    def get(self, name):
        if name not in self.pokemon:
            self.pokemon[name] = PokemonState(name)
        return self.pokemon[name]

    def to_dict(self):
        return {name: p.to_dict() for name, p in self.pokemon.items()}