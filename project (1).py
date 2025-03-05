import random
import os
from flask import Flask, render_template, request, session, jsonify, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

def load_word_list():
    """Load valid 5-letter words from file or use fallback list."""
    try:
        with open("words.txt", "r") as file:
            words = [line.strip().upper() for line in file if len(line.strip()) == 5 and line.strip().isalpha()]
            return words if words else raise_error()
    except (FileNotFoundError, IOError):
        return ["ABOUT", "ABOVE", "ACUTE", "ADEPT", "APPLE", "BEACH", "CLOUD", "DANCE", 
                "EARTH", "FLAME", "GREAT", "HOUSE", "PIANO", "QUEEN", "ROBOT", "SNAKE", 
                "TIGER", "WATER", "ZEBRA", "YOUTH"]

def evaluate_guess(guess, target):
    """Evaluate a guess against the target word."""
    guess, target = guess.upper(), target.upper()
    result = ["absent"] * 5
    guess_list, target_list = list(guess), list(target)
    
    # First pass: mark correct letters
    for i in range(5):
        if guess_list[i] == target_list[i]:
            result[i], target_list[i], guess_list[i] = "correct", "-", "+"
    
    # Second pass: mark present letters
    for i in range(5):
        if guess_list[i] != "+" and guess_list[i] in target_list:
            result[i], target_list[target_list.index(guess_list[i])] = "present", "-"
    
    return result

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/game')
def game():
    """Render the game page and initialize game state."""
    if 'target_word' not in session:
        word_list = load_word_list()
        session['target_word'] = random.choice(word_list).upper()
        session['guesses'] = []
        session['game_over'] = False
    return render_template('game.html')

@app.route('/guess', methods=['POST'])
def handle_guess():
    """Process a player's guess."""
    guess = request.json.get('guess', '').upper()
    word_list = load_word_list()
    
    if len(guess) != 5 or not guess.isalpha() or guess not in (w.upper() for w in word_list):
        return jsonify({'error': 'Invalid guess. Must be a 5-letter word from the word list.', 'valid': False})
    
    target_word = session['target_word']
    result = evaluate_guess(guess, target_word)
    session['guesses'] = session.get('guesses', []) + [{'word': guess, 'result': result}]
    
    is_win = guess == target_word
    is_game_over = is_win or len(session['guesses']) >= 6
    session['game_over'] = is_game_over
    
    return jsonify({
        'valid': True, 'guess': guess, 'result': result, 'is_win': is_win,
        'is_game_over': is_game_over, 'attempts_left': 6 - len(session['guesses']),
        'target_word': target_word if is_game_over else None
    })

@app.route('/reset', methods=['POST'])
def reset_game():
    """Reset the game state."""
    force_reset = request.args.get('force', 'false') == 'true'
    guesses = session.get('guesses', [])
    game_over = session.get('game_over', False)
    
    # Check if there's an unfinished game and this isn't a forced reset
    if len(guesses) > 0 and not game_over and not force_reset:
        return jsonify({'status': 'Game in progress', 'in_progress': True, 'guesses': len(guesses)})
    
    session.clear()
    word_list = load_word_list()
    session['target_word'] = random.choice(word_list).upper()
    session['guesses'] = []
    session['game_over'] = False
    
    return jsonify({'status': 'Game reset', 'in_progress': False})

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/settings')
def settings_page():
    return render_template('setting.html')

if __name__ == '__main__':
    app.run(debug=True)