print('Bem-vindo ao software de gerenciamento de funcionários de Maria Eduarda Vicente Bauer')
print('-' * 20)

lista_funcionarios = []
id_global = 5297739

#Função para cadastrar funcionário
def cadastrar_funcionario(id):
  # Este é o ID que será usado para o novo funcionário
  print(f'Cadastrando o funcionário com ID: {id}')
  # a. Pergunta nome, setor, salario
  nome = input('Digite o nome do funcionário: ')
  setor = input('Digite o setor do funcionário: ')
  salario = float(input('Digite o salário do funcionário (R$): '))
  print('-' * 20)

  # b. Armazena tudo dentro de um dicionário
  funcionario = {
      'id': id,
      'nome': nome,
      'setor': setor,
      'salario': salario
  }

  lista_funcionarios.append(funcionario.copy())

#Função para consultar funcionários
def consultar_funcionarios():
  # vi. Enquanto o usuário não escolher a opção 4, o menu de consulta se repete
  while True:
    print('--- MENU DE CONSULTA ---')
    # a. Pergunta qual opção deseja
    print('1. Consultar Todos')
    print('2. Consultar por Id')
    print('3. Consultar por Setor')
    print('4. Retornar ao menu')

    try:
      opcao_consulta = int(input('Escolha uma opção: '))
      print('-' * 20)

      # i. Se Consultar Todos
      if opcao_consulta == 1:
        if not lista_funcionarios: # Verifica se a lista está vazia
          print('Não há funcionários cadastrados.')
        else:
          print('--- TODOS OS FUNCIONÁRIOS ---')
          for funcionario in lista_funcionarios:
            # Imprime os dados de cada funcionário no dicionário
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Setor: {funcionario['setor']}")
            print(f"Salário: R$ {funcionario['salario']:.2f}")
            print('-' * 20)

      # ii. Se Consultar por Id
      elif opcao_consulta == 2:
        id_busca = int(input('Digite o Id do funcionário: '))
        encontrado = False # flag que vou usar para saber se achei o funcionario
        for funcionario in lista_funcionarios:
          if funcionario['id'] == id_busca:
            print('--- FUNCIONÁRIO ENCONTRADO ---')
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Setor: {funcionario['setor']}")
            print(f"Salário: R$ {funcionario['salario']:.2f}")
            print('-' * 20)
            encontrado = True
            break # se achado quebra para fora do laço
        if not encontrado:
          print('Funcionário com este Id não encontrado.')
          print('-' * 20)

      # iii. Se Consultar por Setor
      elif opcao_consulta == 3:
        setor_busca = input('Digite o setor: ')
        print(f'--- FUNCIONÁRIOS DO SETOR: {setor_busca} ---')
        encontrado = False
        for funcionario in lista_funcionarios:
          if funcionario['setor'].lower() == setor_busca.lower():
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Setor: {funcionario['setor']}")
            print(f"Salário: R$ {funcionario['salario']:.2f}")
            print('-' * 20)
            encontrado = True
        if not encontrado:
          print('Nenhum funcionário encontrado neste setor.')
          print('-' * 20)

      # iv. Se Retornar ao menu
      elif opcao_consulta == 4:
        return # Sai da função consultar_funcionarios e volta pro menu principal

      # v. Se Entrar com um valor diferente
      else:
        print('Opção inválida. Tente novamente.')
        print('-' * 20)

    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')
        print('-' * 20)


# Função para remover funcionário
def remover_funcionario():
  while True:
    try:
      # a. Pergunta pelo id do funcionário a ser removido
      id_remover = int(input('Digite o Id do funcionário a ser removido: '))

      funcionario_para_remover = None
      # Procura o dicionário do funcionário na lista
      for funcionario in lista_funcionarios:
        if funcionario['id'] == id_remover:
          funcionario_para_remover = funcionario
          break

      # b. Se achou, remove o funcionário da lista
      if funcionario_para_remover:
        lista_funcionarios.remove(funcionario_para_remover)
        print('Funcionário removido com sucesso!')
        print('-' * 20)
        return # Sai da função depois de remover
      else:
        # c. Se o id fornecido não existe
        print('Id inválido. Tente novamente.')
        print('-' * 20)

    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')
        print('-' * 20)


# Estrutura de menu no código principal (main)
# vi. Enquanto o usuário não escolher a opção 4, o menu se repete
while True:
  print('--- MENU PRINCIPAL ---')
  # a. Pergunta qual opção deseja
  print('1. Cadastrar Funcionário')
  print('2. Consultar Funcionário(s)')
  print('3. Remover Funcionário')
  print('4. Encerrar Programa')

  try:
    opcao_menu = int(input('Escolha uma opção: '))
    print('-' * 20)

    # i. Se Cadastrar Funcionário
    if opcao_menu == 1:
      cadastrar_funcionario(id_global)
      id_global += 1 # Incrementa o ID para o próximo cadastro ser único

    # ii. Se Consultar Funcionário
    elif opcao_menu == 2:
      consultar_funcionarios()

    # iii. Se Remover Funcionário
    elif opcao_menu == 3:
      remover_funcionario()

    # iv. Se Encerrar Programa
    elif opcao_menu == 4:
      print('Encerrando o programa...')
      break # Quebra o loop 'while True' e o programa acaba

    else:
      print('Opção inválida. Tente novamente.')
      print('-' * 20)

  except ValueError:
    print('Entrada inválida. Por favor, digite um número de 1 a 4.')
    print('-' * 20)
