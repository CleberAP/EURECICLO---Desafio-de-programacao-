class SelectContainers():

    def __init__(self, max_capacity, list_containers):

        self.max_capacity = max_capacity        # Capacidade máxima do recipiente principal
        self.list_containers = list_containers

        self.list_containers_selected = [] # Usado no método que recebe uma seleção específica para verificar

        self.volume_dumped = 0.0        # Recebe o valor despejado no recipiente principal até a capacidade máxima
        self.over = 0.0                # Recebe o valor que sobrou no recipiente despejado quando atingiu o máximo do recipiente principal.
       
        self.Selecteds = {
            'lista':[],
            'soma': 0.0,
            'sobra': 0.0
        }


    # método para esvaziar o recipiente principal. Utilizado na chamada de cada nova análise.
    def empty_container(self):
        self.volume_dumped = 0.0

    # retorna o volume total dos recipientes selecionados
    def get_volume_selected(self):
        return self.volume_dumped
    
    # retorna o valor do excesso, resto ou sobra
    def get_over(self):
        return self.over

    def get_selected(self):
        return self.list_containers_selected

    def get_selecteds(self):
        return self.Selecteds

    def check_selecteds(self):
        check = 0
        for key,value in self.get_selecteds().items():
            if key == 'lista':
                check = len(value)
        if check > 0:
            return True
        else:
            return False

    def set_selecteds(self, dict_selecionado):
        self.Selecteds = dict_selecionado

        
    def execute_selecao(self):
        for container in self.list_containers:
            registry = ''
            max_capacity = 0.0
            
            for key, value in container.items():
                registry = key
                volume = value
                
            self.volume_dumped += volume
            

            # Verifica se atingiu o objetivo, ou seja, encher o recipiente principal
            if self.volume_dumped >= self.max_capacity:
                self.list_containers_selected.append(container)
                self.over = self.volume_dumped - self.max_capacity
                break
            else:
                self.list_containers_selected.append(container)

            
    def execute(self):
        # Quantidade de elementos da lista recebida
        n = len(self.list_containers)
        self.execute_analysis_list(n)

    def execute_analysis_list(self, n):
        # Cria uma Lista [1,...,n] que recebe valores para referência aos índices na lista de valores (self.lista_A)
        s = (n+1) * [0]
        k = 0
         
        flag_menor = 0.0  # recebe sempre o menor valor iterado para decidir se faz a verificação
         
        while True:
            lista = []  # lista de valores acessados
            
            self.volume_dumped = 0.0
            self.over = 0.0  

            k = self.proximo_elemento(s,k,n)

            if k == 0:
                break
            for i in range(1,k+1):
                # variável que identifica o índice da lista de valores que será acessado
                j = s[i] - 1    # recebe o valor da lista de referência decrementado de 1

                # adiciona valor acessado à lista
                volume = 0.0
                for key,value in self.list_containers[j].items():
                    volume = value
                    #print(volume)
                self.volume_dumped += volume

                lista.append(self.list_containers[j])

            self.over = self.volume_dumped - self.max_capacity

            if self.volume_dumped >= self.max_capacity:
                # Verifica se é primeira iteração aprovada
                if len(self.Selecteds['lista']) == 0:
                    flag_menor = self.volume_dumped
                    self.verificar(lista, self.volume_dumped, self.over)
                # Senão fará comparação, assim só faz verificação se valor somado for menor, ou seja, menor sobra
                else:
                    if self.volume_dumped <= flag_menor:
                        flag_menor = self.volume_dumped
                        # Só verifica quando encheu o recipiente principal
                        self.verificar(lista, self.volume_dumped, self.over)

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
        if len(self.Selecteds['lista']) == 0:
            self.set_selecteds({'lista':lista, 'soma': soma, 'sobra': sobra})
        else:
            # Se sobra é menor
            if sobra < self.Selecteds['sobra']:
                self.set_selecteds({'lista':lista, 'soma': soma, 'sobra': sobra})
            # Senão se iguais
            elif sobra == self.Selecteds['sobra']:
                if len(lista) < len(self.Selecteds['lista']):
                    self.set_selecteds({'lista':lista, 'soma': soma, 'sobra': sobra})

#    def get_info_container(self, container):

#        for key, value in container.items():
#            registry = key
#            volume = value

#        return registry, volume
        
