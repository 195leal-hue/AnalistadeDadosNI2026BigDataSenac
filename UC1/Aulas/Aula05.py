# impar_1 = 3
# impar_2 = 5
# impar_3 = 13
# impar_4 = 27

# impares = []
# print(type(impares))
# impares = [3,5,13,27]
# print(impares[-2])
# lista_01 = [
#     12,
#     "Pedro",
#     12.53343,
#     "[(_{^^}_)]",
#     false,
#     0,
#     {2,4,6,8}
#     ]

# print(lista_01[1], lista_01[2], lista_01[4], lista_01[6][2])

# lista_2 = ["Marcia"]

# if "Marcia" in lista_2:
#     print(lista_2)
# else:
#     print("Marcia não esta rpesente na lista.")
    
# participantes = ["Isaque","Luana","Fernando","Bianca","Ana"]
# for participante in participantes:
#     print(participante)
    
# partic_2 = "Hugo"
# participantes.append(partic_2)
# participantes.insert(2,partic_2)
# participantes.pop(1)
# participantes.remove("Hugo")
# participantes.reverse()
# participantes.index
# participantes.clear
# participantes.count

# print(participantes)

# participantes = ("Isaque","Luana","Fernando","Bianca","Ana Paula")

# participante_02 = ("fernnando", "111.111.***-**","Avenida Dr. thiburcio, 444", "DDD21999999999")
# print(participante_02.index("Avenida Dr. thiburcio, 444"))
# listinha_participante_02=list(participante_02)

# print(listinha_participante_02)

numeros_pares = {
    202,
    203,
    204,
    204,
    205,
    219,
    291,
    292,
    202
}
#print(numeros_pares,type(numeros_pares))
numeros_impares = (111,111,112,291,291,205)




produtos = {"Maçã":5.99,"laranja":4.79}
# print(produtos,(type(produtos)))
print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("laranja"))
produtos2 = produtos.copy()
produtos2["Maçã"]=7.99
print(produtos2)
produtos.update(produtos)
achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)