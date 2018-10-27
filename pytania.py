dane=input('podaj prosze imię, nazwisko')
telefon=input('podaj numer telefonu')
print(dane.isalpha())
print(telefon.isdigit())
dane=dane.title()
telefon=telefon.replace('-','').replace(' ','')
print(telefon)
print("Imię kobiece:", dane.endswith("a"))
personal=dane+' '+telefon
print(personal)
print(len(personal))
letters = len(personal) - personal.count(" ") - 9
print(letters)
print (len(dane)) #sprawdzenie
