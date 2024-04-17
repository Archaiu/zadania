n = 6

# Rysowanie kwadratu o boku n

for i in range(n):
    for j in range(n):
        print(" *",end="")
    print("")

# Tutaj prostokąt n x 2*n
print("")

for i in range(2*n):
    for j in range(n):
        print(" *",end="")
    print("")

# A tutaj prostokąt 2*n x n

for i in range(n):
    for j in range(2*n):
        print(" *",end="")
    print("")
