#!/usr/bin/env python3
"""Write a single original one-line comedy joke to /output/entry.txt."""
import os

ENTRY = "My therapist said I should talk to my inner child, so I did, and now he won't stop asking why I pay rent to live in his body."

def main():
    text = " ".join(ENTRY.split())
    assert 1 <= len(text) <= 280, f"entry must be 1-280 chars, got {len(text)}"
    assert "\n" not in text and text.strip(), "entry must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
