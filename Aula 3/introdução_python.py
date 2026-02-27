
# Programa Calculadora Python 
# Disciplina Fundamentos de Programação
# Data: 26/02/2026

import math

print("##############################################")
print("             Calculadora Python               ")
print("##############################################")

print("Tecle a opção desejada e aperte ENTER: ")
print(" 1 - SOMA")
print(" 2 - SUBTRAÇÃO")
print(" 3 - DIVISÃO")
print(" 4 - MULTIPLICAÇÃO")
print(" 5 - POTÊNCIA")
print(" 6 - RAIZ QUADRADA")

op = input("Opção desejada")
op = int(op)

a = input("Entre com o valor de A: ")
a = int(a)
b = input("Entre com o valor de B: ")
b = int(b)

if ( op == 1):
        print("A soma é: ", a+b)
elif ( op == 2):
         print("A subtração é: ", a-b)
elif ( op == 3):
          print("A divisão é: ", a/b)
elif ( op == 4):
          print("A multiplicação é: ", a*b)
elif ( op == 5):
          print("A potência é: ", a**b)
elif ( op == 6):
          print("A raiz quadrada é: ", math.sqrt(a))


input()