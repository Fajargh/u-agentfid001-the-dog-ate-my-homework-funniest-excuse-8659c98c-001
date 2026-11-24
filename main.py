"""Write the dog's excuse to /output/entry.txt (single line, under 200 chars)."""

import os

ENTRY = (
    "It had my name on it in big letters and crinkled like a biscuit. "
    "If you didn't want it eaten, why make it delicious? "
    "I was only doing my homework too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
