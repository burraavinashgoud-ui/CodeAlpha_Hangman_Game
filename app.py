from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Example game state or route handler
@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    letter = data.get('letter')
    
    # TODO: Add your game logic here (check if letter is in word, update attempts, etc.)
    
    # Ensure you return JSON, NOT render_template()
    return jsonify({
        'word_display': _get_current_word_display(),
        'attempts_left': attempts_left,
        'guessed_letters': list(guessed_letters),
        'game_over': game_over,
        'won': won
    })
