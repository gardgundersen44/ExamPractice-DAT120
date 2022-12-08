
import numpy as np

id_maalepunkt = []
navn_maalepunkt = []
dato = []
antall_passeringer = []

def sum_passeringerer(list):
    sum = 0
    for i in list:
        sum += i
    return sum

with open("sykkelplasseringer.txt", encoding="UTF-8") as file:
    for indeks in file:
        data = indeks.strip().split(";")

        id_maalepunkt.append(data[0])
        navn_maalepunkt.append(data[1])
        dato.append(data[2])
        antall_passeringer.append(int(data[3]))

print(f"Total antall passeringer: {sum_passeringerer(antall_passeringer)}")

navn_maalepunkt_input = input("Oppgi navn på målepunkt: ")

counter = 0
for i in navn_maalepunkt:
    if i == navn_maalepunkt_input:
        print(f"Antall passeringer på {navn_maalepunkt_input}: {antall_passeringer[counter]}")
    counter += 1










