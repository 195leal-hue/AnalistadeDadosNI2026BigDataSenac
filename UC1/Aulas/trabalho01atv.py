# cardapio.py

CARDAPIO = {
    1: {"nome": "X-Burger Especial", "preco": 28.90},
    2: {"nome": "Batata Frita Grande", "preco": 22.00},
    3: {"nome": "Refrigerante Lata", "preco": 6.00},
    4: {"nome": "Água Mineral", "preco": 4.50},
    5: {"nome": "Sobremesa do Dia", "preco": 12.00}
}

# comanda.py
#from cardapio import CARDAPIO

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
#from comanda import cliente_comanda

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
        
        
