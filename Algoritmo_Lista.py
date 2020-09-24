# Recebe uma lista
#lista = [3.5, 4.5, 1.1, 3.0, 0.5, 3.45, 2.22, 3.45, 0.1, 0.05]

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
                lista.append(self.lista_A[j])

                soma += self.lista_A[j]
                #if soma >= self.capacidade_max:
                #    break
            sobra = soma - self.capacidade_max

            if soma >= self.capacidade_max:
                # Verifica se é primeira iteração aprovada
                if len(self.Selecionados['lista']) == 0:
                    flag_menor = soma
                    self.verificar(lista, soma, sobra)
                # Senão fará comparação, assim só faz verificação se valor somado for menor, ou seja, menor sobra
                else:
                    if soma <= flag_menor:
                        flag_menor = soma
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
            self.set_selecionados({'lista':lista, 'soma': soma, 'sobra': sobra})
        else:
            # Se sobra é menor
            if sobra < self.Selecionados['sobra']:
                self.set_selecionados({'lista':lista, 'soma': soma, 'sobra': sobra})
            # Senão se iguais
            elif sobra == self.Selecionados['sobra']:
                if len(lista) < len(self.Selecionados['lista']):
                    self.set_selecionados({'lista':lista, 'soma': soma, 'sobra': sobra})
           
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
        lista.append(volume)
        
    procurar = Algoritmo(lista, volume_maximo)
    print("Garrafas registradas")
    for i in range(0,len(lista)):
        print('   Garrafa {}: {:.2f}'.format(i,lista[i]))

    dict_resultado = procurar.get_selecionados()
    resposta = '['
    for key,value in dict_resultado.items():
        if key == 'lista':
            for valor in value:
                resposta = ''.join([resposta, str(valor)+"L,"])
            resposta = resposta[:-1] +"]"
        if key == 'sobra':
            resposta = '- Sobra: '.join([resposta, str(value)])
              
    print("\n**************\nResposta: {}\n".format(resposta))

if __name__== "__main__":
    sys.exit(main(sys.argv))
