public class ChampionService {
    private AbilityRepository abilityRepository;

    public ChampionService(AbilityRepository abilityRepository) {
        this.abilityRepository = abilityRepository;
    }

    public void Ability(Ability ability) {
        repository.useAbility(ability);
    }
}
