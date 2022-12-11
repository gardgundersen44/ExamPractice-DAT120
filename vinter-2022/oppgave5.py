from datetime import datetime

# Leser fil, sorterer informasjon
navn= []
stasjon = []
tid = []
middeltemperatur = []
nedboer = []


with open("vaer_data.txt", encoding="UTF-8") as fil:

    for x in fil:
        # Lagrer all relevant data fra fil til respektive lister
        data = x.strip().split(";")
        try:
            navn.append(data[0])
            stasjon.append(data[1])
            tid.append(datetime.strptime(data[2], "%d.%m.%Y"))
            middeltemperatur.append(float(data[3].replace(',', '.')))
            nedboer.append(float(data[4].replace(',', '.')))
        except ValueError:
            continue


# Printer ut total nedbør
sum_nedboer = 0
for i in nedboer:
    sum_nedboer += i
print(f"Total nedbør: {sum_nedboer:1.2f}")

# Finner lavest og høyest middeltemperatur
hoyest_temp = 0
lavest_temp = 0
indeks_hoyest = 0
indeks_lavest = 0

for j in middeltemperatur:
    if hoyest_temp < j:
        hoyest_temp = j
        indeks_hoyest = middeltemperatur.index(j)

    if lavest_temp > j:
        lavest_temp = j
        indeks_lavest = middeltemperatur.index(j)
print(f"\nHøyest middeltemperatur: {hoyest_temp}, dato: {tid[indeks_hoyest]} \nLavest middeltemperatur: {lavest_temp}, dato: {tid[indeks_lavest]}")

# Søk etter en værstasjon ved hjelp av kode for værstasjon
kode = input("\nOppgi kode til værstasjon: ")

for k in stasjon:
    if k == kode:
        index = stasjon.index(k)
        print(f"Fant værstasjon med navn: {navn[index]}, og kode: {k}, på linje {index} i filen!" )

if kode not in stasjon:
    print("Fant ingen værstasjon på oppgitt kode i filen!")
