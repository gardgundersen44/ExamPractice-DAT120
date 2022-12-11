import turtle
import turtle as tu

# Tegner en taggete linje
def tegn_linje(antall_tagger, tagg_storrelse=15):
    turtle.speed(0)
    for i in range (0, antall_tagger):
        tu.left(60)
        tu.forward(tagg_storrelse)
        tu.right(120)
        tu.forward(tagg_storrelse)
        tu.left(60)

def tegn_firkant():

    for j in range(4):
        try:
            antall_tagger = int(input("Oppgi antall tagger: "))
            tagg_storrelse = int(input("Oppgi størrelsen på taggene: "))
            tegn_linje(antall_tagger, tagg_storrelse)
            tu.right(90)
        except ValueError:
            tegn_linje(antall_tagger)
            tu.right(90)


if __name__ == "__main__":
    tegn_firkant()
    turtle.setup(200,200,200,200)
    turtle.Screen().exitonclick()
