leistungen = {79: "Softgetränk", 123: "Buch", 234: "Kraftraum", 365: "Sauna"}
kunden = []
i = 0
j = 0
anzahl = 0
vorherigeID = 0
try:
    file = open("C:/Users/Marvin Hetzer/Documents/GitHub/Python/1. Program/Datei/verein.csv",mode="rt",encoding="utf-8")
    zeile = file.readline()
    splitZeile = zeile.split()
    kunden.append([])
    kunden[i][j].append(j + 1, splitZeile[2], leistungen[int(splitZeile[2])], splitZeile[4], splitZeile[3],
                        int(splitZeile[4]) * int(splitZeile[3]))
    vorherigeLeistungsID = splitZeile[2]
    while zeile != '':
        while zeile.split()[1] == vorherigeID and zeile != '':
            while zeile.split()[2] == vorherigeLeistungsID and zeile.split()[1] == vorherigeID and zeile != '':
                kunden[i][j][3] += splitZeile[4]
                splitZeile = file.readline().split()
            kunden[i][j].append(j + 1, splitZeile[2], leistungen[int(splitZeile[2])], splitZeile[4], splitZeile[3],
                                int(splitZeile[4]) * int(splitZeile[3]))
            j += 1
        i += 1
        j = 0
        kunden.append([])


    for kunde in kunden:
        for pos in kunde:
            print(pos)



except Exception as ex:
    print(ex)