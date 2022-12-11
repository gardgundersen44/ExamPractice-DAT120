'''
1. Tall som forekommer mist tre ganger -> returner 3 * tallet
2. Hvis flere en 1 tall som forekommer minst tre ganger -> beregn returverdi basert på hvilke som er høyest
3. Hvis ingen tall forekommer minst tre ganger, returner 0
'''


liste1 = [1,2,2,3,4,4,4,6,3,3,2,2,2,1]
liste2 = [3, 4, 3, 4, 3, 2, 5, 5, 6]
liste3 = [1, 2, 3, 4, 5, 6, 6, 6, 5, 5]
liste_av_tall = []
liste_minst_tre = []

def analyser_liste(liste):
    liste_ener = []
    liste_toer = []
    liste_treer = []
    liste_firer = []
    liste_femer = []
    liste_sekser = []

    for tall in range(1,7):
        for i in liste:
            current_tall = i
            if tall == current_tall:
                if current_tall == 1:
                    liste_ener.append(current_tall)
                elif current_tall == 2:
                    liste_toer.append(current_tall)
                elif current_tall == 3:
                    liste_treer.append(current_tall)
                elif current_tall == 4:
                    liste_firer.append(current_tall)
                elif current_tall == 5:
                    liste_femer.append(current_tall)
                else:
                    liste_sekser.append(current_tall)

    liste_av_tall.append(liste_ener)
    liste_av_tall.append(liste_toer)
    liste_av_tall.append(liste_treer)
    liste_av_tall.append(liste_firer)
    liste_av_tall.append(liste_femer)
    liste_av_tall.append(liste_sekser)

    # Sjekk hvilke lister som har minst 3 tall (dersom det finnes noen)
    for k in liste_av_tall:
        if len(k) >= 3:
            liste_minst_tre.append(k)

    # Sjekk hvilke lister som lagrer størst tallverdi
    sjekk_verdi = 0
    for l in liste_minst_tre:
        if sjekk_verdi < l[0]:
            sjekk_verdi = l[0]
    return f"Tallet med størst verdi er: {sjekk_verdi}, og resultatet blir {sjekk_verdi*3}"

    if len(liste_minst_tre) == 0:
        return 0

if __name__ == "__main__":
    print(analyser_liste(liste3))