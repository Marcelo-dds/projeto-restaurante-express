import os;

restaurantes = [{'nome':'Praça','categoria':'Japonesa','status':False},
                {'nome':'Pizza Suprema','categoria':'Italiana','status' : True},
                 {'nome':'Cantina','categoria':'Italiano','status' : False}
                ]#isso e um dicionario dentro de uma lista, toda vez q falar dicionario falamos de chave e valor



def exibir_nome_do_programa():
    print('''
    
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''');

def exibir_opcoes():
    print('1- Cadastrar restaurante');
    print('2- Listar restaurante');
    print('3- Alternar estado do restaruante');
    print('4- Sair\n');

def finalizando_app():
    exibir_subtitulo('Encerrando Programa.')
    

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar para o menu: ');
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)) #vai criar uma linha de * conforme o tamanho do texto 
    print(linha)
    print(texto);
    print(linha)
    print()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante. ')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False;

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True;
            restaurante['status'] = not restaurante['status'];
#usou o not para mudar o estado entao n importa c esta true ou false ele vai mudar 
            mensagem = f'restaurante{nome_do_restaurante} foi ativado com sucesso' if restaurante['status']else f'O restaurante{nome_do_restaurante} foi desativado com sucesso.'
            print(mensagem)

        if not restaurante_encontrado:
            print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante'''

    exibir_subtitulo('Cadastro de novos restaurantes.')   
    nome_do_restaurante = input('Digite o nome do restaurante q deseja cadastrar: ')
    categoria= input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} que deseja cadastrar.')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria': categoria,'status': False}
    restaurantes.append(dados_do_restaurante)##aq foi criado primeiro um dicionario para organizar como vai ser colocado no dicionario principal ja com o status false pois ainda n foi ativo pra dps
    #pra dps jogar para a lista principal 
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes.')   
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categotia_restaurante = restaurante['categoria']
        status_restaurante =  'ativado' if restaurante['status'] else 'desativado'
        print(f'->{nome_restaurante.ljust(20)} | {categotia_restaurante.ljust(20)} | {status_restaurante}')# Alinha o texto à esquerda, completando com espaços em branco à direita até o tamanho especificado ljust()
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolida = int(input('Escolha uma opção: '));# o input por padrao retorna uma string entao foi posto int para retorna int
        if opcao_escolida == 1:
           cadastrar_novo_restaurante();
        elif opcao_escolida == 2:
            listar_restaurantes();
        elif opcao_escolida == 3:
           alterar_estado_do_restaurante();
        elif opcao_escolida == 4:
            finalizando_app();
        else:
            opcao_invalida();
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
