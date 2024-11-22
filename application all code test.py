from flask import Flask, render_template, request, jsonify


import os




def videre():
    videre = input("vil du gå videre til menyen: J eller N: ")

    if videre.lower()=="j":
        printMeny()

    elif videre.lower()=="n":
        avslutt = input("vil du avslutte: J eller N: ")
        
        if avslutt.lower()=="j":
            exit()

        elif avslutt.lower()=="n":
            printMeny()
    else: 
       videre()
def videre_settings():
    videre = input("vil du gå videre til menyen: J eller N: ")

    if videre.lower()=="j":
        setting()

    elif videre.lower()=="n":
        avslutt = input("vil du avslutte: J eller N: ")
        
        if avslutt.lower()=="j":
            exit()

        elif avslutt.lower()=="n":
            setting()
    else: 
       videre_settings()

all_files =[]
filepaths = ["tekstfiles"]
def finn_alle_filer(filepath):
    if os.path.exists(filepath):
        print("file exits")  
        with os.scandir(filepath) as files:
            for file in files:
                all_files.append(file.path)
                
    if os.path.exists(filepath) == False:
        print("file does not exist")
    if len(all_files) == 0:
        print("No files found in this directory")
    if len(all_files) > 0:
        print(all_files)            
filepath ="tekstfiles"
finn_alle_filer(filepath)   


def les_av_filene_og_skriv_det_ned(list_file):
    for file in all_files:
        
        new_list_strip = []
        with open (file, "r") as f:
            for line in f: 
                #print(line)
                line_strip = line.strip()
                #print(line_strip)
                new_list_strip.append(line_strip)
            f.close()
        #print(new_list_strip)
        formatted_text = "\n".join(new_list_strip)
        #if file == [0]:
        #print(formatted_text)
        
        list_file.append(new_list_strip)
        
        #print (content)
printMenys = [
    [ "Søkemontor "],
    [" leter etter ord                                 "],
    ["finn ord                                         "],
    [" finn ord                                        "],   
    [" lett etter linjer                               "],  
    ["Tell ord                                         "],
    ["settings                                         "],
    ["Avslutt                                          "]
] 

settings  = [
"------------------- Innstillinger -------------------"
" 1. Vis alle filer                                "
" 2. Endre filsti                                  "
" 3. Ta med noen filer                             "
" 4. slett noen filer                              "
" 5. gå tilbake til menyen                         " 
" 6. Avslutt                                       "
]
def printMeny():
    index()

def setting():
    settingS()

def settingmeny(valg):
    if valg == "1":
        for index, value in enumerate (all_files):
                print("{0}, {1}".format(index, value))
        videre_settings()

    if valg == "2":
        filepath = input("skriv inn fillsti eller gå tilbake med n: ")
        if filepath.lower() == "n":
            setting()
        else:
            all_files.clear()
            finn_alle_filer(filepath)

    elif valg == "3":
        filepath = input("vil du gå inn og velge hvilken fil eller gå tilbake med n: ")
        if filepath.lower() == "n":
            setting()
        else:
            for index, value in enumerate (all_files):
                print("{0}, {1}".format(index, value))
            filer_som_vil_beholde= input("hvilken vil du beholde ved nummer: ")
            for index, value in enumerate (all_files):
                if index == int(filer_som_vil_beholde):
                    all_files.remove(value)
            videre_settings()

    elif valg == "4":
        filepath = input("vil du gå inn og velge hvilken fil eller gå tilbake med n: ")
        if filepath.lower() == "n":
            setting()
        else:
            for index, value in enumerate (all_files):
                print("{0}, {1}".format(index, value))
            filer_som_vil_slette= input("hvilken vil du slette ved nummer: ")
            for index, value in enumerate (all_files):
                if index == int(filer_som_vil_slette):
                    all_files.remove(value)
            videre_settings()
            
    elif valg == "5":
        printMeny()
    elif valg == "6":
        exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        settingmeny(nyttForsoek)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "0":
         print("1 fungere")
    elif valgtTall == "1":
         print("2 fungere") 
    elif valgtTall == "2":
        print("3 fungere")
    elif valgtTall == "3":
       print("4 fungere")
    elif valgtTall == "4":
        print("5 fungere")
    elif valgtTall == "5":
        print("5 fungere")
    elif valgtTall == "6":
        print("5 fungere")
    elif valgtTall == "7":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N  ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsoek) 


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
