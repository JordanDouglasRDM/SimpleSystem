dadosCliente = []
dadosDocumento = []
maxCliente = 5
maxDocumentos = 30
class Cliente:
    codCliente = 0
    nome = ''
    fone = 0
class Documento:
    numeroDoc = 0
    codDoc = 0
    diaVencimento = 0
    diaPagamento = 0
    valor = 0.0
    juros = 0.0
def cadastroCliente():#1 att 04/11 - 17:23
    if len(dadosCliente) <= maxCliente:
        novoCliente = Cliente()
        newCliete = int(input('Informe o CÓDIGO do cliente: '))
        if existeCliente(newCliete) == False:
            novoCliente.codCliente = newCliete
            novoCliente.nome = input('Informe o NOME do cliente: ')
            novoCliente.fone = int(input('Informe o TELEFONE do cliente: '))#interessante utilizar expressão regular (Regex)
            dadosCliente.append(novoCliente)
        else:
            print('\nCódigo já existente, tente novamente.')
            return cadastroCliente() 
    else:
        print('\nNúmero máximo de clientes atingido!\n')
def relatorioClientes():#2 att 04/11 - 17:24
    print('\nCOD\tNOME\t\tTELEFONE')
    for i in range(len(dadosCliente)):
        print(f'{dadosCliente[i].codCliente:<8}{dadosCliente[i].nome[:14]:<16}{dadosCliente[i].fone:<10}')
def cadastroDocumento():#3 att 04/11 - 17:29
    if len(dadosDocumento) <= maxDocumentos:
        novoDocumento = Documento()
        codigoCliente = int(input('Informe o CÓDIGO do CLIENTE desse documento: '))
        if existeCliente(codigoCliente) == True:
            novoDocumento.codDoc = codigoCliente
            documento = int(input('Informe o NÚMERO do documento: '))
            if existeDocumento(documento) == False:
                novoDocumento.numeroDoc = documento
                novoDocumento.diaPagamento = input('Informe a DATA do pagamento: ')
                novoDocumento.diaVencimento = input('Informe a DATA do vencimento: ')
                novoDocumento.valor = int(input('Informe o VALOR do documento: '))
                juros = datas(novoDocumento.diaPagamento, novoDocumento.diaVencimento)
                if juros == 'maior':
                    novoDocumento.juros = novoDocumento.valor * 0.05
                dadosDocumento.append(novoDocumento)
            else:
                print('\nNúmero de documento já existe.')
                return
        else:
            print('\nCliente não encontrado.')
            return
    else:
        print('\nNúmero máximo de documento atingido!\n')
def relatorioDocumentos():#4 att 10/11 - 11:34
    print(f'\nTotal de documentos: {len(dadosDocumento)}')
    print('NÚMERO\tCÓDIGO\tPAGAMENTO    VENCIMENTO\t  VALOR\t      JÚROS')
    for i in range(len(dadosDocumento)):
        exibeDocumento(i)
    exibeMenu()
def excluiClientesNoDoc():#5
    numeroCliente = int(input('\nInforme o número do cliente a excluir: '))
    if existeCliente(numeroCliente): 
        for i in range(len(dadosDocumento)):
            if numeroCliente == dadosDocumento[i].codDoc:
                print('\nNão foi possível excluir esse cliente, pois existe documentos relacionados a ele.')
                return
        for j in range(len(dadosCliente)):
            if numeroCliente == dadosCliente[j].codCliente:
                busca_pop = j
        dadosCliente.pop(busca_pop)
    else:
        print('\nCliente não encontrado')
        excluiClientesNoDoc()
        return
    print(f'\nO cliente {numeroCliente} foi exluído!')
def excluiDocumentoNumero():#6
    busca = 0
    numero_doc = int(input('Informe o número do documento para exluir: '))
    if existeDocumento(numero_doc) == True:
        for i in range(len(dadosDocumento)):
            if numero_doc == dadosDocumento[i].numeroDoc:
                busca = i
        dadosDocumento.pop(busca)
        print(f'\nDocumento {numero_doc} excluído!')
    else:
        print('\nDocumento não encontrado.')
        excluiDocumentoNumero()
