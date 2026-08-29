# print("calculos no PY")

# a = 25
# b = 5
# print("Soma:", a + b)
# print("Subtração:", a - b)
# print("Multiplicação:", a * b)
# print("Divisão:", a / b)
# print("resto:", a % b)
# print("media:", (a + b) /2)


# print("--- Cálculo de Lâmpadas por Área ---")
# largura = float(input("Digite a largura do cômodo (em metros): "))
# comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# if largura <= 0 or comprimento <= 0:
#     print("Erro: As dimensões devem ser maiores que zero.")
# else:
#     area = largura * comprimento
#     potencia_necessaria = area * POTENCIA_POR_METRO
#     match area:
#         case a if a <= 3:
#             lampadas = 1
#         case _:
#             import math
#             lampadas = math.ceil(area / METROS_POR_BOCAL)

#     print(f"\nÁrea do cômodo: {area:.2f} m²")
#     print(f"Potência total necessária: {potencia_necessaria} W")
#     print(f"Número de lâmpadas/bocais necessários: {lampadas}")
    

# import math

# print("--- Calculadora de Caixas de Azulejos para Cozinha ---")

# try:
#     comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
#     largura = float(input("Digite a largura da cozinha (em metros): "))
#     altura = float(input("Digite a altura da cozinha (em metros): "))
#     if comprimento <= 0 or largura <= 0 or altura <= 0:
#         print("Erro: Todas as dimensões devem ser maiores que zero.")
#     else:
#         area_paredes = (2 * comprimento * altura) + (2 * largura * altura)
#         METROS_POR_CAIXA = 1.5
#         caixas_necessarias = math.ceil(area_paredes / METROS_POR_CAIXA)
#         print("\n--- Resultados ---")
#         print(f"Área total das paredes: {area_paredes:.2f} m²")
#         print(f"Quantidade de caixas de azulejos necessárias: {caixas_necessarias} caixas")
#     print("Erro: Por favor, digite apenas números válidos.")
    

# print("--- Calculadora de Rendimento do Taxista ---")

# PRECO_COMBUSTIVEL = 6.15

# try:
#     odometro_inicio = float(input("Marcação do odômetro no início do dia (km): "))
#     odometro_fim = float(input("Marcação do odômetro no final do dia (km): "))
#     litros_gastos = float(input("Número de litros de combustível gasto: "))
#     valor_recebido = float(input("Valor total recebido dos passageiros (R$): "))

#     if odometro_fim < odometro_inicio:
#         print("Erro: A marcação final do odômetro não pode ser menor que a inicial.")
#     elif litros_gastos <= 0 or odometro_inicio < 0 or odometro_fim < 0 or valor_recebido < 0:
#         print("Erro: Os valores de quilometragem, litros e recebimento devem ser válidos e maiores ou iguais a zero.")
#     else:
#         km_rodados = odometro_fim - odometro_inicio
        
#         if km_rodados == 0 or litros_gastos == 0:
#             print("\nAviso: O veículo não rodou ou não gastou combustível no dia.")
#             media_consumo = 0.0
#         else:
#             media_consumo = km_rodados / litros_gastos
#         custo_combustivel = litros_gastos * PRECO_COMBUSTIVEL
#         lucro_liquido = valor_recebido - custo_combustivel

#         print("\n--- Relatório Diário do Taxista ---")
#         print(f"Quilometragem rodada: {km_rodados:.2f} km")
#         print(f"Média de consumo: {media_consumo:.2f} km/L")
#         print(f"Gasto com combustível: R$ {custo_combustivel:.2f}")
#         print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")
#     print("Erro: Por favor, digite apenas números válidos.")
    
    
# print("--- Sistema de Login ---")

# USUARIO_CORRETO = "admin"
# SENHA_CORRETA = "123456"

# tentativas_restantes = 3

# while tentativas_restantes > 0:
#     print(f"\nTentativas restantes: {tentativas_restantes}")
    
#     usuario_digitado = input("Digite o nome de usuário: ")
#     senha_digitada = input("Digite a senha: ")
    
#     if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
#         print("\n Login realizado com sucesso! Bem-vindo ao sistema.")
#         break  # Sai imediatamente do loop se acertar
#     else:
#         tentativas_restantes -= 1
#         print("Usuário ou senha incorretos.")

# if tentativas_restantes == 0:
#     print("\n Acesso bloqueado! Você esgotou o número de tentativas permitidas.")

# print("Cadastro de candidatos")

# ano_atual = 2026

# candidatos_cadastrados = []

# for i in range(1,13):
#     print(f"candidato {i} de 12")
    
#     try:
#         nome = input("digite o nome do candidatos ")
#         ano_de_nascimento = int(imput("digite o ano de nascimento:"))
        
#         if ano_de_nascimento > ano_atual or ano_de_nascimento < 1900:
#             print("Erro: Acesso invalido para menores de 18 anos")
#             continue
#         idade = ano_atual - ano_de_nascimento
#         if idade < 18:
#             print(f'acesso negado')
#             continue
#         else:
#             print(f"Proxima etapa ")
#             telefone = input("Digite o telefone do candidato: ")
#             email = input("Digite o e-mail do candidato: ")
#             candidatos_cadastrados.append({
#                 "nome": nome,
#                 "idade": idade,
#                 "telefone": telefone,
#                 "email": email
#             })
#         print(f" Cadastro de {nome} realizado com sucesso!\n")
    
#     except ValueError:
#         print("Erro: Digite apenas números válidos para o ano de nascimento.\n")