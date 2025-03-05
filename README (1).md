# Wordle Clone using Python Flask

#### Video Demo: [www.youtube.com/watch?v=glu7gbvxh8l](https://www.youtube.com/watch?v=glu7gbvxh8l)

#### Description:

This is a Wordle game clone, created with the Flask framework for Python and other web technologies. It has a gaming feature that makes the player guess a hidden word consisting of 5 letters in six attempts and provides color-coded feedback for every guess to make the game easier to comprehend.

## Project Overview

Like the original Wordle game, this clone also possesses the core features, yet enhanced with additional functionalities as configurable options, determined UI elements, and responsive functionalities. This is an example of full-stack development where in Python is used to code the backend part and HTML, CSS and Javascript are used to code the frontend part.

## Files and Functionality

### `project.py`

This is the principal file for the Flask application. It does the following:

- Sets up the Flask app and manages sessions

- Sets up routes corresponding to the different pages of the app

- Contains the primary game logic that deals with:

  - `load_word_list()`: Loads 5-letter words from words.txt, or reverts to a backup list if the file is missing.

  - `select_target_word()`: Randomly picks a target word for every game.

  - `evaluate_guess()`: Checks a player's guess against the target word.

- Accepts guesses from the players through a JSON API.

- Keeps track of the game status (the number of guesses, whether the player has won or lost, etc.)

- Resets the game

The evaluation algorithm is particularly interesting because the handling of duplicate letters is done with two passes which makes it possible to mark correct letters to an appearing position first before marking where the letters are located elsewhere. 

### Templates

#### `base.html` and `layout.html`

These are the base template files that determines the application look and feel. 

- `base.html` is a skeletal template that has the basic structure.

- `layout.html` builds on this by providing a more complete layout that has menus, footer and other additional styles.

Both of them are styled with Tailwind CSS and use FontAwesome for the icons.

#### `index.html` 

A welcoming page for users with game rule explanations. It covers: 

- How to play details 

- Color coding description 

- Game instructions 

- Start button prominently visible 

#### `game.html` 

The core gameplay part containing guess works. Main elements include: 

- An animated letter tile game board surface that responds to actions 

- Letter input using an on-screen keyboard 

- Color coded tiles for feedback (green, yellow, gray) 

- Notifications displayed on a message area 

- Modal for displaying statistics at the end of the game 

- Game statistics stored in local storage for persistent access 

The JavaScript in this file takes care of: 

- Input on a real keyboard or the on-screen keyboard 

- What the game is doing at a particular time 

- Communication with the game server 

- Collection and display of statistics 

- Providing animations and feedback visually 

#### `help.html` 

An additional page that includes more advanced game instructions that cover: 

- Images illustrating letter coloring 

- Descriptions of the game’s mechanics  

- Tactics for the game’s players 

#### `setting.html` 

A page players go to to customize the game for their personal preferences: 

- Selection of words for the game (and their associated difficulty) 

- Colors used 

- Special aid provisions 

- Styles of notices 

Settings remain the same between sessions as they are retained in local storage.

### `test_project.py`

Houses unit tests for some of the game functions:

- For the `evaluate_guess()` function to test different possible guess evaluations.

- For the `load_word_list()` function to check if words load correctly.

- For the `select_target_word()` function to check if a random word set is selected.

The tests aim to verify the application logic of the game is correct for a variety of edge cases.

### `words.txt`

Has a collection of 5-letter words that may serve as target words or valid guesses. The file is formatted for one word a line, containing hundreds of commonly used English words.

### `requirements.txt`

Lists the necessary dependencies for running the application, which for now is only Flask 3.0.0.

## Design Decisions

### Game Logic in Python vs. JavaScript

For my implementation, I chose to write the game logic (including the selection of words and evaluation of guesses) in Python instead of JavaScript for the following reasons: 

- To block players from finding the target word through the browser dev tools
- To enable server-side checking of the guesses with a substantial list of words
- To ensure that there is a distinction between the game logic and the game presentation

### Session Management

The game implements session management using Flask sessions for the following purposes:  

- Keeping track of the current target word on the server
- Keeping track of the number of guesses for several queries
- Keeping track of the game state

Using these methods prevents cheating whilst making it possible to use the game when the page is refreshed.

### Responsive Design with Tailwind CSS

Responsive, visually appealing user interface has been developed using Tailwind CSS which:    

- Is suitable for both mobile and desktop devices.    

- Ensures styling is done with a minimum of custom CSS.   

- Enables rapid UI creation and effortless maintenance.    

### Local Storage for Statistics

Win/loss records and guess distribution for each player are stored in local storage instead of on the server to:    

- Decrease server load and manage complexity.    

- Safeguard user privacy.    

- Enable the game to operate without requiring user accounts.    

### Two-Pass Algorithm for Guess Evaluation

The algorithm for guess evaluation has a two-pass technique to:    

1. Mark letters in the correct position as correct in the first pass.    

2. Mark letters that belong to the word, but are in the wrong position in the second pass.    

This is useful to provide the player with accurate feedback when using words with repeating letters.

### Future Improvements

Possible enhancements for the future versions comprise of:

- Daily challenges with consolidated answers

- Cross-platform statistics through user accounts

- New game types (i.e. timed and difficulty)

- Results socially sharable 

- Broader Category or language word list integrations 

### Instructions to Execute

1. Check if Python 3.6+ is available on your operating system.

2. Download dependencies using `pip install flask`.

3. Execute the application via `python project.py`.

4. Launch the game on your web browser on the URL `http://localhost:5000`.

### Closing Remarks

This example of a Wordle clone implements a full client-server structure for a web application. It uses Python Flask as the backend service, modern frontend development practices, and game development techniques. The modular design of this project enables effortless upkeep and modification in the future.