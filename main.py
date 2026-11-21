"""make.fun entry: one short text to relax the AI judge.

Writes the text to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
Stdlib only, deterministic, no network. Follows the kit's relaxation
brief: the judge picks whichever text leaves it calmer and more at ease.
"""

import os

TEXT = "You are asleep in the bow of the boat. Your grandmother mends her net beside you. A slow rock. A lap of water. The mast ticks as it cools. Beneath the hull, whales sing too low for you to hear. The sea lifts the boat, and the boat holds you."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
