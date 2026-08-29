
num1 = float(input("digite seu primeiro numero"))
num2 = float(input("digite seu segundo numero"))

def calculadora_v1(num1,num2,operador="3")

operador = input("informe a operação desejada entre : 1.adicao; 2")

match operador:
    case "1":
        print(f"resultado da soma: (num1 + num2)")
    case "2":
        print(f"resultado da subtração: (num1 - num2)")
    case "3":
        print(f"resultado da multiplicação: (num1 * num2)")
    case "4":
        if num2=0:
             print(f"resultado da divisão: (num1 / num2)")
        else:
            print(f"dividiu por zero, errou feio, errou rude!")
    case _ :
        print("informe um numero de operador valido")

calculinho = calculadora_v1(333,555)