stream = open(r"C:/Users/Marvin Hetzer/Documents/GitHub/Python/1. Program/Datei/Namen.txt",mode="rt",encoding="utf-8")

teams = []
zeile = 0
j = 0
i = 0
teams.append([])

while zeile != '':
    if i >= 4:
        i = 0
        j += 1
        teams.append([])

    zeile = stream.readline()
    teams[j].append(zeile)
    i += 1

print('Es sind ',len(teams),' Teams')

for i in range(0,len(teams) - 1):
    print('Team',i+1,'ist:')
    j = 0
    while j < len(teams[i]):
        print(teams[i][j])
        j +=1