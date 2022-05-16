from flask import Flask, render_template, request
from textblob import Word
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', output=None)

@app.route("/predict", methods=['POST'])
def predict():
    words = str(request.form.get('word'))
    print(words)
    final_words = Word(words)
    meaning = final_words.definitions
    print(meaning)
    print(type(meaning))
    return render_template('home.html', output=meaning,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

