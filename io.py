def openAndRead (filename):
    fo = open(filename, "r", encoding="utf-8")
    content = fo.readlines()
    fo.close()
    return content

def openAndWrite(filename, content):
    fo = open(filename, "w", encoding="utf-8")
    fo.writelines(content)
    fo.close()
    return True

def main():
    
    # Read wiki.txt
    try :
        wiki = openAndRead("wiki.txt")
    except OSError as err:
        print ("File " + err.filename + " does not exist.")

    short, articles, april = [], [], []
    
    # Step 3.1
    short = [l for l in wiki if len(l) < 30]
    # Step 3.2
    articles = [l for l in wiki if l.startswith(("Der", "Die", "Das"))]
    # Step 3.3
    april = [l for l in wiki if "April" in l]
     
    # Write txts
    try:
        openAndWrite("short.txt", short)
        openAndWrite("articles.txt", articles)
        openAndWrite("april.txt", april)  
    except OSError as err:
        print ("File " + err.filename + " does not exist.")
    
if __name__ == "__main__":
    main()