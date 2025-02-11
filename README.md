# Hangman Game

This repository contains the implementation of a classic Hangman game in Python. The game is built using two main files: `main.py` and `hangman.py`.

## Features

- The word is randomly fetched from the Vercel API.
- The player can choose the length of the word.
- You have 9 tries to guess the word.
- The game tracks your win streak.
- Upcoming features include:
  - Providing hints based on the word length.
  - Allowing the player to choose the difficulty level of the word.

## Files Overview

### `main.py`
- This is the main entry point of the Hangman game.
- It initializes the game, manages user interaction, and displays the game progress.

### `hangman.py`
- Contains the logic for the Hangman game, such as choosing words, checking guesses, tracking remaining attempts, and determining win/loss conditions.

## How to Run

1. Clone this repository to your local machine.
   ```bash
   git clone <(https://github.com/KrypticKourosh/hangman_game)>

2.Navigate to the project directory.
  ```bash
  cd <project-directory>
```
3. Run the game using python.
  ```bash
  python main.py
