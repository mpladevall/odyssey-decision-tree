"""
prophecy.py

Teiresias's prophecy to Odysseus (Odyssey, Book 11) modelled as a binary
decision tree — demonstrating that a "mystical prophecy" is structurally
just a nested if/else statement.

Decision structure
------------------
Primary branch : Does the crew slaughter the cattle of the sun god Helios
                 on the island of Thrinakia?

  YES → The sun god demands punishment; Zeus destroys the ship and all
        sailors aboard. Odysseus alone survives, but he washes ashore on
        Ogygia and is stranded for years before a long, hard journey home.

  NO  → Nested branch: Does the whole crew remain disciplined throughout
        the voyage home?

        YES → The crew returns safely, and Odysseus eventually reaches
              Ithaca and is reunited with his household.

        NO  → Even without touching the forbidden cattle, internal
              breakdowns (disobedience, in-fighting, reckless behaviour)
              lead to losses; Odysseus still makes it home but only after
              additional suffering and the loss of men.
"""


def prophecy(crew_touches_cattle: bool, crew_stays_disciplined: bool) -> str:
    """
    Return the prophesied outcome given two key decisions.

    Parameters
    ----------
    crew_touches_cattle : bool
        True if the crew kills and eats the cattle of Helios on Thrinakia.
    crew_stays_disciplined : bool
        True if the crew obeys orders and avoids reckless behaviour.
        Only meaningful when crew_touches_cattle is False.

    Returns
    -------
    str
        A plain-language description of the prophesied outcome.
    """
    if crew_touches_cattle:
        return (
            "The sun god's wrath is unavoidable. Zeus strikes the ship with a "
            "thunderbolt; every sailor perishes. Odysseus alone clings to wreckage, "
            "drifts to a distant island, and is marooned for years before an "
            "agonising journey finally brings him home — alone and unrecognised."
        )
    else:
        if crew_stays_disciplined:
            return (
                "The cattle are left untouched and the crew holds together. "
                "The voyage home is still dangerous, but the men survive, "
                "and Odysseus returns to Ithaca to reclaim his household."
            )
        else:
            return (
                "The cattle are spared, but discord and disobedience take their toll. "
                "Odysseus endures further hardship and loses more companions before "
                "finally making it back to Ithaca — diminished but alive."
            )


def run_all_scenarios() -> None:
    """Print the outcome for every combination of the two decision variables."""
    scenarios = [
        (True,  True,  "Crew touches cattle / crew disciplined"),
        (True,  False, "Crew touches cattle / crew not disciplined"),
        (False, True,  "Crew spares cattle  / crew disciplined"),
        (False, False, "Crew spares cattle  / crew not disciplined"),
    ]

    for touches, disciplined, label in scenarios:
        outcome = prophecy(touches, disciplined)
        print(f"Scenario : {label}")
        print(f"Outcome  : {outcome}")
        print()


if __name__ == "__main__":
    run_all_scenarios()
