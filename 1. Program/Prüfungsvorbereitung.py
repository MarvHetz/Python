kinosaal = [[True, True, True, False, True, True, False, False, False, False, True, False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, True, True, True, False], [True, True, True, False, True, True, True, True, True, False, True, False, True, True, False, False, False, True, True, True, True, True, True, False, True, False, True, True, True, False], [True, False, False, False, False, True, False, True, True, False, True, False, True, True, False, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False], [True, True, True, True, False, True, False, True, True, False, True, False, False, False, False, True, True, True, True, False, True, False, True, True, True, False, False, False, True, False], [True, True, True, False, False, True, False, True, True, True, True, True, False, False, True, True, True, True, False, False, True, False, True, True, True, True, False, False, True, False], [True, False, False, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, False, False, True, False, False, False, True, True, True, True, True, False], [True, False, False, False, True, True, True, False, False, True, True, True, True, True, True, True, False, False, False, True, True, True, False, False, True, True, True, True, True, False]]

def freieSitze(anzahlSitze):
    for i in range(0,len(kinosaal)):
        for j in range(0, len(kinosaal[i])):
            count = 0
            k = 0
            while k in range(0, anzahlSitze) and j+k < len(kinosaal[i]) and count < anzahlSitze:
                if(kinosaal[i][j + k] is True):
                    count += 1
                else:
                    break
                k += 1
            if(count == anzahlSitze):
                return (i + 1) * 100 + j + 1
    return 0

ersterPlatz = freieSitze(int(input("Anzahl der Sitze: ")))

print(ersterPlatz)

if ersterPlatz != 0:
    print("Der erste Sitz ist: ",ersterPlatz)
else:
    print("Kein Platz verfügbar!")