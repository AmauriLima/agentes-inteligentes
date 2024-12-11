# Simulador de Agente e Ambiente

Este projeto é um simulador simples que demonstra a interação entre um agente e um ambiente. O agente navega por um ambiente retangular, evitando obstáculos e tentando alcançar um objetivo.

## 🗂 Estrutura do Projeto

O projeto é organizado em um package modular para facilitar a manutenção e expansão:

## ✨ Funcionalidades

- **Ambiente:**

  - Representa o espaço onde o agente opera.
  - Define o tamanho do grid, posição do objetivo e obstáculos.
  - Gerencia o estado do agente e processa suas ações.

- **Agente:**

  - Recebe percepções do ambiente.
  - Decide ações com base em heurísticas para alcançar o objetivo enquanto evita obstáculos.

- **Simulação:**
  - Realiza a interação entre o agente e o ambiente.
  - Monitora as ações do agente e verifica se ele alcançou o objetivo.

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/AmauriLima/agentes-inteligentes.git
   cd agentes-inteligentes
   ```

2. Certifique-se de ter o Python 3.6 ou superior instalado.

3. Execute o arquivo main.py para iniciar a simulação:

   ```bash
   python src/main.py
   ```

4. O programa executará a simulação e imprimirá a sequência de ações do agente até que ele alcance o objetivo ou o número máximo de passos seja atingido.

## 🛠 Personalização

**Ambiente**
O ambiente é configurado na classe Ambiente, onde você pode:

- Modificar o tamanho do grid (largura e altura).
- Definir a posição do objetivo.
- Adicionar ou remover obstáculos no grid.

Exemplo de personalização no arquivo ambiente.py:

    ```python
    # Criar um ambiente de 5x5 com um objetivo na posição (4, 4)
    ambiente = Ambiente(largura=5, altura=5, posicao_objetivo=(4, 4), obstaculos=[(2, 2), (3, 2), (1, 3)])
    ```

## 📚 Exemplo de Saída

Ao executar a simulação, você verá a seguinte saída no terminal, com o agente realizando as ações para alcançar o objetivo:

```text
Passo 1:
  Percepção: {'posicao_agente': (0, 0), 'posicao_objetivo': (4, 4), 'obstaculos': [(2, 2), (3, 2), (1, 3)]}
  Ação: direita
Passo 2:
  Percepção: {'posicao_agente': (1, 0), ...}
  Ação: baixo
...
O agente alcançou o objetivo!
```

## 👨‍🎓👨‍🎓👨‍🎓 Grupo

- Amauri Lima
- Eurico Gabriel
- Huandrey Pontes
