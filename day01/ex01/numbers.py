def lerNUmeros():
    arquivo = open('numbers.txt','r')

    for numero in arquivo:
        conteudo = numero.split(',')
    for temp in conteudo:
        print(temp)

    arquivo.close()
    

if __name__ =='__main__':
    lerNUmeros()