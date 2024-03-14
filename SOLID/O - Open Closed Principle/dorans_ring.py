from item_interface import Item

class DoransRing(Item):
    def __init__(self):
        super().__init__("Doran's Ring", "Gain 4 mana per 5 seconds. 15 ability power, 60 health.")
        self._cooldown = 0

    def apply_effect(self, champion):
        champion.mana_regen += 4
        champion.ability_power += 15
        champion.health += 60

    def cooldown(self):
        return self._cooldown

    def value(self):
        return 400