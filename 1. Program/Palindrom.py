def trim_String(string):
    string = string.lower()
    return string.replace(" ","")

def reverse_String(string):
    return string[::-1]

string = input("Geben Sie den Satz ein: ")
string = trim_String(string)

if(string == reverse_String(string)):
    print("Es ist ein Palindrom!")
else:
    print("Es ist kein Palindrom!")