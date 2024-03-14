class AbilitiesManager:
    @staticmethod
    def get_champion_abilities(champion):
        return champion.abilities

    @staticmethod
    def add_ability(champion, ability):
        champion.add_ability(ability)

    @staticmethod
    def remove_ability(champion, ability):
        champion.remove_ability(ability)
