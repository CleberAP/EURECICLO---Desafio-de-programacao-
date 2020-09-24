"""
Desafio: README.md
Dado um conjunto de garrafas d'água, com volumes de água diferentes entre si, e um galão de água. Crie um algoritmo, na linguagem que achar melhor, para escolher as garrafas a serem utilizadas para encher o galão, de acordo:
        i. O galão deve ser completamente preenchido com o volume das garrafas;
        ii. Procure esvaziar totalmente as garrafas escolhidas;
        iii. Quando não for possível esvaziar todas garrafas escolhidas, deixe a menor sobra possível;
        iv. utilize o menor número de garrafas possível;
"""

import sys


class Algoritmo():

    def __init__(self, lista, maximo):
        # Quantidade de elementos da lista recebida
        self.n = len(lista)
        
        # lista de valores
        self.lista_A = lista

        # volume máximo que o recipiente principal deve receber dos demais
        self.capacidade_max = maximo

        self.Selecionados = {
            'lista':[],
            'soma': 0.0,
            'sobra': 0.0
        }

        self.execute(self.n)

    # GETTERS
    def get_selecionados(self):
        return self.Selecionados

    def set_selecionados(self, dict_selecionado):
        self.Selecionados = dict_selecionado

    def execute(self, n):
        # Cria uma Lista [1,...,n] que recebe valores para referência aos índices na lista de valores (self.lista_A)
        s = (n+1) * [0]
        k = 0
         
        flag_menor = 0.0  # recebe sempre o menor valor iterado para decidir se faz a verificação
         
        while True:
            lista = []  # lista de valores acessados
            soma = 0.0  # armazena a soma dos valores acessados
            sobra = 0.0 # armazena a diferença entre a soma dos valores acessados e a capacidade máxima do recipiente

            k = self.proximo_elemento(s,k,n)

            if k == 0:
                break
            for i in range(1,k+1):
                # variável que identifica o índice da lista de valores que será acessado
                j = s[i] - 1    # recebe o valor da lista de referência decrementado de 1

                # adiciona valor acessado à lista
                volume = 0.0
                for key,value in self.lista_A[j].items():
                    volume = value
                    #print(volume)
                soma += volume

                lista.append(self.lista_A[j])

            sobra = soma - self.capacidade_max

            if soma >= self.capacidade_max:
                # Verifica se é primeira iteração aprovada
                if len(self.Selecionados['lista']) == 0:
                    print("primeira ****************************")
                    flag_menor = soma
                    self.verificar(lista, soma, sobra)
                # Senão fará comparação, assim só faz verificação se valor somado for menor, ou seja, menor sobra
                else:
                    if soma <= flag_menor:
                        flag_menor = soma
                        print("Gerado: {} --> Soma: {}--> Sobra: {}".format(lista, soma, sobra))
                        # Só verifica quando encheu o recipiente principal
                        self.verificar(lista, soma, sobra)

    def proximo_elemento(self, vetor, k, n):
        # Caso particular - o 1º elemento
        if k == 0:
            vetor[1] = 1
            return 1
        # Caso particular - último elemento
        if vetor[1] == n:
            return 0
        # Caso Geral
        if vetor[k] < n:
            vetor[k+1] = vetor[k] + 1
            return k + 1
        vetor[k-1] += 1

        return k-1

    # Só verifica quando encheu o recipiente principal
    def verificar(self, lista, soma, sobra):
        #print(self.get_resultado())
        if len(self.Selecionados['lista']) == 0:
            #if soma >= self.capacidade_max:
            print("Início: {} --> Soma: {} --> Sobra: {}".format(lista, soma, sobra))
            self.set_selecionados({'lista':lista, 'soma': soma, 'sobra': sobra})
        else:
            print("Vindo: {} --> Soma: {} --> Sobra: {}".format(lista, soma, sobra))
            print(" Dict: {}".format(self.get_teste()))
            # Se sobra é menor
            if sobra < self.Selecionados['sobra']:
                self.set_selecionados({'lista':lista, 'soma': soma, 'sobra': sobra})
                print("    Sobra é menor")   
            # Senão se iguais
            elif sobra == self.Selecionados['sobra']:
                if len(lista) < len(self.Selecionados['lista']):
                    print("    Tamanho da lista é menor")
                    self.set_selecionados({'lista':lista, 'soma': soma, 'sobra': sobra})

        print(" Agora: {}\n".format(self.get_teste()))
           
    def get_teste(self):
        string = ''
        for key, value in self.get_selecionados().items():
            #print(key, ' - ', value)
            if key == 'lista':
                string += "{} --> Soma: ".format(value)
            if key == 'soma':
                string += "{} --> Sobra: ".format(value)
            if key == 'sobra':
                string += "{}".format(value)

        return string

def main(args):
    #lista = [3.5, 4.5, 1.0, 3.0, 0.5, 3.5]
    #lista = [3.5, 4.5, 1.1, 3.0, 0.5, 3.45, 2.22, 3.45, 0.1, 0.05]
    lista = []

    volume_maximo = float(input("Insira o volume do galão: ").replace(',','.'))
    qtd_garrafas = int(input("Informe a quantidade de garrafas: "))

    for i in range(1, qtd_garrafas+1):
        volume = float(input('Garrafa {}: '.format(i)).replace(',','.'))
        lista.append({'Garrafa {}'.format(i):volume})
        
    print("Garrafas registradas")
    for i in range(0,len(lista)):
        print(lista[i])
    #print()
    #print("Garrafas registradas")
    #for registro in lista:
    #    for key,value in registro.items():
    #        print(key,' - ', value)
        

    procurar = Algoritmo(lista, volume_maximo)
    dict_resultado = procurar.get_selecionados()
    resposta = '['
    for key,value in dict_resultado.items():
        if key == 'lista':
            for item in value:
                for k,v in item.items():
                    resposta = ''.join([resposta, k+": "+str(v)+"L, "])
            resposta = resposta[:-2] +" ]"
        if key == 'sobra':
            resposta = '- Sobra: '.join([resposta, str(value)])
              
    print("\n**************\nResposta: {}\n".format(resposta))

if __name__== "__main__":
    sys.exit(main(sys.argv))
