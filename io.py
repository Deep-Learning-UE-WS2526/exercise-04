with open("wiki.txt", encoding='utf-8') as f:
    wikiList = []
    for line in f:
        wikiList.append(line)
    shortList = [x for x in wikiList if len(x) < 30]
    articleList = [x for x in wikiList if x.startswith(("Der", "Die", "Das")) ]
    aprilList = [x for x in wikiList if "April" in x]
    with open("short.txt", "w", encoding="utf-8") as shortFile:
        shortFile.writelines(shortList)
    with open("articles.txt", "w", encoding="utf-8") as artFile:
        artFile.writelines(articleList)
    with open("april.txt", "w", encoding="utf-8") as aprFile:
        aprFile.writelines(aprilList)