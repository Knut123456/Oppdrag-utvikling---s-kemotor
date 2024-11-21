choicelist = [
    [ "Søkemontor "],
    [" leter etter ord                                 "],
    ["finn ord                                         "],
    [" finn ord                                        "],   
    [" lett etter linjer                               "],  
    ["Tell ord                                         "],
    ["settings                                         "],
    ["Avslutt                                          "]
] 

    


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
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N  ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsoek) 

