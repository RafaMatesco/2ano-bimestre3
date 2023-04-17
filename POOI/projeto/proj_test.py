from prettytable import PrettyTable
import mysql.connector


#tabela disciplinas
def abrebanco():
 try:
     print()
     #criando um objeto para conexão ao banco de dados
     #Devemos indicar em :
     # host = Servidor ou IP(caso esteja numa rede),
     # database = nome do banco de dados criado no workbenck
     # user = nome do usuário definido no momento de criação do banco de dados
     # password = senha de acesso do banco de dados
     global conexao
     conexao = mysql.connector.Connect(host='localhost',database='univap',user='root', password='')
     # testando se estamos conectado ao banco de dados
     if conexao.is_connected():
         informacaobanco = conexao.get_server_info()
         print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
         # criando objeto cursor, responsável para trabalharmos com registros retornados pela tabela fisica
         global comandosql
         comandosql = conexao.cursor()
         # Criando uma QUERY para mostrar as informações do banco de dados ao qual nosconectamos
         comandosql.execute('select database();')
         # usando método fetchone para buscar um dado do banco de dados e armazenálo na variável nomebanco
         nomebanco = comandosql.fetchone()
         print(f'Banco de dados acessado = {nomebanco}')
         print()
         return 1

     else:
         print('Conexão não realizada com banco')
         return 0
 except Exception as erro:
     print(f'Erro : {erro}')
     return 0
def mostratodasdisc():
 # criando duas colunas para o grid que exibirá todas as diciplinas cadastradas
 grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
 try:
     print('\n')
     comandosql = conexao.cursor()
     # repare que NÃO USEI A CLÁUSULA WHERE, ou seja, todas as disciplinas gravadas serão consultadas
     comandosql.execute(f'select * from disciplinas;')
     # O MÉTODO fetchall() retornará todos os registros filtrados (um ou mais registros) pelo comando select
     tabela = comandosql.fetchall()
     # O método rowcount conta quantos registros foram filtrados, caso tenha registro filtrado entra no if
     if comandosql.rowcount > 0:
     # se existir pelo menos uma disciplina na tabela temporária, mostre-as no grid
         for registro in tabela:
             # criando as linhas do grid com os registros lidos da tabela temporária Mostrando todas as disciplinas
             grid.add_row([registro[0], registro[1]])
         print(grid)
         print('\n')
     else:
         print('Não existem disciplinas cadastradas!!!')
 except Exception as erro:
     print(f'Ocorreu erro: {erro}')
def consultardisciplina(cd=0):
 try:
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from disciplinas where codigodisc = {cd};')


     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount > 0:
         # se existir pelo menos uma disciplina na tabela temporária, mostre os dados da coluna 1
         for registro in tabela:
            print(f'Nome da Disciplina: {registro[1]} ')
         return 'cadastrado'
     else:
        return 'naocadastrado'
 except Exception as error:
     return (f'Ocorreu erro ao tentar consultar esta disciplina: Erro===>>> {error}')
def cadastrardisciplina(cd=0,nd=''):
 try:
     print('\n')
     comandosql = conexao.cursor()
     #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
     comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({cd},"{nd}") ;')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     print('\n')
     return 'Cadastro da disciplina realizado com sucesso !!!! '

 except Exception as erro :
     print('\n')
     return 'não foi possivel cadastrar disciplina'
def alterardisciplina(cd=0, nomedisciplina=''):
 try:
     print('\n')
     comandosql = conexao.cursor()
     #criando comando update para atulizar o nome da disciplina em questão
     comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc = {cd};')
     #método commit é responsável por REGRAVAR de fato o novo NOME DA DISCIPLINA disciplina na tabela
     conexao.commit()
     print('\n')
     return 'Disciplina alterada com sucesso !!! '
 except Exception as erro :
     print('\n')
     return 'Não foi possível alterada esta disciplina'
