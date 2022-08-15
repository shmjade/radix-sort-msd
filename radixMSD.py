#########################################################################################
######                                AUXILIARES                                   ######
#########################################################################################

#Lê um arquivo txt e retorna uma lista com as palavras
def leitura_arquivo(nome):
    livro = []
    with open(nome, "r") as tf:
        lines = tf.read().replace("\n", " ")
        lines = lines.split(' ')  

    for line in lines:
        if(len(line)>=4):
            livro.append(line)
    return livro

#Dada uma lista de palavras, cria um dicionário contendo as palavras e as respectivas contagens
def conta_palavras(lista):
    dic={}
    for item in lista:
        if item in dic:
            dic[item]=dic[item]+1
        else:
            dic[item]=1
    return dic

#Dada uma lista de palavras, imprime a palavra ao lado da quantidade de ocorrências em sequência dessa palavra
def contagem(lista):
    i=0
    while(i<len(lista)-1):
        cont=1
        while(i<len(lista)-1 and lista[i]==lista[i+1]):
            i+=1
            cont+=1
        if(i==len(lista)-2):
            if(lista[i]==lista[i+1]):
                cont+=1
                print(lista[i]+": "+str(cont))
                i+=1
            else:
                print(lista[i]+": "+str(cont))  
                i+=1
                cont=1
                print(lista[i]+": "+str(cont))  
        else:  
            print(lista[i]+": "+str(cont))     
        i+=1

def escreve(lista, nome):
    f = open(nome, "w") 
    i=0
    while(i<len(lista)-1):
        cont=1
        while(i<len(lista)-1 and lista[i]==lista[i+1]):
            i+=1
            cont+=1
        if(i==len(lista)-2):
            if(lista[i]==lista[i+1]):
                cont+=1
                f.write(lista[i]+" "+str(cont)+"\n")
                i+=1
            else:
                f.write(lista[i]+" "+str(cont)+"\n")  
                i+=1
                cont=1
                f.write(lista[i]+" "+str(cont)+"\n")  
        else:  
            f.write(lista[i]+" "+str(cont)+"\n")     
        i+=1

#########################################################################################
######                     IMPLEMENTAÇÃO DO RADIX SORT                             ######
#########################################################################################

#Implementação do Radix Sort MSD: recebe uma lista e um índice e ordena essa lista de acordo 
#com o índice, separando em buckets e, depois de cada bucket estar ordenado (com uma chamada
#recursiva do radix sort), inserindo os buckets em uma lista de saída da função
def radix(lista, indice):
    if(len(lista)<2): #se tiver menos de 2 itens, já está ordenada
        return lista
    # "Definições"
    ordenado = [] # vetor de saída, ordenado pelo índice dado
    #o fim de string vem antes de tudo (indice 0), 'a' começa em 1 (ascii: 97), 'z' é o final (ascii: 122)
    aux = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #vetor de listas, os "buckets" que vão de vazio, 'a' a 'z'
    # Colocar as palavras nos buckets
    existe_maior=0 #flag que guarda se há uma string de maior tamanho na lista. Caso sim, continua a ordenação, caso não, fim
    for palavra in lista:
        #verifica se a palavra é maior do que o índice analisado
        if(len(palavra)-1>indice):
            existe_maior=1
        #verifica o contrário: se o caracter analisado é um espaço em branco/vazio (ou seja, se a palavra terminou antes do índice)
        if(len(palavra)<=indice):     
            aux[0].append(palavra)    #se a palavra é menor, vai no começo da lista (bucket 0)
        else:
            #o vetor auxiliar guarda os buckets de vazio,a,...,z. Levamos em consideração: 
            # - palavra[indice].lower transforma o caracter em minúsculo
            # - ascii 'a' = 97
            # - para a palavra[indice]=='a' estar no índice 1, devemos fazer -97+1
            aux[ord(palavra[indice].lower())-97+1].append(palavra) #se não for vazio, vai para a lista/bucket correspondente
    # Em ordem alfabética, adicionar as palavras dos buckets no vetor "ordenado" 
    for bucket in aux:
        if(existe_maior==1): #somente chama a recursão se houver 2 ou mais elementos e não houver palavra maior/eles não forem iguais
            bucket = radix(bucket,indice+1)
        for elemento in bucket: #ao sair da recursão, adicionar os elementos na lista ordenada
            ordenado.append(elemento)
    #retorna a lista ordenada a partir do índice dado
    return ordenado


#########################################################################################
######                                 CHAMADAS                                    ######
#########################################################################################
escreve(radix(leitura_arquivo("frankenstein.txt"),0),"frankenstein_ordenado.txt")
escreve(radix(leitura_arquivo("war_and_peace.txt"),0),"war_and_peace_ordenado.txt")

