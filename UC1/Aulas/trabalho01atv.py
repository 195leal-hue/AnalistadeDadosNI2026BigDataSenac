# cardapio.py

# CARDAPIO = {
#     1: {"nome": "X-Burger Especial", "preco": 28.90},
#     2: {"nome": "Batata Frita Grande", "preco": 22.00},
#     3: {"nome": "Refrigerante Lata", "preco": 6.00},
#     4: {"nome": "Água Mineral", "preco": 4.50},
#     5: {"nome": "Sobremesa do Dia", "preco": 12.00}
# }

# comanda.py
def exibir_CARDAPIO():

def cliente_comanda():
    print("=" * 40)
    print("      BEM-VINDO AO NOSSO RESTAURANTE")
    print("=" * 40)
    
    # Pergunta o número da mesa antes de iniciar os pedidos
    while True:
        mesa = input("Digite o número da mesa: ").strip()
        if mesa.isdigit() and int(mesa) > 0:
            mesa = int(mesa)
            break
        print("Número de mesa inválido. Tente novamente.")
        
    carrinho = []
    
    while True:
        print(f"\n--- CARDÁPIO DIGITAL (Mesa {mesa}) ---")
        for codigo, item in CARDAPIO.items():
            print(f"[{codigo}] {item['nome']} - R$ {item['preco']:.2f}")
            
        print("[0] Finalizar Pedido")
        
        escolha = input("\nEscolha o código do item desejado: ").strip()
        
        if escolha == '0':
            break
            
        if escolha.isdigit() and int(escolha) in CARDAPIO:
            cod = int(escolha)
            qtd = int(input(f"Quantas unidades de '{CARDAPIO[cod]['nome']}'? "))
            
            if qtd > 0:
                carrinho.append({
                    "nome": CARDAPIO[cod]["nome"],
                    "preco": CARDAPIO[cod]["preco"],
                    "quantidade": qtd
                })
                print(f"-> {qtd}x {CARDAPIO[cod]['nome']} adicionado(s) à comanda.")
            else:
                print("A quantidade precisa ser maior que zero.")
        else:
            print("Código inválido. Tente novamente.")
            
    # Retorna tanto a mesa escolhida quanto os itens do carrinho agrupados num dicionário
    return {
        "mesa": mesa,
        "itens": carrinho
    }
    
    
# main.py
from comanda import cliente_comanda

def atendimento_caixa(dados_pedido):
    mesa = dados_pedido["mesa"]
    carrinho = dados_pedido["itens"]
    
    if not carrinho:
        print(f"\nNenhum item selecionado para a Mesa {mesa}. Comanda cancelada.")
        return

    print("\n" + "=" * 40)
    print(f"     FECHAMENTO DE CAIXA - MESA {mesa}")
    print("=" * 40)
    
    total = 0
    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal
        print(f"{item['quantidade']}x {item['nome']} ....... R$ {subtotal:.2f}")
        
    print("-" * 40)
    print(f"VALOR TOTAL DA MESA {mesa}: R$ {total:.2f}")
    print("=" * 40)
    
    input(f"Pressione Enter para processar o pagamento da Mesa {mesa} e liberar para a cozinha...")
    print(f"\n[Operação Concluída] Pagamento da Mesa {mesa} registrado! Pedido enviado para a cozinha.")
    print("----------------------------------------")
    print("Próximo atendimento pode ser iniciado.\n")

if __name__ == "__main__":
    while True:
        dados_comanda = cliente_comanda()
        atendimento_caixa(dados_comanda)
        
        continuar = input("Iniciar atendimento para a próxima mesa? (s/n): ").strip().lower()
        if continuar != 's':
            print("Sistema encerrado.")
            break
        
        
# Cardápio do restaurante com os preços
# cardapio = {
#     1: {"nome": "Hambúrguer Artesanal", "preco": 32.50},
#     2: {"nome": "Pizza Margherita", "preco": 45.00},
#     3: {"nome": "Batata Frita", "preco": 18.00},
#     4: {"nome": "Refrigerante 350ml", "preco": 6.50},
#     5: {"nome": "Suco Natural", "preco": 8.00},
# }

# def exibir_cardapio():
#     print("\n--- CARDÁPIO ---")
#     for codigo, item in cardapio.items():
#         print(f"[{codigo}] {item['nome']} - R$ {item['preco']:.2f}")
#     print("-" * 20)

# def fazer_pedido():
#     pedido = []
    
#     print("Bem-vindo ao sistema de pedidos!")
    
