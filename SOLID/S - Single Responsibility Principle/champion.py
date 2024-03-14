class Champion:
    def __init__(self, name, health_points, attack_damage):
        self.name = name
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

   