def excluiAllDocCliente():#7
    numeroCliente = int(input('Informe o número do cliente para excluir todos os documentos: '))
    documentosARemover = []
    for i in range(len(dadosDocumento)):
        if numeroCliente == dadosDocumento[i].codDoc:
            documentosARemover.append(dadosDocumento[i])
    if len(documentosARemover) == 0:
        print('\nCliente não possui documentos! ')
        return
    for i in range(len(documentosARemover)):
        dadosDocumento.remove(documentosARemover[i])
    print(f'\n{len(documentosARemover)} documento(s) encontrado(s) e excluído(s)!')
def excluiDocPeriodo():#8 ------Pela data de vencimento
    docAExluir = []
    inicio = input('Informe o dia inicial: ')
    if verificaData(inicio) == False:
        return
    fim = input('Informe o dia final: ')
    if verificaData(fim) == False:
        return
    if datas(inicio,fim) == 'maior':
        print('O dia inicial deve ser menor que o final')
    if datas(inicio,fim) == 'menor' or datas(inicio,fim) == 'igual' :
        for i in range(len(dadosDocumento)):
            if datas(dadosDocumento[i].diaVencimento,inicio) == 'maior' or datas(dadosDocumento[i].diaVencimento,inicio) == 'igual':
                if datas(dadosDocumento[i].diaVencimento,fim) == 'menor' or datas(dadosDocumento[i].diaVencimento,fim) == 'igual':
                    docAExluir.append(dadosDocumento[i])
        if len(docAExluir) == 0:
            return print('\nNão possui documentos nesse periodo.')
        opc = input(f'\n{len(docAExluir)} documentos foram encontrados. Deseja exclui-los? (s/n): ')
        if opc == 's':
            for i in range(len(docAExluir)):
                dadosDocumento.remove(docAExluir[i])
            print(f' Documentos excluídos.')
def alteraDadosCliente():#9 Alterar os dados do cliente (menos o código)
    cliente = int(input('Informe qual o cliente deseja alterar: '))
    if mostraCliente(cliente, True) == False:
        print('\nCliente não encontrado.')
        return
    posicaoCliente = 0
    for i in range(len(dadosCliente)):
        if cliente == dadosCliente[i].codCliente:
            posicaoCliente = i
    print('\nAlterar cadastro:')
    print('1.Nome')
    print('2.Telefone\n')
    opcao = int(input('Qual opção deseja? '))
    if opcao == 1:
        dadosCliente[posicaoCliente].nome = input('Informe um novo nome: ')
        print('\nNome Alterado com sucesso!')
    elif opcao == 2:
        dadosCliente[posicaoCliente].fone = input('Informe um novo telefone: ')
        print('\nTelfone Alterado com sucesso!')
def totalDocCliente():#10 Mostrar o total de documentos de determinado cliente.
    cliente = int(input('Informe o COD do cliente: '))
    if existeCliente(cliente):
        cont = 0
        for i in range(len(dadosDocumento)):
            if dadosDocumento[i].codDoc == cliente:
                cont += 1
        print(f'\nO cliente {cliente} possui {cont} documento(s).')
        return cont
    else:
        print('\nCliente não encontrado\n')
        return
def quantidadeDocPCliente(cliente):
    cont = 0
    for i in range(len(dadosDocumento)):
        if cliente == dadosDocumento[i].codDoc:
            cont += 1
    return cont
def mostraDocumentoPCliente():
    cliente = int(input('Informe o cliente que deseja consultar os documentos: '))
    if existeCliente(cliente):
        if quantidadeDocPCliente(cliente) > 0:
            print('\nNÚMERO\tCÓDIGO\tPAGAMENTO    VENCIMENTO\t  VALOR\t      JÚROS')
            for i in range(len(dadosDocumento)):
                if cliente == dadosDocumento[i].codDoc:
                    exibeDocumento(i)
        else:
            print('\nCLiente não possui documentos.')
    else:
        print('\nCliente não cadastrado\n')
        mostraDocumentoPCliente()
