from flask import Flask, render_template, request, jsonify
from pathlib import Path

from shared import printMenys, utfoerMenyvalg, finn_alle_filer, all_files 
all_files

finn_alle_filer()

flattened_choicelist = [(index, ", ".join(value)) for index, value in enumerate(printMenys)]
#print(flattened_choicelist)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', choicelist=flattened_choicelist )

@app.route('/printmeny', methods=['POST'])
def push_data():
    data = request.get_json()
    if 'data' in data:
        selected_value = data['data']
        print(selected_value)
        # Do something med `selected_value`
        utfoerMenyvalg(selected_value)
        return jsonify({"message": f"Received value: {selected_value}"})
    else:
        return jsonify({"message": "No value found in request"}), 400
    
@app.route('/setting')
def settingS():
    return render_template('setting.html',  )

    
    


if __name__ == '__main__':
    app.run(debug=True)
