# nome (imput ("informe seu nome:"))

# if nome == "Pietro":
#     resposta="Pietro presente"
# elif nome == "Phellipe":
#     resposta = "Phellipe presente"

# mes = int(input("informe o mes do seu anivrsario"))
# if mes == 1:
#     signo == "aquario"
# elif mes == 2:
#     signo = "peixes"
# elif mes == 3:
#     signo = "aries"
# elif mes == 4:
#     signo = "touro"
# elif mes == 5:
#     signo = "gemeos"
# elif mes == 6:
#     signo = "cancer"
# elif mes == 7:
#     signo = "leao"
# elif mes == 8:
#     signo = "virgem"
# elif mes == 9:
#     signo = "libra"
# elif mes == 10:
#     signo = "escorpiao"
# elif mes == 11:
#     signo = "sargitario"
# elif mes == 12:
#     signo = "capricornio"

# print(f"Seu signo é {signo}.")

# Visão Match Case:
# match mes:
#     (case 1:) and (case 2):
#         signo = "aquario"

# #VISÃO MATCH CASE:
# match mes:
#     case 1:
#         signo="Aquário"
#     case 2:
#         signo="Áries"
#     case 3:
#         signo="Touro"
#     case 4:
#         signo="Gêmeos"
#     case 5:
#         signo="Câncer"
#     case _:
#         signo="Número de mês inválido"

# print(f"{signo}.")

# meunome = "Lucas Leal"

# # for i in meunome:
# #     print(i)
    
# # for i in meunome:
# #     print(meunome [1])
    
# for i in range(2,101,2):
#     print(i)
# somador = int(input("registro:"))
# controle = 0

# while controle <= 30:
#     controle=controle=somador
#     somador = int(input("registro"))
    
# print("oficina lotada!")


# for i in range(5):
#     print(f"Número {i + 1} de 5:")
#     num = float(input("Digite um número: "))
    
#     dobro = num * 2
#     triplo = num * 3
#     quádruplo = num * 4
    
#     print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")


# while contador < limite: # A condição de parada: Enquanto o contador for menor que 5
#  try:
#  print(f"Número {contador + 1} de {limite}:")
#  num = float(input("Digite um número: "))
 
#  dobro = num * 2
#  triplo = num * 3
#  quádruplo = num * 4
 
#  print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
#  contador = contador + 1 # IMPORTANTÍSSIMO! Incrementa o contador para evitar loop
# infinito
 
#  except ValueError:
#  print("Entrada inválida. Tente novamente.")
#  # Não incrementamos o contador para dar nova chance ao usuário

acertou = 0
while acertou < 5:
    print(f"Número {acertou + 1} de 5:") 
    num = float(input("Digite um número: ")) 
        
    dobro = num * 2 
    triplo = num * 3 
    quádruplo = num * 4 
        
    print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
    acertou+=1 