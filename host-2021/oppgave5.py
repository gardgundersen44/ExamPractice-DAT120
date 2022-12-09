from datetime import *

id_maalepunkt = []
navn_maalepunkt = []
dato = []
antall_passeringer = []

def sum_passeringerer(list):
    sum = 0
    for i in list:
        sum += i
    return sum

with open("../sykkelplasseringer.txt", encoding="UTF-8") as file:
    for indeks in file:
        data = indeks.strip().split(";")

        id_maalepunkt.append(data[0])
        navn_maalepunkt.append(data[1])
        dato.append(datetime.strptime(data[2], "%Y-%m-%d"))
        antall_passeringer.append(int(data[3]))

print(f"Total antall passeringer: {sum_passeringerer(antall_passeringer)}")

# Finner antall passeringer basert på oppgitt navn (på målepunkt)
navn_maalepunkt_input = input("Oppgi navn på målepunkt: ")
counter = 0
a = 0
sum = 0
for i in navn_maalepunkt:
    if i == navn_maalepunkt_input:
        sum += antall_passeringer[counter]
    counter += 1

    if i != navn_maalepunkt_input:
        a += 1
        if a == len(navn_maalepunkt):
            print("Fant ingen målepunkt på oppgitt navn!")

# Finner antall passeringer basert på oppgitt dato
try:
    dato_maalepunkt_input = datetime.strptime(input("\nOppgi en dato (ÅÅÅÅ-MM-DD): "), "%Y-%m-%d")
    counter = 0
    for j in dato:
        if dato_maalepunkt_input.day == j.day and dato_maalepunkt_input.month == j.month and dato_maalepunkt_input.year == j.year:
            print(f"Antall passeringer på datoen {dato_maalepunkt_input} for målepunkt {navn_maalepunkt[counter]}: {antall_passeringer[counter]}")
    counter += 1
except ValueError:
    print("Feil format på dato!")









