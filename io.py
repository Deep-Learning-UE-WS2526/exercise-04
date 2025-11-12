#Datei lesen
fh = open ("wiki.txt", mode='r', encoding="utf-8")
lines = fh.readlines()
fh.close()

#whitespaces entfernen damit die Filter Prüfung korrekt funktioniert
lines = [s.strip() for s in lines] #s für ein Satz in Liste lines
    
#Sätze filtern
# 1) Sätze mit weniger als 30 Zeichen (file short.txt)
short = [s for s in lines if len(s)<30]
# 2) Sätze die mit Der/Die/Das anfangen
articles = [s for s in lines if s.startswith(("Der","Die","Das"))]
# 3) Sätze die "April" enthalten
april = [s for s in lines if "April" in s]

#Output files schreiben
with open("short.txt", mode='w', encoding="utf-8") as file:
    for s in short:
        file.write(s)
        
with open("articles.txt", mode='w', encoding="utf-8") as file:
    for s in articles:
        file.write(s)
        
with open("april.txt", mode='w', encoding="utf-8") as file:
    for s in april:
        file.write(s)