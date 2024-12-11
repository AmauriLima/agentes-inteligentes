"""
Atividade Prática 01: Implementação de Agentes Inteligentes
Objetivo:
- Implementar um agente inteligente que navega em um grid 2D para encontrar um objetivo
  enquanto evita obstáculos.
- Demonstrar interação estruturada entre agente e ambiente.

Grupo: Amauri Lima, Huandrey Pontes, Eurico Gabriel
Disciplina: Inteligência Artificial
"""

from agente_inteligente.agente import Agente;
from agente_inteligente.ambiente import Ambiente;

# Simulação do Ambiente e do Agente
def simular():
    # Definição do ambiente
    largura, altura = 5, 5
    posicao_objetivo = (4, 4)
    obstaculos = [(2, 2), (3, 2), (1, 3)]
    ambiente = Ambiente(largura, altura, posicao_objetivo, obstaculos)

    # Inicializar agente
    posicao_inicial = (0, 0)
    ambiente.inicializar_agente(posicao_inicial)
    agente = Agente()

    # Executar simulação
    passos_maximos = 20
    for passo in range(passos_maximos):
        print(f"Passo {passo + 1}:")
        percepcao = ambiente.gerar_percepcao()
        print(f"  Percepção: {percepcao}")

        if ambiente.objetivo_alcancado():
            print("  O agente alcançou o objetivo!")
            break

        agente.atualizar_estado(percepcao)
        acao = agente.selecionar_acao(percepcao)
        print(f"  Ação: {acao}")

        ambiente.receber_acao(acao)
    else:
        print("O agente não alcançou o objetivo dentro do limite de passos.")


if __name__ == "__main__":
    simular()
