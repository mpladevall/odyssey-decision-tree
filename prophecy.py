"""
prophecy.py

Teiresias's prophecy to Odysseus (Odyssey, Book 11) modelled as a binary
decision tree-demonstrating that a "mystical prophecy" is structurally
just a nested if/else statement.

Decision structure
-------------------
Primary branch  : Does the crew touch the cattle of the sun god Helios on
                   the island of Thrinakia?
  YES -> Nested branch: Does Odysseus himself also touch the cattle, or
         does he hold back while the crew does not?
         crew only    -> The sun god's wrath falls on the ship. Everyone
                          but Odysseus is lost; he alone survives, stranded
                          for years before a long, hard journey home.
                          (WORST CASE)
         crew + him   -> Nobody is spared restraint, nobody is spared the
                          consequences either. Total loss. (CATASTROPHE)
  NO  -> Nested branch: Are the companions contained-do they stay
         disciplined for the rest of the voyage?
         YES -> Everyone gets home, Odysseus reclaims his household.
                (HAPPY PATH)
         NO  -> Odysseus still makes it back, but only after more losses
                and hardship. (COSTLY PATH)

Final trial (applies no matter which path got him home):
Once Odysseus is back on Ithaka, he still has to deal with the suitors who
have overrun his household-kill them, then carry his oar inland until
he finds people who have never seen the sea, and make peace with Poseidon.
This stage isn't a branch-it's a mandatory step that runs after any
successful return, regardless of which path led there.

No mysticism required-just a few booleans, a lookup table, and one
guaranteed final boss.
"""

from dataclasses import dataclass

# ANSI color codes-no external deps needed
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


@dataclass
class Outcome:
    label: str
    color: str
    description: str


def prophecy(
    crew_touches_cattle: bool,
    odysseus_also_touches: bool = False,
    companions_contained: bool = True,
) -> Outcome:
    """
    Return the prophesied outcome given the key decisions.

    Parameters
    ----------
    crew_touches_cattle : bool
        True if the crew kills and eats the cattle of Helios on Thrinakia.
    odysseus_also_touches : bool
        True if Odysseus himself joins in, rather than holding back.
        Only meaningful when crew_touches_cattle is True.
    companions_contained : bool
        True if the companions stay disciplined for the rest of the
        voyage. Only meaningful when crew_touches_cattle is False.
    """
    if crew_touches_cattle:
        if odysseus_also_touches:
            return Outcome(
                label="CATASTROPHE",
                color=RED,
                description=(
                    "Nobody holds back this time. The sun god's wrath falls "
                    "on everyone aboard, Odysseus included. There is no "
                    "survivor left to carry the story home."
                ),
            )
        else:
            return Outcome(
                label="WORST CASE",
                color=RED,
                description=(
                    "The crew touches the cattle, but Odysseus himself holds "
                    "back. The sun god's wrath still falls on the ship-it "
                    "is destroyed and every other sailor perishes. Odysseus "
                    "alone survives, drifting to a distant island before an "
                    "agonising journey finally brings him home-alone, "
                    "unrecognised, and on a stranger's ship."
                ),
            )
    elif companions_contained:
        return Outcome(
            label="HAPPY PATH",
            color=GREEN,
            description=(
                "The cattle are left untouched and the companions stay "
                "contained. The voyage stays dangerous, but the men survive, "
                "and Odysseus reaches Ithaka with his household intact."
            ),
        )
    else:
        return Outcome(
            label="COSTLY PATH",
            color=YELLOW,
            description=(
                "The cattle are spared, but the companions aren't contained "
                "for long-discord and disobedience take their toll. "
                "Odysseus endures further hardship and loses more "
                "companions before finally making it home-diminished but "
                "alive."
            ),
        )


def kill_suitors(method: str = "treachery") -> str:
    """
    The "try"-Odysseus is granted one move: deal with the suitors who
    have overrun his household. The prophecy allows either method.
    """
    if method not in ("treachery", "open force"):
        raise ValueError("method must be 'treachery' or 'open force'")
    return (
        "Reaching home is never the end of it. Odysseus finds his house "
        "full of suitors who have spent years eating through his estate "
        f"and courting his wife. The prophecy grants him one move: kill "
        f"them, by {method}."
    )


def carry_the_oar_inland() -> str:
    """
    The "finally"-non-negotiable, and it runs immediately after the
    suitors are dealt with, no matter which method was used above.
    """
    return (
        "Immediately after-no delay, no choice in the matter-he must "
        "shoulder his oar and travel inland until he finds people who have "
        "never seen the sea, and make his peace with Poseidon there."
    )


def face_the_suitors(method: str = "treachery") -> str:
    """
    The final trial, common to every path that gets Odysseus home at all.

    Structured like try/finally on purpose: killing the suitors is the
    part with a choice in it (treachery vs. open force-the "try").
    The oar journey afterward isn't a branch or a choice at all-it
    runs unconditionally, the moment the suitors are dealt with, exactly
    like a `finally` block that fires no matter what happened above it.
    """
    try:
        suitors_result = kill_suitors(method)
    finally:
        oar_result = carry_the_oar_inland()

    return f"{suitors_result} {oar_result}"


def print_tree() -> None:
    """Render the decision structure as a small ASCII tree."""
    print(f"{BOLD}{CYAN}The Prophecy, as a decision tree:{RESET}\n")
    print("                      crew_touches_cattle_of_helios?")
    print("                    /                              \\")
    print(f"                {GREEN}NO{RESET}                                {RED}YES{RESET}")
    print("                 |                                |")
    print("      companions_contained?              odysseus_also_touches?")
    print("           /              \\                  /              \\")
    print(f"        {GREEN}YES{RESET}             {YELLOW}NO{RESET}              {RED}NO{RESET}               {RED}YES{RESET}")
    print("          |                |               |                |")
    print(f"    {GREEN}HAPPY PATH{RESET}     {YELLOW}COSTLY PATH{RESET}     {RED}WORST CASE{RESET}      {RED}CATASTROPHE{RESET}")
    print("           \\               |               |               /")
    print("            \\              |               |              /")
    print("       '-----> face_the_suitors(), if anyone made it home <-----'")
    print("                    (skipped only after CATASTROPHE)\n")


def run_all_scenarios() -> None:
    """Print the outcome for every combination of the decision variables."""
    scenarios = [
        (True, True, True, "Crew touches cattle, Odysseus touches it too"),
        (True, False, True, "Crew touches cattle, Odysseus holds back"),
        (False, False, True, "Cattle spared, companions stay contained"),
        (False, False, False, "Cattle spared, companions lose discipline"),
    ]

    print(f"{BOLD}Running all {len(scenarios)} scenarios...{RESET}\n")
    for touches, also_touches, contained, label in scenarios:
        outcome = prophecy(touches, also_touches, contained)
        print(f"{BOLD}Scenario :{RESET} {label}")
        print(f"{BOLD}Outcome  :{RESET} {outcome.color}{outcome.label}{RESET}")
        print(f"           {outcome.description}")
        if outcome.label != "CATASTROPHE":
            print(f"{BOLD}Then     :{RESET} {face_the_suitors()}")
        print()


if __name__ == "__main__":
    print_tree()
    run_all_scenarios()