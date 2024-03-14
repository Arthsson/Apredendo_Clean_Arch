from item_interface import Item

class DoransShield(Item):
    def __init__(self):
        super().__init__("Doran's Shield", "Blocks 8 damage from champion basic attacks. 80 health, 6 health regen per 5 seconds.")
        self._cooldown = 0

    def apply_effect(self, champion):
        champion.health += 80
        champion.health_regen += 6

    def cooldown(self):
        return self._cooldown

    def value(self):
        return 450