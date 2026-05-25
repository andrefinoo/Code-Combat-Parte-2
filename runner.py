from icebreaker import Icebreaker


class Runner:

    def __init__(self, handle: str, max_integrity: int, power: int, finesse: int):
        self.handle = handle

        # TODO: controlla che max_integrity >= 1, correggi a 1 se necessario
        self.max_integrity = max_integrity
        if max_integrity < 1:
            print("Attenzione: max_integrity deve essere >= 1. Corretto a 1.")
            self.max_integrity = 1
        self.integrity = self.max_integrity

        # TODO: controlla che power sia in [1, 20], clampa se necessario
        self.power = power
        if power != max(1, min(20, power)):
            print("Attenzione: power fuori range. Corretto.")
        self.power = max(1, min(20, power))

        # TODO: controlla che finesse sia in [1, 20], clampa se necessario
        self.finesse = finesse
        if finesse != max(1, min(20, finesse)):
            print("Attenzione: finesse fuori range. Corretto.")
        self.finesse = max(1, min(20, finesse))
        self.icebreaker = None           # nessun icebreaker all'inizio

    def equip(self, icebreaker: Icebreaker) -> None:
        # TODO: assegna l'icebreaker al runner (una riga)
        self.icebreaker = icebreaker

    def modifier(self, value: int) -> int:
        # TODO: restituisci (value - 10) // 2  (una riga)
        return (value - 10) // 2

    def is_alive(self) -> bool:
        # TODO: restituisci True se integrity > 0  (una riga)
        return self.integrity > 0

    def take_damage(self, amount: int) -> int:
        # TODO: riduci integrity (mai sotto 0) e restituisci il danno effettivo
        # Suggerimento: usa min() per clampare il danno a integrity disponibile
        damage_taken = min(amount, self.integrity)
        self.integrity -= damage_taken
        return damage_taken

    def attack(self, enemy: "Runner") -> int:
        # TODO (passo 1): decidi il danno base
        #   - se self.icebreaker è None → danno base = 1
        #   - altrimenti → danno base = self.icebreaker.get_damage()
        # TODO (passo 2): scegli il modificatore corretto
        #   - se l'icebreaker è "fracter" → usa self.power
        #   - se è "decoder" → usa self.finesse
        #   - applicalo con self.modifier(...)
        if self.icebreaker is None:
            base_damage = 1
            damage_modifier = 0  # nessun modificatore senza arma
        else:
            base_damage = self.icebreaker.get_damage()
            if self.icebreaker.type == "fracter":
                damage_modifier = self.modifier(self.power)
            else:
                damage_modifier = self.modifier(self.finesse)


        # TODO (passo 3): il danno totale non può scendere sotto 0
        total_damage = max(0, base_damage + damage_modifier)

        # TODO (passo 4): chiama enemy.take_damage(...) e restituisci il risultato
        return enemy.take_damage(total_damage)

    def __str__(self) -> str:
        # TODO: es. "armitage (Integrity: 32/50)"
        return f"{self.handle} (Integrity: {self.integrity}/{self.max_integrity})"