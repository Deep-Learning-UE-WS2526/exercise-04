with open("C:/Users/maris/Documents/Uni/IV/KO Deep Learning/exercise-04/wiki.txt", "r", encoding="utf-8") as wiki:
    lines = wiki.readlines()

with open("short.txt", "w", encoding = "utf-8") as short:
    [short.write(line) for line in lines if len(line) < 30]

with open("articles.txt", "w", encoding = "utf-8") as articles:
    [articles.write(line) for line in lines if line.startswith(("Der", "Die", "Das"))]

with open("april.txt", "w", encoding = "utf-8") as april:
    [april.write(line) for line in lines if "April" in line]