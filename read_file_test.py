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




list_files = []
les_av_filene_og_skriv_det_ned(list_files)

#print(list_files[0])


#ord = input("hvilket ord vil du ha: ")
def printOrd(ord):
    #find_word = False
    #word = ord.find()
    file_number = -1
    for file in list_files:
        file_number += 1
        line_number = 0
        for line in file:
            line_number += 1
            #print(line)
            if ord in line:
                #print(file_name)
                file_name = all_files[file_number]
                #print(file_name)
                print("fant ordet {0} i fil {2} på linje {1}". format(ord, line_number, file_name))

    if ord not in line:
        print("ordet " + ord + " ble ikke funnet")

    videre()      

     
def finnord_func(finnord):
    for file in list_files:
        for line in file:
            if finnord in line:
               fant = True
    if fant == True:
        print("fant ordet {0}".format(finnord))     

    if fant == False:
        print("ordet {0} ble ikke funnet".format(finnord))

    videre()
                              



 
def find_line_func(find_line):
    number = 0 #to keep track of the number of find is shown
    file_number = 0 #to keep track of the file is in
    line_number = 0 #to keep track of the line is in
    for file in list_files:
        file_number += 1
        line_number = 0
        for line in file:
            line_number += 1
            if find_line in line:
                file_name = all_files[file_number]
                print("in file {0} line {1} and the text is {2}". format(file_name, line_number, line)) 
                number += 1
                
                            
    print("fant jeg {} mange ganger".format(number))

    videre()     

def finn_number(find_number):
    number = 0 #to keep track of the number of find is shown
    for file in list_files:
        for line in file:
            if find_number in line:
                number += 1
                
                            
    print("fant jeg {} mange ganger".format(number))

    videre()      



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

def setting():
    print("------------------- Innstillinger -------------------")
    print("| 1. Vis alle filer                                 |")
    print("| 2. Endre filsti                                   |")
    print("| 3. Ta med noen filer                              |")
    print("| 4. slett noen filer                               |")
    print("| 5. gå tilbake til menyen                          |")
    print("| 6. Avslutt                                        |")
    print("-----------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    settingmeny(menyvalg)
    
    

        

def printMeny():
    choice_list = [
        ("------------------- Telefonkatalog -------------------"),
        "| 1. leter etter ord                                 |",
        "| 2. finn ord                                        |",
        "| 3. lett etter linjer                               |",
        "| 4. Tell ord                                        |",
        "| 5. settings                                        |",
        "| 6. Avslutt                                         |",
        "------------------------------------------------------"
    ]
    for line in choice_list:
        print(line)
    if False:
        print("------------------- Telefonkatalog -------------------")
        print("| 1. leter etter ord                                 |")
        print("| 2. finn ord                                        |")
        print("| 3. lett etter linjer                               |")
        print("| 4. Tell ord                                        |")
        print("| 5. settings                                        |")
        print("| 6. Avslutt                                         |")
        print("------------------------------------------------------") 

    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        ord = input("hvilke ord vil du finne: ")
        printOrd(ord)
    elif valgtTall == "2":
        finnord = input("hvilket ord vil du finne: ")  
        finnord_func(finnord)  
    elif valgtTall == "3":
        find_line = input("hvilket linje vil du finne: ")  
        find_line_func(find_line)
    elif valgtTall == "4":
        find_number = input("hvilket ord vil du telle: ") 
        finn_number(find_number)
    elif valgtTall == "5":
        setting()   
    elif valgtTall == "6":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N  ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsoek)

printMeny()

