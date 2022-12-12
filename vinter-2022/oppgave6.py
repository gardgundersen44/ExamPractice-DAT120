import random
# Korttypene som konstanter
KLOVER = 1
RUTER = 2
SPAR = 3
HJERTER = 4

class Kort:
 def __init__(self, korttype, verdi):
  self.korttype = korttype
  self.verdi = verdi

def __str__(self):
 korttypene = ["ingen", "Kløver", "Ruter", "Spar", "Hjerter"]
 if self.verdi == 1:
  return korttypene[self.korttype] + " ess"
 elif self.verdi <= 10:
  return f"{korttypene[self.korttype]} {self.verdi}"
 elif self.verdi == 11:
  return korttypene[self.korttype] + " knekt"
 elif self.verdi == 12:
  return korttypene[self.korttype] + " dame"
 elif self.verdi == 13:
  return korttypene[self.korttype] + " konge"
 else:
  return "Ugyldig kort!"

class Kortstokk:
 def __init__(self):
  self.kortene = list()

 def lag_kortene(self):
     for t in range(1, 5):
      for v in range(1, 14):
       self.kortene.append(Kort(t, v))

 def trekk(self):
     kortet = self.kortene[-1]
     del self.kortene[-1]
     return kortet

 def stokk(self):
  random.shuffle(self.kortene)

 def __str__(self):
     resultat = f"Kortstokk med {len(self.kortene)} kort\n"
     for kort in self.kortene:
      resultat += str(kort) + "\n"
     return resultat

if __name__ == "__main__":
    kortstokk = Kortstokk()
    liste = kortstokk.lag_kortene()
    korttype = kortstokk.kortene[0].korttype
    for i in liste:
        if i != korttype:
            sum = 0
        if kortet.verdi == 1:
            sum += 15
        elif kortet.verdi > 10:
            sum += 10
        else:
            sum += kortet.verdi
    print(sum)

