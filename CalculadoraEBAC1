import os

continuar="S"
while continuar=="S":
    os.system('cls' if os.name == 'nt' else 'clear')
    valor1=int(input("Digite o valor1: "))
    valor2=int(input("Digite o valor2: "))
    operador=input("Digite algum desses operadores(+),(-),(*),(/),(**): ")
    match operador:
        case "+":
            result=valor1+valor2
            print(result)
        case "-":
            result=valor1-valor2
            print(result)
        case "*":
            result=valor1*valor2
            print(result)
        case "/":
            result=float(valor1/valor2)
            print(result)
        case "**":
            result=valor1**valor2
            print(result)
    continuar=input("Deseja fazer mais alguma operação S ou N: ").capitalize()
else:
    print("Programa Finalizado")
