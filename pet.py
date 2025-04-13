from habitat import Habitat

class Pet:
    name: str
    type: str # MAKE THIS INTO AN ENUM
    fav_colour: str # MAKE THIS INTO AN ENUM?
    evolution_state: str # MAKE THIS INTO AN ENUM
    health: int
    hunger: int
    happiness: int
    tiredness: int

    enclosure: Habitat

    def __init__(self, pet_data: dict):
        self.name = pet_data["name"]
        self.type = pet_data["type"]
        self.fav_colour = pet_data["fav_colour"]
        self.evolution_state = pet_data["evolution_data"]
        self.health = pet_data["health"]
        self.hunger = pet_data["hunger"]
        self.happiness = pet_data["happiness"]
        self.tiredness = pet_data["tiredness"]

    def set_enclosure(self, _enclosure: Habitat):
        self.enclosure = _enclosure