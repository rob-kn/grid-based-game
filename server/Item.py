import configuration as conf

item_types = {
    "health_kit": {
        "name": "Health Kit",
        "image": conf.health_potion,
        "can_carry": True,
        "health_increase": 40
    }
}

items = {}


class Item:
    def __init__(self, item_id, type):
        self.item_id = item_id
        self.type = type
        self.name = item_types[type]["name"]
        self.image = item_types[type]["image"]
        self.can_carry = item_types[type]["can_carry"]
        items[item_id] = self


class HealthKit(Item):
    def use_on_target(self, target):
        pass
