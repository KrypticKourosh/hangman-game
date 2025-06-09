# Hangman Game

A feature-rich console-based Hangman game built in Python. This project started as a basic implementation inspired by the youtuber [Bro Code](https://www.youtube.com/@BroCodez) but was significantly enhanced with API integration, advanced game mechanics, and improved user experience.

## Project Origin

This project was inspired by the foundational Hangman game by [this tutorial](https://youtu.be/ag8NtD1e0Kc?si=7kKuYNJNSuO9LDAM). While the tutorial provided the core game logic, this implementation adds substantial enhancements including dynamic word fetching, session management, and comprehensive error handling.

## Features

### Core Gameplay
- **Classic Hangman mechanics** with visual ASCII art progression
- **Configurable word length** (3-9 characters) for difficulty control
- **Input validation** with comprehensive error checking
- **Visual feedback** with progressive hangman drawing

### Enhanced Features (Beyond Tutorial)
- **Dynamic Word Fetching**: Integrates with Random Word API for unlimited vocabulary
- **Win Streak Tracking**: Persistent scoring system across game sessions
- **Session Management**: Complete game loop with replay functionality
- **Network Error Handling**: Robust API integration with fallback mechanisms
- **Enhanced User Interface**: Console clearing and improved visual presentation
- **Custom Exception Handling**: Specialized error classes for better user experience

## Technical Implementation

### API Integration
- Fetches random words from `random-word-api.vercel.app`
- Implements proper HTTP error handling and connection management
- Graceful degradation when network issues occur

### Game Architecture
- **Modular Design**: Separated game logic from main execution flow
- **State Management**: Tracks game progress, guesses, and win streaks
- **Input Validation**: Multi-layer checking for user inputs
- **Error Recovery**: Handles invalid inputs without crashing

### Key Algorithms
- **Word Matching**: Efficient character matching and hint updating
- **Game State Evaluation**: Win/loss condition checking
- **Input Processing**: Comprehensive validation with user-friendly error messages

## Installation & Setup

### Requirement
```bash
pip install requests
```

### Running the Game
```bash
python main.py
```

## Usage

### Game Flow
1. **Word Length Selection**: Choose difficulty by selecting word length (3-9 characters)
2. **Letter Guessing**: Enter single letters to guess the hidden word
3. **Visual Feedback**: Watch the hangman drawing progress with incorrect guesses
4. **Win/Loss Tracking**: Monitor your win streak across multiple games

### Input Validation
The game handles various input scenarios:
- **Length validation**: Only single characters accepted
- **Type validation**: Only alphabetic characters allowed
- **Duplicate prevention**: Tracks previously guessed letters
- **Range validation**: Word lengths must be within API limits

## Code Structure

```
hangman_game/
├── hangman.py          # Core game engine and logic
├── main.py            # Main execution loop and session management
└── README.md          # Project documentation
```

### Key Functions

**hangman.py**
- `play_hangman()`: Main game loop and state management
- `fetch_random_word()`: API integration for dynamic word retrieval
- `display_art()`: ASCII art rendering system
- `check_guess()`: Comprehensive input validation
- `update_hint()`: Word reveal logic

**main.py**
- `main()`: Session management and win streak tracking
- Game loop with replay functionality

## Game Mechanics

### Difficulty Scaling
- **Word Length**: Longer words increase challenge
- **Guess Limit**: Maximum 9 incorrect guesses
- **Progressive Visualization**: Hangman drawing provides visual feedback

### Scoring System
- **Win Streak Tracking**: Consecutive victories counted
- **Performance Feedback**: Display of incorrect guess count
- **Session Persistence**: Streaks maintained across replays

## Error Handling

### Network Resilience
- HTTP error detection and reporting
- Connection timeout management
- Graceful application termination on critical failures

### Input Robustness
- Custom exception classes for specific error types
- User-friendly error messages with retry prompts
- Input sanitization and validation

## Future Enhancement Possibilities

- **Difficulty Modes**: Easy/Medium/Hard with different guess limits
- **Category Selection**: Words from specific topics (animals, countries, etc.)
- **Multiplayer Support**: Turn-based gameplay for multiple players
- **Score Persistence**: Save high scores and statistics to file
- **GUI Version**: Transition from console to graphical interface
- **Hint System**: Optional clues for challenging words

## Dependencies

- **requests**: HTTP library for API communication
- **Python 3.x**: Standard library functions (os, time)

## Learning Outcomes

This project demonstrates:
- **API Integration**: Working with external web services
- **Error Handling**: Robust application behavior under various conditions
- **Game Development**: State management and user interaction design
- **Code Organization**: Modular programming and separation of concerns
- **User Experience**: Thoughtful interface design and feedback systems

## Acknowledgments

- **Bro Code**: Original tutorial foundation ([YouTube Link](https://youtu.be/ag8NtD1e0Kc?si=7kKuYNJNSuO9LDAM))
- **Random Word API**: External word service for dynamic content
