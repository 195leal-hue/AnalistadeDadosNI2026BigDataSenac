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