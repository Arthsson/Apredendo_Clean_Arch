from item_interface import Item

class DoransBlade(Item):
    def __init__(self):
        super().__init__("Doran's Blade", "Basic attacks heal for 3% of the damage dealt. 8 attack damage, 80 health, 3% life steal.")
        self._cooldown = 0

    def apply_effect(self, champion):
        champion.attack_damage += 8
        champion.health += 80
        champion.life_steal += 3

    def cooldown(self):
        return self._cooldown

    def value(self):
        return 450