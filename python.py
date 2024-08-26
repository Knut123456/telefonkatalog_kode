telefonkatalog = [] #listeformat ["fornavn", "etternavn" , "telephonnummer"]

def printMeny ():
    print ("---------------------- Telefonkatalog ----------------------")
    print (" 1. legg til en ny person")
    print (" 2. Søk opp person eller telefonnummer")
    print (" 3. vis alle personer")
menyvalg = input ("skriv inn tall for å velge fra menyen")
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
        bekreftelse = input ("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse =="j" or bekreftelse =="j"): # skjekker bare fo ja
            exit()
    else:
        nyttforsoek = input ("Ulydig valg. velg en tall mellom 1-4 ")
        utfoermenyvalg (nyttforsoek)

def registrerPerson():
    fornavn = input ("skriv inn fornavn: ")
    etternavn = input ("skriv inn etternavn: ")
    telefonnummer = input ("skriv inn telefonnummer: ")

    nyRegristering = [fornavn, etternavn, telefonnummer]
    telefonkatalog.append(nyRegristering)

    print ("{0} {1} er registert med telefonnummer {2}"
           .format (fornavn, etternavn, telefonnummer))
    input ("Trykk en tast for å gå tilbake til meny")
    printMeny()

def visallePersonar():
    if not telefonkatalog:
        print("det er ingen registerte personer i katalogen")
        input ("Trykk en tast for å gå tilbake til meny")
        printMeny()
    else:
        print

