class Rom:
    def __init__(self, romtype, kapasitet, romnummer):
        self.romtype = romtype
        self.kapasitet = kapasitet
        self.romnummer = romnummer

    def __str__(self):
        return f"Rom: {self.romnummer} av {self.romtype} med kapasitet {self.kapasitet}"

def sjekk_rom(list, oppgitt_kapasitet):
    rom_med_samme_kapasitet = []
    for rom in list:
        if rom.kapasitet == oppgitt_kapasitet:
            rom_med_samme_kapasitet.append(rom)
    return rom_med_samme_kapasitet

def print_liste(liste):
    for j in liste:
        print(j)

# Test
if __name__ == "__main__":
    rom1 = Rom('A',200, 322)
    rom2 = Rom('B',200, 442)
    rom3 = Rom('C', 221, 223)
    rom4 = Rom('D', 224, 112)
    rom5 = Rom('E', 200, 244)
    rom_liste = [rom1, rom2, rom3, rom4, rom5]

    print_liste(sjekk_rom(rom_liste, 200))
