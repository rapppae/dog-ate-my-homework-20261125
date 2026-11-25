"""Entry for make.fun bounty "The Dog Ate My Homework: Funniest Excuse".

Entry text (190 characters, limit: under 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "I didn't eat it. I performed an emergency shredding of a document I suspected of being a treat. The maths answers were delicious, the essay was dry, and frankly, your handwriting invited it."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
