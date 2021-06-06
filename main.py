opcao = 0
dados = list()
produtos = list()
print('BEM VINDO AO E-COMMERCE!')
while opcao != 5:
    print('''    [1] Listar Produtos 
    [2] Cadastrar Produto
    [3] Alterar Produto
    [4] Excluir Produto
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção?'))
    if opcao == 1:
        print(f'{"No.":<4}{"NOME":<10}{"VALOR":<8}{"DESCRICAO":<5}')
        print('-' * 26)
        for index, produto in enumerate(produtos):
            print(f'{index:<4}{produto[0]:<10}{produto[1]:<8.1f}{produto[2]:<5}')
    elif opcao == 2:
        while True:
            dados.append(str(input('Nome: ')))
            dados.append(int(input('Valor: ')))
            dados.append(str(input('Descricao: ')))
            produtos.append(dados[:])
            dados.clear()

            resp = str(input('Quer continuar cadastrando produtos? [S/N]'))
            if resp in 'Nn':
                break
        print('Os dados foram cadastrados!')
        print('=-=' * 30)
    elif opcao == 3:
        opc = int(input('Qual produto deseja alterar? (999 interrompe)'))
        if opc == 999:
            print('FINALIZANDO...')
            break
        if opc <= len(produtos) - 1:
            dados.append(str(input('Nome: ')))
            dados.append(int(input('Valor: ')))
            dados.append(str(input('Descricao: ')))
            produtos.pop(opc)
            produtos.insert(opc, dados[:])
            dados.clear()
    elif opcao == 4:
        opc = int(input('Qual produto deseja excluir? (999 interrompe)'))
        if opc == 999:
            print('FINALIZANDO...')
            break
        if opc <= len(produtos) - 1:
            produtos.pop(opc)
    elif opcao == 5:
        break
    else:
        print('Opção Inválida. Tente novamente')
print('Fim do programa! Volte Sempre!')