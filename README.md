# 🎮 Azaf's Ultimate Number Guessing Game 🐍

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

### 📝 Project Description
🎮 A fun, terminal-based Number Guessing Game built in Python where you try to guess a secret number between 1 and 100! 🐍 It guides you along the way with instant 📉 "too low" or 📈 "too high" hints, while automatically tracking and saving your all-time best score to a local file so you can continuously smash your own high score. 🏆🔄

---

## 🚀 Features

* **🔢 Dynamic Number Generation:** Automatically picks a random secret number between `1` and `100` every round.
* **💡 Intelligent Live Hints:** Gives real-time 📉 **Too Low** or 📈 **Too High** feedback to guide your next strategic guess.
* **🏆 Local High Score Leaderboard:** Automatically creates and updates a `high_score.txt` file on your computer. It remembers your best record even after you close the terminal!
* **🛡️ Crash-Proof Input Handling:** Safeguarded against accidental typos. If you enter letters or symbols, the game gently reminds you to type a number instead of crashing.
* **🔄 Seamless Replay Loop:** Allows you to jump straight into a new game instantly so you can try to break your own record.

---

## 📦 Project Structure

```text
├── Number_Guessing_Game.py  # The main Python script
└── high_score.txt           # Generated automatically to store your best score

```
---
## 🧠 How It Works

Behind the scenes, the script relies on a clean, efficient logic flow to keep the game running smoothly:

* **🏆 High Score Initialization:** When launched, the program looks for `high_score.txt` in the same directory. If it finds the file, it reads and displays your current best score. If it doesn't find it (like your very first run), it gracefully handles the missing file error and sets a fresh starting baseline.
* **🎲 Secret Number Generation:** The script imports Python's built-in `random` module and uses `random.randint(1, 100)` to lock in a hidden number at the start of each round.
* **🛡️ The Input & Validation Loop:** Every time you type a guess, the game checks your input using a `try-except` block. If you type letters or symbols, it catches the error instantly, displays a warning, and lets you try again without breaking the game loop.
* **⚖️ Comparison Logic:** A series of `if/elif/else` statements compare your guess to the secret number, tracking your total number of attempts along the way.
* **💾 Score Persistence:** Once you guess correctly, the program compares your current attempts to the historical high score. If your current run is faster, it opens `high_score.txt` in write mode (`"w"`) and replaces the old record with your new one.
* ---

* ## 🕹️ Gameplay Walkthrough

* **👋 The Welcome Screen:** The game boots up, initializes, and checks if you have a pre-existing high score to beat.
* **🤔 The Guessing Phase:** Enter a number between 1 and 100.
* **🎉 The Victory Screen:** Once you guess correctly, the game calculates your total attempts. If it's a new personal best, it saves it instantly! 🥳
* **🔄 The Choice:** Type `yes` to play again or `no` to exit like a champ.

> 💡 **Pro-Tip:** The fewer the attempts, the better your high score! Can you get it in under 7 guesses? 😉
>
> ---
