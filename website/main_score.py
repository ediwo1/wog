from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_score():
    # Reading the score from the file
    with open('../Scores.txt', 'r') as file:
        score = file.read().strip()  # Read and strip any newlines or spaces
    return render_template('score.html', score=score)

if __name__ == '__main__':
    app.run()