# wpisz tutaj funkcję zwracającą wartość współczynnika w pochodnej w zależności od pierwotnego współczynnika i potęgi zmiennej x
def pochodna(wsp, potega):
  
# tego nie ruszaj :)
print("Witaj w programie obliczającym pochodną wielomianu ax^3 + bx^2 + cx + d.")
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))
d = int(input("Podaj współczynnik d: "))

i = 0
poch = []
for wsp in [d, c, b, a]:
    poch.append(pochodna(wsp, i))
    i+=1


print("Pochodna funkcji:")
print(poch[3], "x^2 +", poch[2], "x +", poch[1], "+", poch[0])
