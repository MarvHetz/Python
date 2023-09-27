def readFile(file):
    try:
        stream = open(r"C:/Users/Marvin Hetzer/Documents/GitHub/Python/1. Program/Datei/"+file+".txt",mode="rt",encoding="utf-8")
        print(stream.read())
        stream.close()
    except:
        print("Datei kann nicht geöffnet werden")

file = input("Welche Datei: ")
readFile(file)