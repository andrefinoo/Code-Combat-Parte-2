from random import randint
from icebreaker import Icebreaker
from runner import Runner


if __name__ == "__main__":

    # --- 1. Crea i due Runner con statistiche casuali ---
    armitage = Runner("armitage", max_integrity=50, power=randint(1,20), finesse=randint(1,20))
    molly = Runner("molly",    max_integrity=50, power=randint(1,20), finesse=randint(1,20))

    # --- 2. Scegli l'icebreaker giusto per ciascun Runner ---
    # Se power > finesse → "fracter", altrimenti → "decoder"
    # Inventa nome e range di danno a piacere
    if armitage.power > armitage.finesse:
        armitage_icebreaker = Icebreaker("Pipeline", 8, 13, "fracter")
    else:
        armitage_icebreaker = Icebreaker("Pipeline", 8, 13, "decoder")
    if molly.power > molly.finesse:
        molly_icebreaker = Icebreaker("Pipeline", 8, 13, "fracter")
    else:
        molly_icebreaker = Icebreaker("Pipeline", 8, 13, "decoder")
    # --- 3. Equipaggia ---
    armitage.equip(armitage_icebreaker)
    molly.equip(molly_icebreaker)


    # --- 4. Stampa l'intestazione ---
    print("=== NETRUN DUEL ===\n")
    # TODO: stampa power e finesse di ciascun runner
    print(f"{armitage.handle}: Power={armitage.power}, Finesse={armitage.finesse}")
    print(f"{molly.handle}: Power={molly.power}, Finesse={molly.finesse}")
    # TODO: stampa quale icebreaker ha equipaggiato ciascuno
    print(f"{armitage.handle} ha equipaggiato {armitage_icebreaker}")
    print(f"{molly.handle} ha equipaggiato {molly_icebreaker}")

    print("\n=== INIZIO COMBATTIMENTO ===\n")

    # --- 5. Game loop ---
    turno = 1
    combattenti = [armitage,molly ]   # TODO: metti qui i due runner

    # Nota di design: in questo loop entrambi i runner attaccano nello stesso turno.
    # Questo significa che è possibile un pareggio se muoiono entrambi al turno N.
    # Il primo della lista ha però un lieve vantaggio strutturale perché attacca prima.

    while True:
        print(f"--- Turno {turno} ---")

        # TODO: chi attacca chi?
        attaccante = combattenti[(turno + 1) % 2]
        bersaglio  = combattenti[turno % 2]

        # TODO: esegui l'attacco e stampa il risultato
        danno = attaccante.attack(bersaglio)
        print(f"{attaccante.handle} attacca {bersaglio.handle} e infligge {danno} danni")
        print(bersaglio)

        # TODO: controlla se il bersaglio è ancora vivo; se no, esci dal loop
        if not bersaglio.is_alive():
            break

        turno += 1
        print()

    # --- 6. Dichiara il vincitore ---
    print("\n=== FINE COMBATTIMENTO ===\n")
    # TODO: chi ha vinto? Considera il caso di pareggio (entrambi a 0)
    if armitage.is_alive() and not molly.is_alive():
        print(f"{armitage.handle} vince!")
    elif molly.is_alive() and not armitage.is_alive():
        print(f"{molly.handle} vince!")
    else:
        print("Pareggio!")