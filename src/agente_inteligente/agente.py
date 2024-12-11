class Agente:
    def __init__(self):
        self.estado_interno = {}

    def atualizar_estado(self, percepcao):
        """Atualiza o estado interno do agente com base na percepção."""
        self.estado_interno = percepcao

    def selecionar_acao(self, percepcao):
        """Seleciona a próxima ação com base na percepção, evitando obstáculos."""
        posicao_agente = percepcao["posicao_agente"]
        posicao_objetivo = percepcao["posicao_objetivo"]
        obstaculos = percepcao.get("obstaculos", [])

        # Heurística para mover na direção do objetivo
        dx = posicao_objetivo[0] - posicao_agente[0]
        dy = posicao_objetivo[1] - posicao_agente[1]

        acoes_preferenciais = []
        if abs(dx) > abs(dy):
            acoes_preferenciais = ["direita" if dx > 0 else "esquerda", "baixo" if dy > 0 else "cima"]
        else:
            acoes_preferenciais = ["baixo" if dy > 0 else "cima", "direita" if dx > 0 else "esquerda"]

        # Adicionar todas as ações possíveis
        todas_acoes = acoes_preferenciais + ["cima", "baixo", "esquerda", "direita"]

        # Verificar quais ações não levam a um obstáculo
        for acao in todas_acoes:
            nova_posicao = self.simular_movimento(posicao_agente, acao)
            if nova_posicao not in obstaculos:
                return acao

        # Se todas as ações levam a obstáculos (caso raro), permanecer no lugar
        return "parar"

    @staticmethod
    def simular_movimento(posicao, acao):
        """Simula o movimento do agente baseado na ação."""
        x, y = posicao
        if acao == "cima":
            return x, y - 1
        elif acao == "baixo":
            return x, y + 1
        elif acao == "esquerda":
            return x - 1, y
        elif acao == "direita":
            return x + 1, y
        return posicao
