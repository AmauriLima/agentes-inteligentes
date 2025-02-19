import random

# Classe que define o Ambiente
class Ambiente:
    def __init__(self, largura, altura, posicao_objetivo, obstaculos):
        self.largura = largura
        self.altura = altura
        self.posicao_objetivo = posicao_objetivo
        self.obstaculos = obstaculos
        self.estado_agente = None

    def inicializar_agente(self, posicao_inicial):
        """Define a posição inicial do agente."""
        self.estado_agente = posicao_inicial

    def receber_acao(self, acao):
        """Atualiza o estado do agente baseado na ação recebida."""
        x, y = self.estado_agente
        if acao == "cima":
            y -= 1
        elif acao == "baixo":
            y += 1
        elif acao == "esquerda":
            x -= 1
        elif acao == "direita":
            x += 1

        # Verificar limites e evitar obstaculos
        if 0 <= x < self.largura and 0 <= y < self.altura and (x, y) not in self.obstaculos:
            self.estado_agente = (x, y)

    def gerar_percepcao(self):
        """Retorna a percepção para o agente."""
        return {
            "posicao_agente": self.estado_agente,
            "posicao_objetivo": self.posicao_objetivo,
            "obstaculos": self.obstaculos,
            "tamanho-bord": (self.largura, self.altura),
        }

    def objetivo_alcancado(self):
        """Verifica se o agente alcançou o objetivo."""
        return self.estado_agente == self.posicao_objetivo
