import rarfile

base = 'UnderThe'
words = []

with open('c_words.txt') as input_file:
    for line in input_file:
        words.append(line[:-1])

rf = rarfile.RarFile('program.rar')

for i in words:
    attempt = base + i.capitalize()
    for f in rf.infolist():
        with rf.open(f.filename, mode='r', psw=attempt) as input_file:
            for ln in input_file:
                print(ln)

    # print(password)
