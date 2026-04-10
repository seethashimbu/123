import random

choice = input("Choose heads or tails: ").strip().lower()

if choice not in ["heads", "tails"]:
    print("Invalid choice. Please choose 'heads' or 'tails'.")
else:
    outcome = random.choice(["heads", "tails"])
    print(f"Coin toss outcome: {outcome}")

    if outcome == choice:
        print("yes, go ahead fearlessly")
    else:
        print("wait breathe, not all fights are destined to be fought")
