import os
import json 

import sqlite3

conn = sqlite3.connect("telefonkatolog.db")

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS personer (
               fornavn TEXT,
               etternavn TEXT,
               telefonnummer TEXT
               )""")

conn.commit()


telefonkatalog = [] #listeformat ["fornavn", "etternavn" , "telephonnummer"]

def visallePersonar():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("det er ingen registerte personer i katalogen")
        input ("Trykk en tast for å gå tilbake til meny: ")
        printMeny()
    else:
        print ("************************************"
               "************************************")
        for personer in resultater:
            print ("* Fornavn : {:15s} Etternavn: {:15s} Telefonnummer: {:8s} *"
                   .format (personer[0], personer[1], personer[2]))
            print ("************************************"
                   "************************************")
        
        input ("Trykk en tast for å gå tilbake til meny: ")
        printMeny()

def legg_til_person_i_db(fornavn, etternavn, telefonnummer):
    cursor.execute("INSERT INTO personer (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)", 
                   (fornavn, etternavn, telefonnummer))
    conn.commit()


def slett_person_fra_db(fornavn, etternavn, telefonnummer):
    cursor.execute("DELETE FROM personer WHERE fornavn=? AND etternavn=? AND telefonnummer=?", 
                   (fornavn, etternavn, telefonnummer))
    conn.commit()

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
            exit()
    else:
        nyttforsoek = input ("Ulydig valg. velg en tall mellom 1-5: ")
        utfoermenyvalg (nyttforsoek)

def registrerPerson():
    fornavn = input ("skriv inn fornavn: ")
    etternavn = input ("skriv inn etternavn: ")
    telefonnummer = input ("skriv inn telefonnummer: ")
    
    legg_til_person_i_db(fornavn, etternavn, telefonnummer)
    
    print ("{0} {1} er registert med telefonnummer {2}"
           .format (fornavn, etternavn, telefonnummer))
    input ("Trykk en tast for å gå tilbake til meny: ")
    printMeny()





def sokPerson ():
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

    if typesok == "fornavn":
        cursor.execute("SELECT * FROM personer WHERE fornavn=?", (sokeTekst,))
    elif typesok == "etternavn":
        cursor.execute("SELECT * FROM personer WHERE etternavn=?", (sokeTekst,))
    elif typesok == "telefonnummer":
        cursor.execute("SELECT * FROM personer WHERE telefonnummer=? ", (sokeTekst,))

    resultater = cursor.fetchall()
    
    if not resultater:
        print("finner ingen personer")
        input ("Trykk en tast for å gå tilbake til meny: ")
        sokPerson()
    else:
        for personer in resultater:
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
    fornavn = input("skriv inn fornavn til person du vil slette: ")
    etternavn = input ("skriv inn etternavn til person du vil slette: ")
    telefonnummer = input ("skriv inn telefonnummer til person du vil slette: ")

    slett = input ("Vil du slette oppføringen J/N: ")
    if slett == "J" or "j":
        
        slett_person_fra_db(fornavn, etternavn, telefonnummer)
        print(f"{fornavn} {etternavn} er slettet fra katalogen")

    if slett == "N" or "n":
        Innstilinger ()
    else:
        slett = input ("Ulydig valg. velg en tall mellom J-N: ")
        slette_oppføring (slett)

def endre_oppfølging():
    print (telefonkatalog)

      

        



printMeny() # starter programmet ved å skrive menyen for første gang