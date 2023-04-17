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
            print(f'Nome da Disciplina: {registro[1]}')
         return 'cadastrado'
     else:
        return 'naocadastrado'
 except Exception as error:
     return (f'Ocorreu erro ao tentar consultar esta disciplina: Erro===>>> {error}')
def cadastrardisciplina(cd=0,nd=''):
 try:
     comandosql = conexao.cursor()
     #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
     comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({cd},"{nd}") ;')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     return 'Cadastro da disciplina realizado com sucesso !!!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível cadastrar esta disciplina !!!'
def alterardisciplina(cd=0, nomedisciplina=''):
 try:
     comandosql = conexao.cursor()
     #criando comando update para atulizar o nome da disciplina em questão
     comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc = {cd};')
     #método commit é responsável por REGRAVAR de fato o novo NOME DA DISCIPLINA disciplina na tabela
     conexao.commit()
     return 'Disciplina alterada com sucesso !!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível alterada esta disciplina'
def excluirdisciplina(cd=0):
 try:
     comandosql = conexao.cursor()
     #criando comando delete e concatenando o código da disciplina para ser escluída
     comandosql.execute(f'delete from disciplinas where codigodisc = {cd};')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     return 'Disciplina excluída com sucesso !!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível excluir esta disciplina'

#tabela professores
def mostratodasprof():
 # criando duas colunas para o grid que exibirá todas as diciplinas cadastradas
 grid = PrettyTable(['Registro', "Nome do professor", "Telefone", "Idade", "Salário"])
 try:
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
     else:
         print('Não existem professores cadastrados!!!')
 except Exception as erro:
     print(f'Ocorreu erro: {erro}')
def consultarprofessor(reg=0):
 try:
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
         return 'cadastrado'
     else:
        return 'naocadastrado'
 except Exception as error:
     return (f'Ocorreu erro ao tentar consultar este professor: Erro===>>> {error}')
def cadastrarprofessor(reg=0,np='',tp='',ip=0, sp=0.0):
 try:
     comandosql = conexao.cursor()
     #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
     comandosql.execute(f'insert into professores(registro, nomeprof, telefoneprof, idadeprof, salarioprof) values({reg},"{np}","{tp}", {ip}, {sp});')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     return 'Cadastro do professor realizado com sucesso !!!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível cadastrar este professor !!!'
def alterarprofessor(reg=0, nomeprofessor='', telefoneprof='', idadeprof=0, salarioprof=0.0):
 try:
     comandosql = conexao.cursor()
     #criando comando update para atulizar o nome da disciplina em questão
     comandosql.execute(f'Update professores SET nomeprof="{nomeprofessor}", telefoneprof="{telefoneprof}", idadeprof="{idadeprof}", salarioprof="{salarioprof}" where registro = {reg};')
     #método commit é responsável por REGRAVAR de fato o novo nome do professor disciplina na tabela
     conexao.commit()
     return 'Professor alterado com sucesso !!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível alterar este professor'
def excluirprofessor(reg=0):
 try:
     comandosql = conexao.cursor()
     #criando comando delete e concatenando o código da disciplina para ser escluída
     comandosql.execute(f'delete from professores where registro = {reg};')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     return 'Professor excluído com sucesso !!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível excluir este professor'

#TABELA  DISC X PROF
def mostratodasdiscxprof():
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
     else:
         print('Não existem cadastros!!!')
 except Exception as erro:
     print(f'Ocorreu erro: {erro}')
def consultardiscxprof(cod=0):
 try:
     comandosql = conexao.cursor()
     comandosql.execute(f'select * from professores where codigodisciplinanocurso = {cod};')
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
         return 'cadastrado'
     else:
        return 'naocadastrado'
 except Exception as error:
     return (f'Ocorreu erro ao tentar consultar esta tabela: Erro===>>> {error}')
def cadastrardiscxprof(cod=0,coddisc=0,codprof=0,curso=0, cargaHoraria=0, anoLetivo=0):
 try:
     comandosql = conexao.cursor()
     #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
     comandosql.execute(f'insert into disciplinasxprofessores(codigodisciplinanocurso, coddisciplina, codprofessor, curso, anoletivo) values({cod},{coddisc}, {codprof}, {curso}, {cargaHoraria}, {anoLetivo});')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     return 'Cadastro da tabela realizado com sucesso !!!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível cadastrar este registro na tabela !!!'
