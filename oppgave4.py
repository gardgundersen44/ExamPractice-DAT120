# Lar brukeren velge størrelse på gangetabell, og printe respektiv gangetabell
storrelse = int(input("Oppgi størrelse: "))
print("Tabellstørrelse: " + str(storrelse))
print("\t", end="")

for tall in range(1, storrelse+1):
    print(tall, end=" ")
print("\n-----------------------------------")

for rad in range(1, storrelse+1):
    print(rad, end=": ")
    for kolonne in range(1, storrelse+1):
        produkt = rad * kolonne
        print(produkt, end= " ")
    print()
