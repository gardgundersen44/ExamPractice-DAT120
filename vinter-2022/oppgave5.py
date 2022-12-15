from datetime import datetime

# Leser fil, sorterer informasjon
navn= []
stasjon = []
tid = []
middeltemperatur = []
nedboer = []

ny_fil = open("vaer_stasjoner.txt", "w")
ny_fil.write("Stasjon;Total nedboer; Hoeyeste middeltemperatur; Respektiv dato; Lavest middeltemperatur; Respektiv dato")
def analyse_stasjon(gitt_fil):
    with open(gitt_fil, encoding="UTF-8") as fil:
        next(fil)
        for x in fil:
            # Lagrer all relevant data fra fil til respektive lister
            data = x.strip().split(";")
            try:
                navn.append(data[0].replace("å", "aa"))
                stasjon.append(data[1])
                tid.append(datetime.strptime(data[2], "%d.%m.%Y").strftime("%d.%m.%Y"))
                middeltemperatur.append(float(data[3].replace(',', '.')))
                nedboer.append(float(data[4].replace(',', '.')))
            except ValueError:
                continue

    sum = finn_sum()
    temp = temperatur_informasjon()
    navn_stasjon = navn[1]


    ny_fil.write("\n"+navn_stasjon+";"+str(sum)+";"+str(temp[0])+";"+str(temp[1])+";"+str(temp[2])+";"+str(temp[3]))
    ny_fil.close()

# Printer ut total nedbør
def finn_sum():
    sum_nedboer = 0
    for i in nedboer:
        sum_nedboer += i
    return round(sum_nedboer, 3)

# Finner lavest og høyest middeltemperatur
def temperatur_informasjon():
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

    return hoyest_temp, tid[indeks_hoyest], lavest_temp, tid[indeks_lavest]

# Søk etter en værstasjon ved hjelp av kode for værstasjon
def sok_etter_stasjon():
    kode = input("\nOppgi kode til værstasjon: ")
    for k in stasjon:
        if k == kode:
            index = stasjon.index(k)
            print(f"Fant værstasjon med navn: {navn[index]}, og kode: {k}, på linje {index} i filen!" )
    if kode not in stasjon:
        print("Fant ingen værstasjon på oppgitt kode i filen!")

if __name__ == "_ _main__":
    analyse_stasjon("vaer_data.txt")