#     while True:
#         exibir_cardapio()
#         try:
#             opcao = int(input("Digite o código do item que deseja (ou 0 para encerrar): "))
            
#             if opcao == 0:
#                 break
            
#             if opcao in cardapio:
#                 quantidade = int(input(f"Quantas unidades de '{cardapio[opcao]['nome']}'? "))
#                 if quantidade > 0:
#                     item_pedido = {
#                         "nome": cardapio[opcao]["nome"],
#                         "preco_unitario": cardapio[opcao]["preco"],
#                         "quantidade": quantidade,
#                         "subtotal": cardapio[opcao]["preco"] * quantidade
#                     }
#                     pedido.append(item_pedido)
#                     print(f"-> Adicionado: {quantidade}x {item_pedido['nome']}")
#                 else:
#                     print("A quantidade deve ser maior que zero.")
#             else:
#                 print("Código inválido! Escolha uma opção do cardápio.")
        
#         except ValueError:
#             print("Por favor, digite apenas números válidos.")

#     return pedido

# def calcular_resumo(pedido):
#     if not pedido:
#         print("\nNenhum item foi solicitado.")
#         return

#     total_geral = 0
    
#     print("\n" + "="*30)
#     print("       RESUMO DO PEDIDO")
#     print("="*30)
    
#     for item in pedido:
#         print(f"{item['quantidade']}x {item['nome']} - R$ {item['subtotal']:.2f} (R$ {item['preco_unitario']:.2f} un)")
#         total_geral += item['subtotal']
        
#     print("-" * 30)
#     print(f"TOTAL A PAGAR: R$ {total_geral:.2f}")
#     print("="*30)
#     print("Obrigado pela preferência! Bom apetite!")

# # Execução do programa
# if __name__ == "__main__":
#     meu_pedido = fazer_pedido()
#     calcular_resumo(meu_pedido)


# sistema_restaurante.py
# from cardapio import CARDAPIO
# from mesa import cliente_comanda

# def cliente_comanda():
#     carrinho = []
#     print("=" * 40)
#     print("      BEM-VINDO AO NOSSO RESTAURANTE")
#     print("=" * 40)
    
#     while True:
#         print("\n--- CARDÁPIO DIGITAL ---")
#         for codigo, item in CARDAPIO.items():
#             print(f"[{codigo}] {item['nome']} - R$ {item['preco']:.2f}")
            
#         print("[0] Finalizar Pedido")
        
#         escolha = input("\nEscolha o código do item desejado: ").strip()
        
#         if escolha == '0':
#             break
            
#         if escolha.isdigit() and int(escolha) in CARDAPIO:
#             cod = int(escolha)
#             qtd = int(input(f"Quantas unidades de '{CARDAPIO[cod]['nome']}'? "))
            
#             if qtd > 0:
#                 carrinho.append({
#                     "nome": CARDAPIO[cod]["nome"],
#                     "preco": CARDAPIO[cod]["preco"],
#                     "quantidade": qtd
#                 })
#                 print(f"-> {qtd}x {CARDAPIO[cod]['nome']} adicionado(s) à comanda.")
#             else:
#                 print("A quantidade precisa ser maior que zero.")
#         else:
#             print("Código inválido. Tente novamente.")
            
#     return carrinho

# def atendimento_caixa(carrinho):
#     if not carrinho:
#         print("\nNenhum item selecionado. Comanda cancelada.")
#         return

#     print("\n" + "=" * 40)
#     print("         FECHAMENTO DE MESA / CAIXA")
#     print("=" * 40)
    
#     total = 0
#     for item in carrinho:
#         subtotal = item["preco"] * item["quantidade"]
#         total += subtotal
#         print(f"{item['quantidade']}x {item['nome']} ....... R$ {subtotal:.2f}")
        
#     print("-" * 40)
#     print(f"VALOR TOTAL DA MESA: R$ {total:.2f}")
#     print("=" * 40)
    
#     input("Pressione Enter para processar o pagamento e liberar para a cozinha...")
#     print("\n[Operação Concluída] Pagamento registrado! Pedido enviado para a cozinha.")
#     print("----------------------------------------")
#     print("Próximo cliente pode iniciar o atendimento.\n")

# if __name__ == "__main__":
#     while True:
#         comanda_atual = cliente_comanda()
#         atendimento_caixa(comanda_atual)
        
#         continuar = input("Iniciar atendimento para o próximo cliente? (s/n): ").strip().lower()
#         if continuar != 's':
#             print("Sistema encerrado.")
#             break
