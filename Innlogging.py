import hashlib # Importerer hashlib som er brukt for å kryprtere passord og annen informasjon


database = {  #Lager databasen med brukernavn og passord
    'Joost': hashlib.sha256('Joostepop'.encode()).hexdigest(), #Eksempel bruker med sha256 kryptering som gjør den om til en 32-bit string
    'Bjoorn': hashlib.sha256('Brukerstøtte'.encode()).hexdigest(),
    'Joakim': hashlib.sha256('Jogge'.encode()).hexdigest()
}

def sjekk_innlogging(brukernavn, passord): #Funksjon for å sjekke om brukernavn og passord er riktig
    if brukernavn in database: #Sjekker om brukernavnet finnes i databasen
        if hashlib.sha256(passord.encode()).hexdigest() == database[brukernavn]: #Sjekker om passorded stemmer med brukernavnet, og sjekker om passordet er likt det krypterte i databasen
            print("Du har nå logget inn!")
        else:
            print("Passordet er feil")
    else:
        print("Brukerenet finnes ikke")

def main(): #Funksjon for å kjøre programmet og be brukeren om å skrive inn brukernavn og passord, og for å se om det stemmer med sjekk_innloggign funksjonen
    brukernavn = input("Skriv inn brukernavn: ")
    passord = input("Skriv inn passord: ")
    sjekk_innlogging(brukernavn, passord) #Kjører sjekk_innlogging funksjonen I main()

if __name__ == "__main__":
    main() # Starter programmet