def excluirdisciplina(cd=0):
 try:
     print('\n')
     comandosql = conexao.cursor()
     #criando comando delete e concatenando o código da disciplina para ser escluída
     comandosql.execute(f'delete from disciplinas where codigodisc = {cd};')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     print('\n')
     return 'Disciplina excluída com sucesso !!! '
 except Exception as erro :
     print('\n')
     return 'Não foi possível excluir esta disciplina'

#tabela professores
def mostratodasprof():

 # criando duas colunas para o grid que exibirá todas as diciplinas cadastradas
 grid = PrettyTable(['Registro', "Nome do professor", "Telefone", "Idade", "Salário"])
 try:
     print('\n')
     comandosql = conexao.cursor()
     # repare que NÃO USEI A CLÁUSULA WHERE, ou seja, todas as disciplinas gravadas serão consultadas
     comandosql.execute(f'select * from professores;')
     # O MÉTODO fetchall() retornará todos os registros filtrados (um ou mais registros) pelo comando select
     tabela = comandosql.fetchall()
     # O método rowcount conta quantos registros foram filtrados, caso tenha registro filtrado entra no if
     if comandosql.rowcount > 0:
     # se existir pelo menos uma disciplina na tabela temporária, mostre-as no grid
         for registro in tabela:
             # criando as linhas do grid com os registros lidos da tabela temporária Mostrando todas as disciplinas
             grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4]])
         print(grid)
         print('\n')
     else:
         print('Não existem professores cadastrados!!!')
 except Exception as erro:
     print(f'Ocorreu erro: {erro}')
def consultarprofessor(reg=0):
 try:
     print('\n')
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from professores where registro = {reg};')
     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount > 0:
         # se existir pelo menos uma disciplina na tabela temporária, mostre os dados da coluna 1

         for registro in tabela:
            print(f'Nome do professor: {registro[1]}')
            print(f'telefone: {registro[2]}')
            print(f'Idade: {registro[3]}')
            print(f'Salário: {registro[4]}')
         print('\n')
         return 'cadastrado'
     else:
        return 'naocadastrado'
 except Exception as error:
     return (f'Ocorreu erro ao tentar consultar este professor')
def cadastrarprofessor(reg=0,np='',tp='',ip=0, sp=0.0):
 try:
     print('\n')
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from professores where nomeprof = "{np}";')
     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount > 1:
         return 'já existe professor com esse nome'
     # se existir pelo menos uma disciplina na tabela temporária, mostre os dados da coluna 1
     comandosql = conexao.cursor()
     #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
     comandosql.execute(f'insert into professores(registro, nomeprof, telefoneprof, idadeprof, salarioprof) values({reg},"{np}","{tp}", {ip}, {sp});')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     tabela=comandosql.fetchall()

    #2
     print('\n')
     return 'Cadastro do professor realizado com sucesso !!!! '
 except Exception as erro :
     print(erro)
     return 'Não foi possível cadastrar este professor !!!'
def alterarprofessor(reg=0, nomeprofessor='', telefoneprof='', idadeprof=0, salarioprof=0.0):
 try:
     print('\n')
     comandosql = conexao.cursor()
     #criando comando update para atulizar o nome da disciplina em questão
     comandosql.execute(f'Update professores SET nomeprof="{nomeprofessor}", telefoneprof="{telefoneprof}", idadeprof="{idadeprof}", salarioprof="{salarioprof}" where registro = {reg};')
     #método commit é responsável por REGRAVAR de fato o novo nome do professor disciplina na tabela
     conexao.commit()
     print('\n')
     return 'Professor alterado com sucesso !!! '
 except Exception as erro :

     return 'Não foi possível alterar este professor'
def excluirprofessor(reg=0):
 try:
     print('\n')
     comandosql = conexao.cursor()
     #criando comando delete e concatenando o código da disciplina para ser escluída
     comandosql.execute(f'delete from professores where registro = {reg};')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     print('\n')
     return 'Professor excluído com sucesso !!! '
 except Exception as erro :

     return 'Não foi possível excluir este professor'

