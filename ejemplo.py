# import cs50
from cs50 import get_int

x = get_int("Dame el valor de x: ")
y = get_int("Dame el valor de y: ")
z = get_int("Dame el valor de z: ")

if x > y and x > z:
    print("Es mayor")
elif x < y and x < z:
    print("Es menor")

