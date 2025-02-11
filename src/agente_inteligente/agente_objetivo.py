"""tem como objetivo explorar locais inesplorados e caso fique preso backtraking"""

class AgenteObjetivo:
    def __init__(self):
        self.estado_interno = {}
        # Utilizei list pois preciso saber a ordem de insersão
        self.visitados = []
        # O ponteiro serve para marcar a posição do agente no backtraking
        self.pointer = 0

    def atualizar_estado(self, percepcao):
        """Atualiza o estado interno do agente com base na percepção."""
        self.estado_interno = percepcao
        # Marcar a posição atual como visitada
        if not (percepcao["posicao_agente"] in self.visitados):
            self.visitados.append(percepcao["posicao_agente"])
            self.pointer = len(self.visitados)
        else:
            # cada movimento retrogrado do agente o ponteiro é realocado para a posição anterior da lista
            self.pointer -= 1

    def selecionar_acao(self, percepcao):
        """Seleciona a próxima ação com base na percepção, evitando obstáculos."""
        agente = percepcao["posicao_agente"]

        if self.__valida_posicao((agente[0]-1, agente[1])):
            return "esquerda"
        if self.__valida_posicao((agente[0]+1, agente[1])):
            return "direita"
        if self.__valida_posicao((agente[0], agente[1]-1)):
            return "cima"
        if self.__valida_posicao((agente[0], agente[1]+1)):
            return "baixo"
        return self.backtrack(self.visitados[self.pointer-2])

    # Verifica o sentido do movimento e aplica o contrario, assim indo no sentido contrario
    def backtrack(self, posicao):
        if posicao[0] != self.estado_interno["posicao_agente"][0]:
            if posicao[0] > self.estado_interno["posicao_agente"][0]:
                return "direita"
            return "esquerda"
        else:
            if posicao[1] > self.estado_interno["posicao_agente"][1]:
                return "baixo"
            return "cima"

    # Veridica se a posicao esta dentro dos limites do grid e se é um obstaculo
    def __valida_posicao(self, posicao):
        """Verifica se a posição esta dentro do limite do bord e se tem um obstaculo"""
        y, x = self.estado_interno["tamanho-bord"]
        if not(0 <= posicao[0] <= x-1 and 0 <= posicao[1] <= y-1):
            return False
        if posicao in self.estado_interno["obstaculos"]:
            return False
        if posicao in self.visitados:
            return False
        return True