#TABELA  DISC X PROF
def mostratodasdiscxprof():
 print('\n')
 # criando duas colunas para o grid que exibirá todas as diciplinas cadastradas
 grid = PrettyTable(['Código', "Cód. Disc.", "Cód. prof.", "Curso", "Carga horária", "Ano letivo"])
 try:
     comandosql = conexao.cursor()
     # repare que NÃO USEI A CLÁUSULA WHERE, ou seja, todas as disciplinas gravadas serão consultadas
     comandosql.execute(f'select * from disciplinasxprofessores;')
     # O MÉTODO fetchall() retornará todos os registros filtrados (um ou mais registros) pelo comando select
     tabela = comandosql.fetchall()
     # O método rowcount conta quantos registros foram filtrados, caso tenha registro filtrado entra no if
     if comandosql.rowcount > 0:
     # se existir pelo menos uma disciplina na tabela temporária, mostre-as no grid
         for registro in tabela:
             # criando as linhas do grid com os registros lidos da tabela temporária Mostrando todas as disciplinas
             grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]])
         print(grid)
         print('\n')
     else:
         print('Não existem cadastros!!!')
 except Exception as erro:
     print(f'Ocorreu erro')
def consultardiscxprof(cod=0):
 print('\n')
 try:
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from disciplinasxprofessores where codigodisciplinanocurso = {cod};')
     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount > 0:
         # se existir pelo menos uma disciplina na tabela temporária, mostre os dados da coluna 1
         for registro in tabela:
            print(f'código disciplina: {registro[1]}')
            print(f'código professor: {registro[2]}')
            print(f'curso: {registro[3]}')
            print(f'carga horária: {registro[4]}')
            print(f'ano letivo: {registro[5]}')
         print('\n')
         return 'cadastrado'
     else:
        return 'naocadastrado'
 except Exception as error:



     return (f'Ocorreu erro ao tentar consultar esta tabela')
def cadastrardiscxprof(cod=0,coddisc=0,codprof=0,curso=0, cargaHoraria=0, anoLetivo=0):
 print('\n')
 try:
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from disciplinas where codigodisc = {coddisc};')

     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount == 0:
         return 'disciplina não existe'

     comandosql = conexao.cursor()
     comandosql.execute(f'select * from professores where registro = {codprof};')

     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount == 0:
         return 'professor não existe'

     comandosql = conexao.cursor()
     #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
     comandosql.execute(f'insert into disciplinasxprofessores(codigodisciplinanocurso, coddisciplina, codprofessor, curso,cargahoraria, anoletivo) values({cod},{coddisc}, {codprof}, {curso}, {cargaHoraria}, {anoLetivo});')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     print('\n')
     return 'Cadastro da tabela realizado com sucesso !!!! '
 except Exception as erro :

     return 'Não foi possível cadastrar este registro na tabela !!!'
def alterardiscxprof(cod=0,coddisc=0,codprof=0,curso=0, cargaHoraria=0, anoLetivo=0):
 print('\n')
 try:
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from disciplinas where codigodisc = {coddisc};')

     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount == 0:
         return'disciplina não existe'

     comandosql = conexao.cursor()
     comandosql.execute(f'select * from professores where registro = {codprof};')

     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount == 0:
         return 'professor não existe'

     comandosql = conexao.cursor()
     comandosql.execute(f'select * from disciplinasxprofessores where codigodisciplinanocurso = {cod};')
     tabela = comandosql.fetchall()
     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     if comandosql.rowcount == 0:
         return 'registro não existe'

     comandosql = conexao.cursor()
     #criando comando update para atulizar o nome da disciplina em questão
     comandosql.execute(f'Update disciplinasxprofessores SET coddisciplina = {coddisc}, codprofessor = {codprof}, curso = {curso}, cargahoraria = {cargaHoraria}, anoletivo = {anoLetivo} where codigodisciplinanocurso = {cod};')
     #método commit é responsável por REGRAVAR de fato o novo nome do professor disciplina na tabela



     # verivificando quanto registros de disciplinas de código igual ao digitado
     # filtrados pelo select foram guardados na tabela temporária
     print('\n')
     return 'Tabela alterada com sucesso !!! '

 except Exception as erro :

     return 'Não foi possível alterar esta tabela'
