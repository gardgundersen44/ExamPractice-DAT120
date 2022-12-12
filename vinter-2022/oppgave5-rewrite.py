# Historisk værdata

total_nedboer = {}
hoyeste_middel_temperatur = {}
laveste_middel_temperatur = {}
dato_max = {}
dato_min = {}

with open("vaer_stasjoner.csv", encoding="UTF8") as fil:
    for rad in fil:
        kolonne = rad.strip().split(";")

        # Sjekker at vi har fått all informasjon oppgitt
        if len(kolonne) < 5:
            continue
        try:
            # Regner ut total nedboer for respektiv værstasjon
            if kolonne[0] in total_nedboer:
                total_nedboer[kolonne[0]] += float(kolonne[4])
            else:
                total_nedboer[kolonne[0]] = float(kolonne[4])
            # Regner ut maks temperatur:
            temperatur = float(kolonne[3])
            if kolonne[0] in hoyeste_middel_temperatur:
                if temperatur > hoyeste_middel_temperatur[kolonne[0]]:
                    hoyeste_middel_temperatur[kolonne[0]] = temperatur
                    dato_max[kolonne[0]] = kolonne[2]
            else:
                hoyeste_middel_temperatur[kolonne[0]] = temperatur
                dato_max[kolonne[2]] = kolonne[2]

            # Regner ut min temperatur
            if kolonne[0] in laveste_middel_temperatur:
                if temperatur < laveste_middel_temperatur[kolonne[0]]:
                    laveste_middel_temperatur[kolonne[0]] = temperatur
                    dato_min[kolonne[0]] = kolonne[2]
            else:
                laveste_middel_temperatur[kolonne[0]] = temperatur
                dato_min[kolonne[0]] = kolonne[2]
        # Skip dersom ikke kan konvertee fra string til float
        except ValueError:
            continue

        with open("totaler_for_alle_vaerstasjoner.csv", encoding="UTF8") as skrivefil:
            skrivefil.write("Vaerstasjon; Total nedboer; hoyeste middeltemperatur; dato; laveste middeltemperatur; dato\n")

            for vaerstasjon in total_nedboer:
                skrivefil.write(f"{vaerstasjon};")
                skrivefil.write(f"{total_nedboer[vaerstasjon]};")
                skrivefil.write(f"{hoyeste_middel_temperatur[vaerstasjon]};")
                skrivefil.write(f"{dato_max[vaerstasjon]};")
                skrivefil.write(f"{laveste_middel_temperatur[vaerstasjon]};")
                skrivefil.write(f"{dato_min};\n")