def alterardiscxprof(cod=0,coddisc=0,codprof=0,curso=0, cargaHoraria=0, anoLetivo=0):
 try:
     comandosql = conexao.cursor()
     #criando comando update para atulizar o nome da disciplina em questão
     comandosql.execute(f'Update disciplinasxprofessores SET coddisciplina={coddisc}, codprofessor={codprof}, curso={curso}, cargahoraria={cargaHoraria}, anoletivo{anoLetivo} where codigodisciplinanocurso = {cod};')
     #método commit é responsável por REGRAVAR de fato o novo nome do professor disciplina na tabela
     conexao.commit()
     return 'Tabela alterada com sucesso !!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível alterar esta tabela'
def excluirdiscxprof(cod=0):
 try:
     comandosql = conexao.cursor()
     #criando comando delete e concatenando o código da disciplina para ser escluída
     comandosql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocruso = {cod};')
     #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
     conexao.commit()
     return 'registro excluído com sucesso !!! '
 except Exception as erro :
     print(f'Erro: {erro}')
     return 'Não foi possível excluir este registro'


#modulo principal=============================================================================
while True:
    resposta = int(input('Digite: 1-tabela disciplinas | 2- tabela professores | 3-tabela disciplinas X professores | 4-sair do programa: '))

    #TABELA DISCIPLINAS
    if resposta == 1:
        if abrebanco() == 1:
             print('='*80)
             print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS'))
             print('='*80)
             while True:
                 resps = input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar uma disciplina \n 2-cadastrar uma disciplina \n 3-alterar o nome de uma disciplina \n 4-excluir uma disciplina \n 5-sair da tabela: ')
                 if resps.isnumeric():
                     resps = int(resps)
                     break

             #SELECT ALL====
             if resps == 0:
                 mostratodasdisc()

             #SELECT ONE====
             elif resps == 1:
                 while True:
                     codigodisc = input('Digite o código da disciplina: ')
                     if codigodisc.isnumeric():
                         codigodisc = int(codigodisc)
                         break
                 if consultardisciplina(codigodisc) == 'cadastrado':
                     print()
                 elif consultardisciplina(codigodisc) == 'naocadastrado':
                    print('Disciplina não cadastrada')

             #CADASTRAR====
             if resps == 2:
                 while True:
                     codigodisc = input('Digite o código da disciplina: ')
                     if codigodisc.isnumeric():
                         codigodisc = int(codigodisc)
                         break
                 nomedisciplina = input('Nome da Disciplina: ')
                 msg = cadastrardisciplina(codigodisc, nomedisciplina)
                 print(msg)

             #ALTERAR====
             if resps == 3:
                 print('Atenção: Código da disciplina não pode ser alterado: ')
                 while True:
                     codigodisc = input('Digite o código da disciplina: ')
                     if codigodisc.isnumeric():
                         codigodisc = int(codigodisc)
                         break
                 nomedisciplina = input('Informe novo nome da disciplina: ')
                 msg = alterardisciplina(codigodisc, nomedisciplina)
                 print(msg)

             #EXCLUIR====
             elif resps == 4:
                 while True:
                     codigodisc = input('Digite o código da disciplina: ')
                     if codigodisc.isnumeric():
                         codigodisc = int(codigodisc)
                         break
                 confirma = input('Confirme a exclusão S-SIM OU N-NÃO: ')
                 while confirma != 'S' and confirma != 'N': confirma = input('Digite S-SIM OU N-NÃO: ')
                 msg = excluirdisciplina(codigodisc)
                 print (msg)

             #SAIR====
             elif resps == 5:
                 continue

             print('\n\n')
             print('='*80)
        else:
            print('Alguma falha ocorreu na conexão com o bando de dados.')

    #TABELA PROFESSORES
    elif resposta == 2:
        if abrebanco() == 1:
            print('=' * 80)
            print('{:^80}'.format('SISTEMA UNIVAP - PROFESSORES'))
            print('=' * 80)
            while True:
                resps = input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar um professor \n 2-cadastrar um professor \n 3-alterar um professor \n 4-excluir um professor \n 5-sair da tabela: ')
                if resps.isnumeric():
                    resps = int(resps)
                    break

            # SELECT ALL====
            if resps == 0:
                mostratodasprof()

            # SELECT ONE====
            elif resps == 1:
                while True:
                    registro = input('Digite o código do professor: ')
                    if registro.isnumeric():
                        registro = int(registro)
                        break
                if consultarprofessor(registro) == 'cadastrado':
                    print()
                elif consultarprofessor(registro) == 'naocadastrado':
                    print('Professor não cadastrado')

            # CADASTRAR====
            if resps == 2:
                while True:
                    registro = input('Digite o código do professor: ')
                    if registro.isnumeric():
                        registro = int(registro)
                        break
                nomeprofessor = input('Nome do professor: ')
                telefoneprof = input('telefone: ')
                idadeprof = input('idade: ')
                salarioprof = input('salário: ')
                msg = cadastrarprofessor(registro, nomeprofessor, telefoneprof, idadeprof, salarioprof)
                print(msg)

            # ALTERAR====
            if resps == 3:
                print('Atenção: Código do professor não pode ser alterado: ')
                while True:
                    registro = input('Digite o código do professor: ')
                    if registro.isnumeric():
                        registro = int(registro)
                        break
                nomeprofessor = input('Nome do professor: ')
                telefoneprof = input('telefone: ')
                idadeprof = input('idade: ')
                salarioprof = input('salário: ')
                msg = alterarprofessor(registro, nomeprofessor, telefoneprof, idadeprof, salarioprof)
                print(msg)

            # EXCLUIR====
            elif resps == 4:
                while True:
                    registro = input('Digite o código do professor: ')
                    if registro.isnumeric():
                        registro = int(registro)
                        break
                confirma = input('Confirme a exclusão S-SIM OU N-NÃO: ')
                while confirma != 'S' and confirma != 'N': confirma = input('Digite S-SIM OU N-NÃO: ')
                msg = excluirprofessor(registro)
                print(msg)

            # SAIR====
            elif resps == 5:
                continue

            print('\n\n')
            print('=' * 80)
        else:
            print('Alguma falha ocorreu na conexão com o bando de dados.')

    #TABELA DISCIPLINAS X PROFESSORES
    elif resposta == 3:
        if abrebanco() == 1:
            print('=' * 80)
            print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS X PROFESSORES'))
            print('=' * 80)
            while True:
                resps = input('Digite a ação desejada:\n 0-selecionar todos \n 1-selecionar registro \n 2-cadastrar novo registro \n 3-alterar um registro \n 4-excluir um registro \n 5-sair da tabela: ')
                if resps.isnumeric():
                    resps = int(resps)
                    break

            # SELECT ALL====
            if resps == 0:
                mostratodasdiscxprof()

            # SELECT ONE====
            elif resps == 1:
                while True:
                    cod = input('Digite o código do registro: ')
                    if cod.isnumeric():
                        cod = int(cod)
                        break
                if consultardiscxprof(cod) == 'cadastrado':
                    print()
                elif consultardiscxprof(cod) == 'naocadastrado':
                    print('registro não está cadastrado')

            # CADASTRAR====
            if resps == 2:
                while True:
                    cod = input('Digite o código do registro: ')
                    if cod.isnumeric():
                        cod = int(cod)
                        break
                coddisc = input('código disciplina: ')
                codprof = input('código professor: ')
                curso = input('curso: ')
                cargahoraria = input('carga horária: ')
                anoletivo = input('ano letivo: ')
                msg = cadastrardiscxprof(cod, coddisc, codprof, curso, cargahoraria, anoletivo)
                print(msg)

            # ALTERAR====
            if resps == 3:
                print('Atenção: Código do professor não pode ser alterado: ')
                while True:
                    cod = input('Digite o código do registro: ')
                    if cod.isnumeric():
                        cod = int(cod)
                        break
                coddisc = input('código disciplina: ')
                codprof = input('código professor: ')
                curso = input('curso: ')
                cargahoraria = input('carga horária: ')
                anoletivo = input('ano letivo: ')
                msg = alterardiscxprof(cod, coddisc, codprof, curso, cargahoraria, anoletivo)
                print(msg)

            # EXCLUIR====
            elif resps == 4:
                while True:
                    cod = input('Digite o código do registro: ')
                    if cod.isnumeric():
                        cod = int(cod)
                        break
                confirma = input('Confirme a exclusão S-SIM OU N-NÃO: ')
                while confirma != 'S' and confirma != 'N': confirma = input('Digite S-SIM OU N-NÃO: ')
                msg = excluirdiscxprof(cod)
                print(msg)

            # SAIR====
            elif resps == 5:
                continue

            print('\n\n')
            print('=' * 80)
        else:
            print('Alguma falha ocorreu na conexão com o bando de dados.')

    #SAIR
    elif resposta == 4:
        break

    #ERRO
    else:
        print('Digite um número válido')
