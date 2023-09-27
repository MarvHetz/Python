hours = int(input('Anfagsstunden: '))
minutes = int(input('Anfangsminuten: '))
duration = int(input('Laufzeit: '))

minutes += duration

hours += int(minutes / 60)
hours %= int(24)
minutes %= int(60)

print(hours, ' : ', minutes)