def exibeDocumento(posicao):
        print(f'{dadosDocumento[posicao].numeroDoc:<9}{dadosDocumento[posicao].codDoc:<7}{dadosDocumento[posicao].diaPagamento:<13}{dadosDocumento[posicao].diaVencimento:<12}R$ {dadosDocumento[posicao].valor:<9}R$ {dadosDocumento[posicao].juros:<9}')
def existeCliente(cliente):
    clientes = []
    for i in range(len(dadosCliente)):
        clientes.append(dadosCliente[i].codCliente)
    if cliente in clientes:
        return True
    return False
def existeDocumento(documento):
    documentos = []
    for i in range(len(dadosDocumento)):
        documentos.append(dadosDocumento[i].numeroDoc)
    if documento in documentos:
        return True
    return False
def mostraCliente(cliente,argumento):#mostrar dados do cliente pelo cod
    if argumento == False:
        cliente = int(input('Informe o COD do cliente: '))
    if existeCliente(cliente) ==  True:
        busca = 0
        for i in range(len(dadosCliente)):
            if dadosCliente[i].codCliente == cliente:
                busca = i
        print('\nCOD\tNOME\t\tTELEFONE')
        print(f'{dadosCliente[busca].codCliente:<8}{dadosCliente[busca].nome[:14]:<16}{dadosCliente[busca].fone:<10}')
    else:
        print('\nNão existe cliente cadastrado')
        return False
def limpaDados():
    apagaDoc = []
    apagaClit = []
    for i in range(len(dadosDocumento)):
        apagaDoc.append(dadosDocumento[i])
    for i in range(len(dadosCliente)):
        apagaClit.append(dadosCliente[i])
    for i in range(len(dadosDocumento)):
        dadosDocumento.remove(apagaDoc[i])
    for i in range(len(dadosCliente)):
        dadosCliente.remove(apagaClit[i])
def lerDados():#apaga vetor, pega o que está no arquivo e escreve no vetor
    limpaDados()
    arquivoCliente = open('dadosCliente.txt','r')
    arquivoDoc = open('dadosDocumentos.txt','r')
    for linha in arquivoCliente.readlines():
        cod, name, fone = linha.split(';')
        atualizaCliente = Cliente()
        atualizaCliente.codCliente = int(cod)
        atualizaCliente.nome = name
        atualizaCliente.fone = int(fone)
        dadosCliente.append(atualizaCliente)
    arquivoCliente.close
    for linha in arquivoDoc.readlines():
        nmDoc, codC, pagam, vencim, val, jur = linha.split(';')
        atualizaDocumento = Documento()
        atualizaDocumento.numeroDoc = int(nmDoc)
        atualizaDocumento.codDoc = int(codC)
        atualizaDocumento.diaPagamento = pagam
        atualizaDocumento.diaVencimento = vencim
        atualizaDocumento.valor = float(val)
        atualizaDocumento.juros = float(jur)
        dadosDocumento.append(atualizaDocumento)
    arquivoDoc.close
def salvarDados():
    arquivoCliente = open('dadosCliente.txt','w')
    arquivoDoc = open('dadosDocumentos.txt','w')
    for i in range(len(dadosCliente)):
        arquivoCliente.write(f'{dadosCliente[i].codCliente};{dadosCliente[i].nome};{dadosCliente[i].fone}\n')
    arquivoCliente.close
    for i in range(len(dadosDocumento)):
        arquivoDoc.write(f'{dadosDocumento[i].numeroDoc};{dadosDocumento[i].codDoc};{dadosDocumento[i].diaPagamento};{dadosDocumento[i].diaVencimento};{dadosDocumento[i].valor};{dadosDocumento[i].juros}\n')
    arquivoDoc.close
