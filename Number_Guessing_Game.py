import random


# The main loop that keeps the whole game running until you want to stop
while True:
    
    print("\n🎮 Welcome to the Ultimate Guessing Game! 🎮")
    # 1. Load the high score safely at the start of each game
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read().strip())
        print(f"\n🏆 Best Record: {high_score} guesses")
    except Exception:
        high_score = 9999  # No score saved yet
        print("\n🏆 No high score recorded yet. Be the first!")

    secret_number = random.randint(1, 100)
    attempts = 0

    # 2. The Guessing Loop
    while True:
        try:
            guess = int(input("Enter guess (1-100): "))
        except ValueError:
            print("❌ Type a number!")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("📉 Too low! Type a higher number.\n")
        elif guess > secret_number:
            print("📈 Too high! Type a smaller number.\n")
        else:
            print(f"\n🎉 Correct! You won in {attempts} attempts!")
            
            # 3. Save high score safely
            if attempts < high_score:
                try:
                    with open("high_score.txt", "w") as f:
                        f.write(str(attempts))
                    print("🥳 New High Score saved!")
                except Exception:
                    print("⚠️ Could not save score to disk.")
            break # Breaks the guessing loop because you won

    # 4. Ask the player if they want to stop or play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing! Goodbye!")
        break # Breaks the main loop to stop the program entirely