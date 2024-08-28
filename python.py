import os
import json 

fil ="telefondata.json"

def save_to_file ():
    with open (fil, "w") as file:
        json.dump(telefonkatalog, file)


def load_from_file():
    if os.path.exists(fil):  # Check if the file exists
        if os.path.getsize(fil) > 0:  # Check if the file is not empty
            with open(fil, "r") as file:
                try:
                    global telefonkatalog
                    telefonkatalog = json.load(file)  # Load JSON data into the list5
                    #print("Data loaded successfully from", fil)
                except json.JSONDecodeError:
                    print("Error: The file contains invalid JSON. Initializing an empty telefonkatalog.")
                    telefonkatalog = []
        else:
            print("The file is empty. Initializing an empty telefonkatalog.")
            telefonkatalog = []
    else:
        print(fil, "doesn't exist. Initializing an empty telefonkatalog.")
        telefonkatalog = []

        
def exit_programm():
    save_to_file()
    print("data saved. exiting...")
    exit()


telefonkatalog = [] #listeformat ["fornavn", "etternavn" , "telephonnummer"]

load_from_file()

#print(telefonkatalog,  "fungerer")

def printMeny ():
    print ("---------------------- Telefonkatalog ----------------------")
    print (" 1. legg til en ny person")
    print (" 2. Søk opp person eller telefonnummer")
    print (" 3. Vis alle personer")
    print (" 4. Innstilinger")
    print (" 5. Avslutt")
    menyvalg = input ("skriv inn tall for å velge fra menyen: ")
    utfoermenyvalg(menyvalg)


def utfoermenyvalg (valgtall):
    if valgtall == "1":
        registrerPerson()
    elif valgtall == "2":
        sokPerson()
        printMeny()
    elif valgtall == "3":
        visallePersonar()
    elif valgtall == "4":
        Innstilinger()
    elif valgtall == "5":
        bekreftelse = input ("Er du sikker på at du vil avslutte? J/N  ")
        if (bekreftelse =="j" or bekreftelse =="j"): # skjekker bare fo ja
          exit_programm()
    else:
        nyttforsoek = input ("Ulydig valg. velg en tall mellom 1-5: ")
        utfoermenyvalg (nyttforsoek)

def registrerPerson():
    fornavn = input ("skriv inn fornavn: ")
    etternavn = input ("skriv inn etternavn: ")
    telefonnummer = input ("skriv inn telefonnummer: ")

    nyRegristering = [fornavn, etternavn, telefonnummer]
    telefonkatalog.append(nyRegristering)
    save_to_file ()

    print ("{0} {1} er registert med telefonnummer {2}"
           .format (fornavn, etternavn, telefonnummer))
    input ("Trykk en tast for å gå tilbake til meny: ")
    printMeny()

def visallePersonar():
    load_from_file()
    if not telefonkatalog:
        print("det er ingen registerte personer i katalogen")
        input ("Trykk en tast for å gå tilbake til meny: ")
        printMeny()
    else:
        #print("test ", telefonkatalog)
        print ("************************************"
               "************************************")
        for personer in telefonkatalog:
            print ("* Fornavn : {:15s} Etternavn: {:15s} Telefonnummer: {:8s} *"
                   .format (personer[0], personer[1], personer[2]))
            print ("************************************"
                   "************************************")
        
        input ("Trykk en tast for å gå tilbake til meny: ")
        printMeny()

def sokPerson ():
    #load_from_file()
    if not telefonkatalog:
        print("det er ingen registerte personer i katalogen")
        printMeny()
    else:
        print ("1, søk på fornavn") 
        print ("2, søk på etternavn") 
        print ("3, søk på telefonnummer")
        print ("4, Tilbake til hovedmeny")
        sokefelt = input ("velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnperson ("fornavn", navn)
        elif sokefelt == "2":
            navn = input ("Etternavn: ")
            finnperson ("Etternavn", navn)
        elif sokefelt == "3":
            tlfnummer =input ("Telefonnummer: " )
            finnperson ("telefonnummer", tlfnummer)
        elif sokefelt == "4":
            printMeny()
        else:
            print ("ugyldig valg. Velg en tall mellom 1-4: ")
            sokPerson()

# typesok angir om man søker på fornavn, etternavn eller telefonnummer
def finnperson (typesok, sokeTekst):
    #load_from_file()
    svar =[]
    for personer in telefonkatalog:
        if typesok == "fornavn":
            if personer [0] == sokeTekst:
                svar.append(personer)
        elif typesok == "etternavn":
            if personer [1] == sokeTekst:
                svar.append(personer)
        elif typesok == "telefonnummer":
            if personer [2] == sokeTekst:
               svar.append(personer)
    
    if not svar:
        print("finner ingen personer")
        input ("Trykk en tast for å gå tilbake til meny: ")
        sokPerson()
    else:
        for personer in svar:
            print ("{0} {1} har telefonnnummer {2}"
                   .format(personer[0], personer [1], personer [2]))
                


def Innstilinger():
    print ("---------------------- Innstilinger ----------------------")
    print (" 1. slette oppføringen")
    print (" 2. endre oppfølging")
    print (" 3. Til hovedmenyen")
    Innstilingervalg = input ("skriv inn tall for å velge fra menyen: ")
    utfoerInnstilingervalg(Innstilingervalg)

def utfoerInnstilingervalg (valgtall):
    if valgtall == "1":
        slette_oppføring()
    elif valgtall == "2":
        endre_oppfølging()
    elif valgtall == "3":
        printMeny()
    else:
        nyttforsoek = input ("Ulydig valg. velg en tall mellom 1-3: ")
        utfoerInnstilingervalg (nyttforsoek)

def slette_oppføring():
    slett = input ("Vil du slette oppføringen J/N: ")
    if slett == "J" or "j":
        with open (fil, "w") as file:
            file.write("") # clear the info on the json file
    if slett == "N" or "n":
        Innstilinger ()
    else:
        slett = input ("Ulydig valg. velg en tall mellom J-N: ")
        slette_oppføring (slett)

def endre_oppfølging():
    print (telefonkatalog)

      

        



printMeny() # starter programmet ved å skrive menyen for første gang