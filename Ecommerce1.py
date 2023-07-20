# Implementando a Leituda de informações dos produtos | 1 de 5
# Implementando o cadastro de produtos | Parte 2 de 5
# Implementando o menu de interação | Parte 3 de 5
# Implementando o menu de produtos | Parte 4 de 5
# Implementando o filtro de produtos por preço | 5 de 5

def cadastrarProduto(estoque):
    codigo = int(input("Digite o código do produto: "))
    if codigo in estoque:
        print ('Produto já cadastrado')
    categoria = input("Digite a categoria do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {"codigo": codigo, "produto": nome, "info": descricao, "preco": preco}
    if categoria not in estoque:
        estoque[categoria] = []
        estoque[categoria].append(produto)
    else:
        estoque[categoria].append(produto)
    return(estoque)

def mostrarProduto(estoque):
    print("______________________________________")
    print("________Informações do Produto________")
    print("______________________________________\n")
    for categoria in estoque:
        for produto in estoque[categoria]:
            print("PRODUTO")
            print(f"Código: {produto['codigo']}")
            print(f"Categoria: {categoria}")
            print(f"Produto: {produto['produto']}")
            print(f"Descrição: {produto['info']}")
            print(f"Preço: {produto['preco']}\n")

estoque = {} # Armazena Informações
estoque = {
            'Quadro': [
                        {'codigo': 99, 'produto': 'Quadro Show Gravel 2023', 'info': 'gravel', 'preco': 1299.99},

                        {'codigo': 34, 'produto': 'Quadro Cube Nuroad Ex 2021', 'info': 'Gravel', 'preco': 4899.99}], 
            'Rodas':  [ 
                        {'codigo': 12, 'produto': 'Rodas Roval Terra C', 'info': 'gravel//carbono', 'preco': 8999.99}], 

            'Pneus': [
                        {'codigo': 33, 'produto': 'Pneu Pathfinder 700x42', 'info': 'gravel', 'preco': 589.99},
                      
                        {'codigo': 88, 'produto': 'Pneu WTB Raddler 700x44', 'info': 'gravel', 'preco': 489.99}], 
                        
            'Guidão': [
                        {'codigo': 44, 'produto': 'Guidão Discovery Shimano Pro', 'info': 'guidão gravel 30 graus flare', 'preco': 459.99}], 
                        
            'Pedal': [
                        {'codigo': 22, 'produto': 'Pedal Shimano M520', 'info': 'pedal', 'preco': 569.99}]}

def mostrarProdutoPreco(estoque, precoMax):
    print("______________________________________")
    print("________Informações do Produto________")
    print("______________________________________\n")
    for categoria in estoque:
        for produto in estoque[categoria]:
            if produto['preco'] <= precoMax:
               print("PRODUTO")
               print(f"Código: {produto['codigo']}")
               print(f"Categoria: {categoria}")
               print(f"Produto: {produto['produto']}")
               print(f"Descrição: {produto['info']}")
               print(f"Preço: {produto['preco']}\n")

while True:
    print("Seja vem vindo a Mike's Bike Shop, sua loja de ciclismo online!")
    print("O que você deseja realizar? \n 1) Cadastrar Produto, 2) Mostrar Produto, 3) Consulta por preço, 4) Finalizar Sistema: ")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrarProduto(estoque)
    elif opcao == 2:
        mostrarProduto(estoque)
    elif opcao == 3:
        precoMax = float(input("Digite o valor máximo do produto: "))
        if precoMax <= precoMax:
            mostrarProdutoPreco(estoque, precoMax)
    elif opcao == 4:
        print("Programa finalizado!")
        break
    else:
        print("Opção Inválida!")