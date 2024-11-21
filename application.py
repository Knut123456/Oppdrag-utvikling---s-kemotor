from flask import Flask, render_template, request
from pathlib import Path
import read_file_test
from read_file_test import choicelist, utfoerMenyvalg



flattened_choicelist = [(index, ", ".join(value)) for index, value in enumerate(choicelist)]
print(flattened_choicelist)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', choicelist=flattened_choicelist )

@app.route('/push_data', methods=['POST'])
def push_data():
    variable_value = request.form['value']
    print(f"Received variable: {variable_value}")
    #return f"Received variable: {variable_value}"
    result = utfoerMenyvalg(variable_value)
    
    return result 


if __name__ == '__main__':
    app.run(debug=True)
