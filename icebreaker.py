import random


class Icebreaker:

    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.name = name

        # TODO: controlla che min_damage >= 1
        # Se non lo è, stampa un avviso e correggilo a 1
        self.min_damage = min_damage
        if min_damage < 1:
            print("Attenzione: min_damage deve essere >= 1. Corretto a 1.")
            self.min_damage = 1

        # TODO: controlla che max_damage >= min_damage
        # Se non lo è, stampa un avviso e correggilo
        self.max_damage = max_damage
        if self.max_damage < self.min_damage:
            print("Attenzione: max_damage deve essere >= min_damage.")
            self.max_damage = self.min_damage

        # TODO: controlla che type sia "fracter" o "decoder"
        # Se non lo è, stampa un avviso e scegli un default
        self.type = type
        if type != "fracter" and type != "decoder":
            print(f"Attenzione: type deve essere 'fracter' o 'decoder'. Corretto a 'decoder'.")
            self.type = "decoder"

    def get_damage(self) -> int:
        # TODO: restituisci un intero casuale tra min_damage e max_damage
        return random.randint(self.min_damage, self.max_damage)

    def __str__(self) -> str:
        # TODO: restituisci una stringa tipo "Pipeline Decoder (8–13 dmg)"
        # Nota: il trattino è un en-dash –, non un meno -
        return f"{self.name} {self.type.capitalize()} ({self.min_damage}–{self.max_damage} dmg)"