def quantidadeLinhasDoc():
    file = open('dadosCliente.txt','r') 
    cont = 0
    conteudo = file.read() 
    lista = conteudo.split("\n") 
    for i in lista: 
        if i: 
            cont += 1
    file.close
    return cont
def verificaData(data):
    data = data.split('/')
    if data[0] < '0' or data[0] > '31' or data[1] < '0' or data[1] > '12'  or data[2] < '0' or data[2] < '1850':
        print('\nVocê digitou uma data inválida')
        return False
def datas(data,data2):#pagamento/vencimento
    ###--------TESTE PARA TRATAR DATAS
    data = data.split('/')
    data2 = data2.split('/')
    maiorAno = data[2]
    maiorMes = data[1] 
    maiorDia = data[0]
    maiorData = data
    if maiorAno < data2[2]:
        maiorData = data2
    elif maiorAno == data2[2]:
        if maiorMes < data2[1]:
            maiorData = data2
        elif maiorMes == data2[1]:
            if maiorDia < data2[0]:
                maiorData = data2
            elif maiorDia == data2[0]:
                return 'igual'
    if maiorData == data2:
        return 'menor'
    return 'maior'
def opcoes(opcao):
    erroNoDoc = '\nNão existe documentos cadastrados.'
    if opcao == 1:
        cadastroCliente()
    if opcao == 2:
        relatorioClientes()
    elif opcao == 3:
        cadastroDocumento()
    elif opcao == 5:
        excluiClientesNoDoc()
    elif opcao == 7:
        if len(dadosDocumento) > 0:
                excluiAllDocCliente()
        else:
                print(erroNoDoc)
    elif opcao == 9:
        alteraDadosCliente()
    elif opcao == 10:
        if len(dadosDocumento) > 0:
            totalDocCliente()
        else:
            print(erroNoDoc)
    elif opcao == 12:
        mostraCliente(0,False)
    elif opcao == 4:
        relatorioDocumentos()
    elif opcao == 6:
        excluiDocumentoNumero()
    elif opcao == 8:
        excluiDocPeriodo()
    elif opcao == 11:
        mostraDocumentoPCliente()
def exibeMenu():
    print('\nMENU DE OPÇÕES: ')
    print('1.Cadastrar clientes\n2.Relatório de clientes\n3.Cadastrar documentos\n4.Relatório de documentos\n5.Excluir clientes sem documentos\n6.Excluir documentos individuais pelo número\n7.Excluir documentos por cliente\n8.Excluir documentos por período\n9.Alterar as informações dos clientes\n10.Mostrar o total de documentos de determinado cliente\n11.Consultar documentos pelo cliente\n12.Mostra cliente pelo COD')
    print('99.Sair sem salvar')
    print('00.Sair e salvar\n')
def validaOpcao(opcao):
    if opcao > 0 and opcao < 13 or opcao == 00 or opcao == 99:
        return True
    return False
def sair(metodo):#99 #00
    if metodo == 1:
        salvarDados()
        print('Salvo!\nVocê escolheu sair...')
        return False
    if metodo == 2:
        print('Alterações descartadas\nVocê escolheu sair...')
        return False
def main():
    linhas = quantidadeLinhasDoc()
    if linhas > 0:
        lerDados
    if  linhas == 0:
        print('\nNenhuma opção está disponível se não houver clientes cadastrados.\nPor isso, cadastre um cliente para continuar.\n')
        cadastroCliente()
        salvarDados()
    lerDados()
    exibeMenu()
    opcao = int(input('\nQual opção você deseja? '))
    while validaOpcao(opcao):
        exibeMenu()
        if opcao == 00:
            if sair(1) == False:
                break
        if opcao == 99:
            if sair(2) == False:
                break
        else:
            opcoes(opcao)
        opcao = int(input('\nQual opção você deseja? '))
    if validaOpcao(opcao) == False:
        print('\n\t\t\tOpcao inválida\n')
        main()
main()