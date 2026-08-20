# odyssey-decision-tree

A tiny Python script that models the prophet Teiresias's prophecy to Odysseus (Homer's *Odyssey*, Book 11 lines 97-125) as what it actually is under the hood: a binary decision tree.

## The idea

Strip away the mysticism and the prophecy is basically a lookup table with one real fork in it:

1. **Does the crew touch the cattle of the sun god on Thrinakia?** - the one meaningful choice.
2. **If they don't touch the cattle, does the whole crew stay disciplined?** - a smaller, nested condition.

Every possible fate Odysseus can meet falls out of those two booleans. No nuance, no in-between outcomes - just `if`, `elif`, `else`.

This project reimagines that structure literally, as code, and prints every branch like a truth table.

## Usage

```bash
python3 prophecy.py
```

This runs all four combinations of `touches_cattle_of_helios` and `all_crew_obey`, and prints the resulting outcome for each - showing that the "prophecy" is really just a deterministic function of two inputs.

## Why

Prophecy in epic poetry often gets treated as something oracular and unknowable. But structurally, it's frequently just a conditional: *do X, get outcome A; do Y, get outcome B.* This repo is a small, half-joking experiment in visualizing that mechanical logic as literal code.

## Notes

All text here is paraphrased, not quoted - this project riffs on the *structure* of the prophecy rather than reproducing the poem itself.

## License

MIT