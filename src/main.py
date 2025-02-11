"""
Atividade Prática 01: Implementação de Agentes Inteligentes
Objetivo:
- Implementar um agente inteligente que navega em um grid 2D para encontrar um objetivo
  enquanto evita obstáculos.
- Demonstrar interação estruturada entre agente e ambiente.

Grupo: Amauri Lima, Huandrey Pontes, Eurico Gabriel
Disciplina: Inteligência Artificial
"""

from agente_inteligente.agente_objetivo import AgenteObjetivo
from agente_inteligente.agente import Agente
from agente_inteligente.ambiente import Ambiente

# Simulação do Ambiente e do Agente
def simular(agente):
    # Definição do ambiente
    largura, altura = 5, 5
    posicao_objetivo = (4, 4)
    obstaculos = []
    ambiente = Ambiente(largura, altura, posicao_objetivo, obstaculos)

    # Inicializar agente
    posicao_inicial = (0, 0)
    ambiente.inicializar_agente(posicao_inicial)

    # Executar simulação
    passos_maximos = altura * largura
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
    mensagem = "\nEscolha um agente inteligente: \n1. Agente Baseado em Modelo\n2. Agente Baseado em Objetivo\n-. Sair\n"
    ent = input(mensagem)
    while ent != "-":
        if ent == "1" or ent == "2":
            match ent:
                case "1":
                    simular(Agente())
                case "2":
                    simular(AgenteObjetivo())
        ent = input(mensagem)