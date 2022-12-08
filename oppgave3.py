# Regner ut verdier fra -1000 til 1000, og plotter funksjonsverdiene i matplotlib
import matplotlib.pyplot as plt

# x-verdiene vil da være tallene mellom -1000 og 1000
# y-verdiene vil da være verdiene som kommer ut fra funksjonen

plt.title("Lister og plotting")
plt.xlabel("x-verdier (fra -1000 til 1000)")
plt.ylabel("y-verdier (funksjonsverdiene)")

x_verdier = []
y_verdier = []

def funksjonen(tall):
    return tall**2 - tall*500

for tall in range (-1000, 1001):
    x_verdier.append(tall)
    y_verdier.append(funksjonen(tall))

plt.plot(x_verdier, y_verdier)
plt.show()