from item_interface import Item

class Cull(Item):
    def __init__(self):
        super().__init__("Cull", "Basic attacks deal an additional 5 physical damage to minions on hit. You gain 1 gold when a minion dies near you.")
        self._cooldown = 0

    def apply_effect(self, champion):
        champion.attack_damage += 7

    def cooldown(self):
        return self._cooldown

    def value(self):
        return 450