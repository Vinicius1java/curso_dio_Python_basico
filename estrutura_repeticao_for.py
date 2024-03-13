nome = input("Digite seu nome:")
VOGAIS = "AEIOU"


for letra in nome :
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

#Registra as consoantes

for letra in nome :
    if letra.upper() not in VOGAIS:
        print(letra, end="/")
print()

#numero de 0 a 11
for numero in range(0,11):
    print(numero, end=" ")
print()

#tabuada do 5
for numero in range (0,51,5):
    print(numero, end=" ")
print()