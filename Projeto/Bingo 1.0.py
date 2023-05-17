def header(cartSelecionadas):
    print('-='*20)
    print(f'{"BINGO LITE":^40}')
    print('-='*20)


def lerCartelas(arquivo):
    tamanho = len(arquivo.readlines())
    cartelas = [0]*tamanho
    i = 0
    arquivo.seek(0,0)
    while True:
        linha = arquivo.readline().rstrip()
        if linha == '':
            break
        else:
            t = linha.split(',')
            cartelas[i] = (t)
            i += 1
    return cartelas

    
def sorteio(cartelas):
    sorteados = [0] * 4
    from random import randint
    for i in range(4):
        aleatorio = randint(0,len(cartelas)-1)
        if cartelas[aleatorio] not in sorteados:
            sorteados[i] = cartelas[aleatorio]
        else:
            aleatorio = randint(0,len(cartelas)-1)
            sorteados[i] = cartelas[aleatorio]      
    return sorteados
        

def numerosSorteados(cartSelec,repetidos):
    from random import sample,randint
    while True:
        i = randint(0,len(cartSelec)-1)
        numEscolhido = sample(cartSelec[i],1)
        if numEscolhido[0] not in repetidos and numEscolhido[0].isnumeric():
            return numEscolhido[0]


def jogo(cart, jogador, numSorteado=0):
    #Eu ia tentar adicionar uma lógica pra adicionar os espaços aqui porém não consegui
    return cart


def imprimeJogo(cart,numSorteado,jogador):
    espaco = [' '*4,' '*10,' '*16,' '*22,' '*28]
    if jogador > 0:
        jogador -= 1
    print('-*'*20)
    print('SORTEANDO....',numSorteado)
    print('-*'*20)
    marca = False
    pos = 0
    for l in range(len(cart)):
        print('\n-----------')
        print(f'CARTELA {l+1} : | ',end = ' ')
        for c in range(len(cart[0])):
            if cart[l][c] == numSorteado:
                marca = True
                pos = c
            print(f'{cart[l][c]:^3}',end=' | ')
        for tag in range(len(cart)):
            if jogador == l:
                print('<<<<<<<',end ='')
                break
        print('\n---------',end=' ')
        if marca == True:
            print(espaco[pos],'--- ',end=' ')
            marca = False
    

def jogada(jogador):
    temp = jogador
    jogador = input('\nSelecione a tabela [1,2,3,4] ou pressione [ENTER] para continuar: ')
    if jogador.isnumeric():
        temp = jogador
    if not jogador.isnumeric():
        jogador = temp
    return int(jogador)


def verificarGanhador(cartSelecionadas,numSorteado):
    listaCartelas = [0]*len(cartSelecionadas)
    vencedores = []
    for l in range(len(cartSelecionadas)):
        for c in range(len(cartSelecionadas[0])):
            if l == 0:
                if cartSelecionadas[l][c] in numSorteado:
                    listaCartelas[0] += 1
            if l == 1:
                if cartSelecionadas[l][c] in numSorteado:
                    listaCartelas[1] += 1
            if l == 2:
                if cartSelecionadas[l][c] in numSorteado:
                    listaCartelas[2] += 1
            if l == 3:
                if cartSelecionadas[l][c] in numSorteado:
                    listaCartelas[3] += 1
    for i in range(len(listaCartelas)):
        if listaCartelas[i] == 5:
            vencedores.append(i)
    if len(vencedores) > 0:
        return vencedores,False
    else:
        return -1,True

    
def telaFinal(cartSelecionadas,vencedores,jogador):
    arquivoFinal = open('vencedores.txt','w',encoding ='UTF-8')
    if jogador > 0:
        jogador = jogador - 1
    for l in range(len(cartSelecionadas)):
        if l in vencedores:
            print('\n','*'*45)
            print(f'CARTELA {l+1} * ',end = ' ')
            for c in range(len(cartSelecionadas[0])):
                print(f'{cartSelecionadas[l][c]:^3}',end=' * ')
            for tag in range(len(cartSelecionadas)):
                if jogador == l:
                    print('<<<<<<<',end ='')
                    break
            print('\n','*'*45,end=' ')
        else:
            print('\n-----------')
            print(f'CARTELA {l+1} : | ',end = ' ')
            for c in range(len(cartSelecionadas[0])):
                print(f'{cartSelecionadas[l][c]:^3}',end=' | ')
            for tag in range(len(cartSelecionadas)):
                if jogador == l:
                    print('<<<<<<<',end ='')
                    break
            print('\n---------',end=' ')
    print('\nO VENCEDOR FOI A CARTELA ',end='... ')
    for i in range(len(vencedores)):
        print(f'{vencedores[i]+1}',end=' ')
    if jogador in vencedores:
        print('PARABÉNS')
        nome = input('DIGITE SEU NOME PARA ENTRAR NO ROL DE VENCEDORES: ')
        arquivoFinal.write(nome)
    else:
        print('\nNÃO FOI DESSA VEZ QUE VOCÊ VENCEU:(')
        arquivoFinal.write('SEM GANHADORES')
    


def main():
    print('JONATAS GARCIA DE OLIVEIRA  ')
    arquivo = open('cartelas.txt','r',encoding='UTF-8')
    cartelas = lerCartelas(arquivo)
    arquivo.close()
    selecionadas = sorteio(cartelas)
    header(selecionadas)
    numRepetidos = []
    jogador = 0
    qtd_Jogadas = 0
    flag = True
    while flag == True:
        numSorteado = numerosSorteados(selecionadas,numRepetidos)
        tabela = jogo(selecionadas,jogador,numSorteado)
        imprimeJogo(tabela,numSorteado,jogador)
        jogador = jogada(jogador)
        numRepetidos.append(numSorteado)
        qtd_Jogadas += 1
        if qtd_Jogadas >= 5:
            vencedores,flag = verificarGanhador(selecionadas,numRepetidos) 
    telaFinal(selecionadas,vencedores,jogador)
    
              
main()
