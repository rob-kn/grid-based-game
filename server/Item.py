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
    def __init__(self, item_id, item_type):
        self.item_id = item_id
        self.type = item_type
        self.name = item_types[item_type]["name"]
        self.image = item_types[item_type]["image"]
        self.can_carry = item_types[item_type]["can_carry"]


class HealthKit(Item):
    def __init__(self, item_id, x, y):
        super(HealthKit, self).__init__(item_id, "health_kit")
        self.x = x
        self.y = y
        self.offset = (0, 0)
        self.health_increase = 30
        items[item_id] = self

    def use_on_target(self, target_sprite):
        target_sprite.change_health(target_sprite.health + self.health_increase)
        return self.item_id
