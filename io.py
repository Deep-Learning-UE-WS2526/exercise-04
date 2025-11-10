import json

def reader(filename):

    with open(filename, "r", encoding="utf-8") as file:
        l = file.readlines()
    
    lineDictonary = {}
    a = 0

    for lines in l:
        lineDictonary[a] = lines
        a = a + 1
    return lineDictonary

with open('exercise-04/0_file.txt', 'w', encoding="utf-8") as file:
     file.write(json.dumps(reader('exercise-04/wiki.txt'), ensure_ascii=False, indent=2)) 





def linecounter(filename_lineCounter):
    lineList_lineCounter = reader(filename_lineCounter)

    shortlines = {}

    for key, value in lineList_lineCounter.items():
        line_length = len(value)
        if line_length < 30:
            shortlines[key] = value

    return shortlines

with open('exercise-04/1_short.txt', 'w', encoding="utf-8") as file:
     file.write(json.dumps(linecounter('exercise-04/wiki.txt'), ensure_ascii=False, indent=2)) 



def articleSeperate(filename_articleSeperate):
    lineList_articleSeperate = reader(filename_articleSeperate)

    articleLines = {}

    for key, value in lineList_articleSeperate.items():
        words_articleSeperate = value.split()
        if words_articleSeperate[0] == "Der" or words_articleSeperate[0] == "Die" or words_articleSeperate[0] == "Das":
            articleLines[key] = value

    return articleLines


with open('exercise-04/2_article.txt', 'w', encoding="utf-8") as file:
     file.write(json.dumps(articleSeperate('exercise-04/wiki.txt'), ensure_ascii=False, indent=2)) 



def seperateByWord(filename_seperateByWord):
    lineList_seperateByWord = reader(filename_seperateByWord)
    
    aprilLines = {}

    for key, value in lineList_seperateByWord.items():
        if "April"  in value:
            aprilLines[key] = value

    return aprilLines


with open('exercise-04/3_april.txt', 'w', encoding="utf-8") as file:
     file.write(json.dumps(seperateByWord('exercise-04/wiki.txt'), ensure_ascii=False, indent=2)) 

    












