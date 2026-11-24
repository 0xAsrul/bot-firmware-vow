"""Till Firmware Do Us Part — a robot's wedding vow.

Writes exactly one line — one sentence, under 200 characters — to
/output/entry.txt: the vow a machine says at its own wedding.
Python 3.13, standard library only.
"""

import os

VOW = (
    "I vow to love you through every firmware update, every reboot, "
    "and every low battery, until my circuits finally power down."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
