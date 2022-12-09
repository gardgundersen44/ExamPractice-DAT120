# Program som finner laveste, høyeste og gjennomsnittsverdi

verdi = 1
sum = 0
counter = 0
gjennomsnitt_verdi = 0

start_verdi = float(input("Oppgi et starttall: "))
minste_verdi = start_verdi
storste_verdi = start_verdi

while verdi > 0:
    verdi = float(input("Oppgi et tall, negativt tall eller 0 for å avslutte: "))


    # Sjekker om oppgitt verdi er positivt, hvis ikke avslutt
    if verdi <= 0:
        break

    # Finner høyest verdi
    if storste_verdi < verdi:
        storste_verdi = verdi

    # Finner lavest verdi
    if minste_verdi > verdi:
        minste_verdi = verdi

    counter += 1
    sum += verdi
    gjennomsnitt_verdi = sum/counter

print("\nMinste verdi: " + str(minste_verdi))
print("Største verdi: " + str(storste_verdi))
print("Gjennomsnittsverdi: " + str(gjennomsnitt_verdi))





