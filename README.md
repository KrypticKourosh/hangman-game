# Hangman Game

A console-based Hangman game built in Python inspired by [this tutorial](https://youtu.be/ag8NtD1e0Kc?si=7kKuYNJNSuO9LDAM). The project was enhanced with API work fetching, game mechanics like keeping track of win-streaks, and improved user experience.


## Features (Beyond the tutorial)

- **Dynamic Word Fetching**: Random Word API -> [Random Word API Vercel](https://random-word-api.vercel.app).
- **Session Management**: Complete game loop with replay functionality
- **Enhanced User Interface**: Console clearing after each guess
- **Win Streak Tracking**

## Installation & Setup

### installations
```bash
pip install requests
```

### run the game using:
```bash
python main.py
```

### How to play
1. **Word Length Selection**: Choose difficulty by selecting word length (3-9 characters)
2. **Letter Guessing**: Enter single letters to guess the hidden word
3. **Visual Feedback**: Watch the hangman drawing progress with incorrect guesses
4. **Win/Loss Tracking**: Monitor your win streak across multiple games

![game_play](https://github.com/user-attachments/assets/cb274ec2-c44f-4cac-93e1-be426cf372ac)


### Input Validation
The game handles various input scenarios:
- **Length validation**: Only single characters accepted
- **Type validation**: Only alphabetic characters allowed
- **Duplicate prevention**: Tracks previously guessed letters
- **Range validation**: Word lengths must be within API limits


### Scoring System
- **Win Streak Tracking**: Consecutive victories counted
- **Performance Feedback**: Display of incorrect guess count
- **Session Persistence**: Streaks maintained across replays


## Future Plans (Coming soon)

- **Difficulty Modes**: Easy/Medium/Hard with different guess limits
- **Category Selection**: Words from specific topics (animals, countries, etc.)
- **Multiplayer Support**: Turn-based gameplay for multiple players
- **Score Persistence**: Save high scores and statistics to file
- **GUI Version**: Transition from console to graphical interface
- **Hint System**: Optional clues for challenging words

## Acknowledgments

- **Bro Code**: Original tutorial ([YouTube Channel](https://youtu.be/@BroCodez))
- **Random Word API Vercel**: External word service for dynamic content
