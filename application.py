from flask import Flask, render_template
from pathlib import Path
import read_file_test
from read_file_test import choicelist

choicelist
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',choicelist=choicelist )

if __name__ == '__main__':
    app.run(debug=True)
