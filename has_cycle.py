

def has_cycle(head):
    past_heads = []
    # Cria uma lista para armazenar os Nodes já visitados
    while head.next:
        # Enquanto o proximo Node não for nulo, verifica se ele já foi visitado
        if head.next in past_heads:
            return 1
        past_heads.append(head.next)
        head = head.next
        # Adiciona o Node atual na lista de Nodes visitados e passa para o próximo Node
    return 0
    # Se não houver ciclos, retorna 0