def excluirdiscxprof(cod=0):
 print('\n')
 try:
     comandosql = conexao.cursor()
     #criando comando delete e concatenando o código da disciplina para ser escluída
     comandosql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocurso = {cod};')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     print('\n')
     return 'registro excluído com sucesso !!! '
 except Exception as erro :

     return 'Não foi possível excluir este registro'


#modulo principal=============================================================================
while True:
    try:
        resposta = int(input('Digite: 1-tabela disciplinas | 2- tabela professores | 3-tabela disciplinas X professores | 4-sair do programa: '))
    except:
        resposta = int(input('Digite: 1-tabela disciplinas | 2- tabela professores | 3-tabela disciplinas X professores | 4-sair do programa: '))
        while resposta<1 or resposta>4:
            resposta = int(input(
                'Digite: 1-tabela disciplinas | 2- tabela professores | 3-tabela disciplinas X professores | 4-sair do programa: '))
    #TABELA DISCIPLINAS
    if resposta == 1:
        if abrebanco() == 1:
             print('='*80)
             print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS'))
             print('='*80)
             while True:
                 try:
                    resps = int(input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar uma disciplina \n 2-cadastrar uma disciplina \n 3-alterar o nome de uma disciplina \n 4-excluir uma disciplina \n 5-sair da tabela: '))
                 except:
                     resps = int(input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar uma disciplina \n 2-cadastrar uma disciplina \n 3-alterar o nome de uma disciplina \n 4-excluir uma disciplina \n 5-sair da tabela: '))

                     while (resps < 0) or (resps > 5):
                        resps = int(input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar uma disciplina \n 2-cadastrar uma disciplina \n 3-alterar o nome de uma disciplina \n 4-excluir uma disciplina \n 5-sair da tabela: '))

                 print('\n\n')
             #SELECT ALL====
                 if resps == 0:
                     mostratodasdisc()

        #SELECT ONE====
                 elif resps == 1:
                    while True:
                        try:
                            codigodisc = int(input('Digite o código da disciplina: '))
                        except:
                            codigodisc = int(input('Digite o código da disciplina: '))


                        if consultardisciplina(codigodisc) == 'cadastrado':
                            print()
                        elif consultardisciplina(codigodisc) == 'naocadastrado':
                            print('Disciplina não cadastrada')
                        break
                    print('\n')

             #CADASTRAR====
                 if resps == 2:
                  while True:
                        try:
                            codigodisc = int(input('Digite o código da disciplina: '))
                        except:
                            codigodisc = int(input('Digite o código da disciplina: '))



                        nomedisciplina = input('Nome da Disciplina: ')

                        msg = cadastrardisciplina(codigodisc, nomedisciplina)
                        print(msg)
                        break
                  print('\n')
             #ALTERAR====
                 if resps == 3:
                    print('Atenção: Código da disciplina não pode ser alterado: ')
                    while True:
                        try:
                            codigodisc = int(input('Digite o código da disciplina: '))
                        except:
                            codigodisc = int(input('Digite o código da disciplina: '))



                        nomedisciplina = input('Informe novo nome da disciplina: ')

                        msg = alterardisciplina(codigodisc, nomedisciplina)
                        print(msg)
                        break
                    print('\n')
             #EXCLUIR====
                 elif resps == 4:
                    while True:
                     try:
                        codigodisc = int(input('Digite o código da disciplina: '))
                     except:
                         codigodisc = int(input('Digite o código da disciplina: '))



                     confirma = input('Confirme a exclusão S-SIM OU N-NÃO: ')

                     while confirma != 'S' and confirma != 'N': confirma = input('Digite S-SIM OU N-NÃO: ')
                     msg = excluirdisciplina(codigodisc)
                     print (msg)
                     break

        #SAIR====
                 elif resps == 5:
                     print('\n')
                     print('='*80)
                     break
                 print('\n')


    #TABELA PROFESSORES
    elif resposta == 2:
        if abrebanco() == 1:
            print('=' * 80)
            print('{:^80}'.format('SISTEMA UNIVAP - PROFESSORES'))
            print('=' * 80)
        while True:
            try:
                resps = int(input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar um professor \n 2-cadastrar um professor \n 3-alterar o nome de um professor \n 4-excluir um professor \n 5-sair da tabela: '))
            except:
                resps = int(input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar um professor \n 2-cadastrar um professor \n 3-alterar o nome de um professor \n 4-excluir um professor \n 5-sair da tabela: '))

                while (resps < 0) or (resps > 5):
                    try:
                        resps = int(input(
                            'Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar um professor \n 2-cadastrar um professor \n 3-alterar o nome de um professor \n 4-excluir um professor \n 5-sair da tabela: '))
                    except:
                        resps = int(input(
                            'Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar um professor \n 2-cadastrar um professor \n 3-alterar o nome de um professor \n 4-excluir um professor \n 5-sair da tabela: '))
            print('\n')
            # SELECT ALL====
            if resps == 0:
                mostratodasprof()

        # SELECT ONE====
            elif resps == 1:
                while True:
                    try:
                        registro = int(input('Digite o código do professor: '))
                    except:
                        registro = int(input('Digite o código do professor: '))

                    if consultarprofessor(registro) == 'cadastrado':
                        print('')
                    elif consultarprofessor(registro) == 'naocadastrado':
                        print('Professor não cadastrado')
                    break
            # CADASTRAR====
            if resps == 2:
                while True:
                    try:
                        registro = int(input('Digite o código do professor: '))
                    except:
                        registro = int(input('Digite o código do professor: '))

                    try:
                         nomeprofessor = input('Nome do professor: ')
                         telefoneprof = input('telefone: ')
                         idadeprof = int(input('idade: '))
                         salarioprof = int(input('salário: '))
                    except:
                         nomeprofessor = input('Nome do professor: ')
                         telefoneprof = input('telefone: ')
                         idadeprof = int(input('idade: '))
                         salarioprof = int(input('salário: '))

                    while idadeprof > 100:
                        try:
                            idadeprof = int(input('idade: '))
                        except:
                            idadeprof = int(input('idade: '))
                    msg = cadastrarprofessor(registro, nomeprofessor, telefoneprof, idadeprof, salarioprof)
                    print(msg)
                    break

            # ALTERAR====
            if resps == 3:
                print('Atenção: Código do professor não pode ser alterado: ')
                while True:
                    try:
                        registro = int(input('Digite o código do professor: '))
                    except:
                        registro = int(input('Digite o código do professor: '))

                    try:
                        nomeprofessor = input('Nome do professor: ')
                        telefoneprof = input('telefone: ')
                        idadeprof = int(input('idade: '))
                        salarioprof = float(input('salário: '))
                    except:
                        nomeprofessor = input('Nome do professor: ')
                        telefoneprof = input('telefone: ')
                        idadeprof = int(input('idade: '))
                        salarioprof = float(input('salário: '))

                    while idadeprof > 100:
                        try:
                            idadeprof = int(input('idade: '))
                        except:
                            idadeprof = int(input('idade: '))
                    msg = alterarprofessor(registro, nomeprofessor, telefoneprof, idadeprof, salarioprof)
                    print(msg)
                    break

            # EXCLUIR====
            elif resps == 4:
                while True:
                    try:
                        registro = int(input('Digite o código do professor: '))
                    except:
                        registro = int(input('Digite o código do professor: '))

                    confirma = input('Confirme a exclusão S-SIM OU N-NÃO: ')

                    while confirma != 'S' and confirma != 'N': confirma = input('Digite S-SIM OU N-NÃO: ')
                    msg = excluirprofessor(registro)
                    print(msg)
                    break

        # SAIR====
            elif resps == 5:
                print('=' * 80)
                break




    #TABELA DISCIPLINAS X PROFESSORES
    elif resposta == 3:
        if abrebanco() == 1:
            print('=' * 80)
            print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS X PROFESSORES'))
            print('=' * 80)
            while True:
                try:
                    resps = int(input('Digite a ação desejada:\n 0-sair da tabela \n 1-selecionar registro \n 2-cadastrar novo registro \n 3-alterar um registro \n 4-excluir um registro \n 5-selecionar todos: '))
                except:
                    resps = int(input('Digite a ação desejada:\n 0-sair da tabela \n 1-selecionar registro \n 2-cadastrar novo registro \n 3-alterar um registro \n 4-excluir um registro \n 5-selecionar todos: '))


                while (resps < 0) or resps > 6:
                    resps = int(input('Digite a ação desejada:\n 0-sair da tabela \n 1-selecionar registro \n 2-cadastrar novo registro \n 3-alterar um registro \n 4-excluir um registro \n 5-selecionar todos: '))
                print('\n')
            # SELECT ALL====
                if resps == 5:
                    mostratodasdiscxprof()

            # SELECT ONE====
                elif resps == 1:
                    while True:
                        try:
                            cod = int(input('Digite o código do registro: '))
                        except:
                            cod = int(input('Digite o código do registro: '))

                        if consultardiscxprof(cod) == 'cadastrado':
                            print()
                        elif consultardiscxprof(cod) == 'naocadastrado':
                            print('registro não está cadastrado')
                        break
            # CADASTRAR====
                if resps == 2:
                    while True:
                        confirmar = input('Quer verificar todos os professores e disciplinas antes? S-SIM OU N-NÃO: ')
                        while confirmar != 'S' and confirmar != 'N':
                             confirmar = input('Digite S-SIM OU N-NÃO: ')
                        if confirmar == 'S':
                            mostratodasdisc()
                            mostratodasprof()

                        try:
                            cod = int(input('Digite o código do registro: '))
                        except:
                            cod = int(input('Digite o código do registro: '))

                        try:
                            coddisc = int(input('código disciplina: '))
                            codprof = int(input('código professor: '))
                            curso = int(input('curso: '))
                            cargahoraria = int(input('carga horária: '))
                            anoletivo = int(input('ano letivo: '))
                        except:
                            coddisc = int(input('código disciplina: '))
                            codprof = int(input('código professor: '))
                            curso = int(input('curso: '))
                            cargahoraria = int(input('carga horária: '))
                            anoletivo = int(input('ano letivo: '))





                        msg = cadastrardiscxprof(cod, coddisc, codprof, curso, cargahoraria, anoletivo)
                        print(msg)
                        break
            # ALTERAR====
                if resps == 3:
                    print('Atenção: Código do professor não pode ser alterado: ')
                    while True:
                        try:
                           cod = int(input('Digite o código do registro: '))
                        except:
                            cod = int(input('Digite o código do registro: '))

                        try:
                            coddisc = int(input('código disciplina: '))
                            codprof = int(input('código professor: '))
                            curso = int(input('curso: '))
                            cargahoraria = int(input('carga horária: '))
                            anoletivo = int(input('ano letivo: '))
                        except:
                            coddisc = int(input('código disciplina: '))
                            codprof = int(input('código professor: '))
                            curso = int(input('curso: '))
                            cargahoraria = int(input('carga horária: '))
                            anoletivo = int(input('ano letivo: '))
                        msg = alterardiscxprof(cod, coddisc, codprof, curso, cargahoraria, anoletivo)
                        print(msg)
                        break

                # EXCLUIR====
                elif resps == 4:
                    while True:
                        try:
                            cod = int(input('Digite o código do registro: '))
                        except:
                            cod = int(input('Digite o código do registro: '))

                        confirma = input('Confirme a exclusão S-SIM OU N-NÃO: ')
                        while confirma != 'S' and confirma != 'N': confirma = input('Digite S-SIM OU N-NÃO: ')
                        msg = excluirdiscxprof(cod)
                        print(msg)
                        break

                # SAIR====
                elif resps == 0:
                    break

            print('\n\n')
            print('=' * 80)
        else:
            print('Alguma falha ocorreu na conexão com o bando de dados.')

    #SAIR
    elif resposta == 4:
        print('\n\n')
        print('=' * 80)
        print('obrigado por testar o programa')
        break

    #ERRO
    else:
        print('Digite um número válido')
