# def read_wiki_file():
#     with open('wiki.txt', 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     return [line.strip() for line in lines]

# # Usage
# wiki_lines = read_wiki_file()



reader = open('wiki.txt', 'r', encoding='utf-8')

writer1 = open('short.txt', 'w', encoding='utf-8')
for line in reader:
    if len(line) < 30:
        writer1.write(line)
writer1.close()
reader.seek(0)

writer2 = open('articles.txt', 'w', encoding='utf-8')
for line in reader:
    if line.startswith(('Der', 'Die', 'Das')):
        writer2.write(line)
writer2.close()
reader.seek(0)

writer3 = open('April.txt', 'w', encoding='utf-8')
for line in reader:
    if 'April' in line:
        writer3.write(line)
writer3.close()

reader.close()