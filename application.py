from flask import Flask, render_template
from pathlib import Path
import read_file_test 


var = read_file_test.printMeny()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
