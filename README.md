# 🐍 Jogo da Cobrinha

Um jogo clássico da cobrinha, feito em **Python** com a biblioteca gráfica **Tkinter**. Controle a cobra, coma a comida, aumente sua pontuação e tente preencher todo o tabuleiro sem bater nas paredes ou em si mesmo.

## 🎮 Como jogar

| Ação | Teclas |
| --- | --- |
| Mover para cima | `↑` ou `W` |
| Mover para baixo | `↓` ou `S` |
| Mover para a esquerda | `←` ou `A` |
| Mover para a direita | `→` ou `D` |
| Recomeçar depois do fim da partida | `R` |

Cada comida aumenta o tamanho da cobra e acrescenta **1 ponto**. A partida termina se a cobra sair dos limites do tabuleiro ou bater no próprio corpo. Se ela ocupar todas as posições disponíveis, você vence!

## ✨ Funcionalidades

- Tabuleiro de **400 × 400 pixels**, dividido em células de **20 × 20 pixels**.
- Cobra verde que se movimenta continuamente.
- Comida vermelha posicionada aleatoriamente em uma casa livre.
- Pontuação exibida durante a partida.
- Controles pelas setas do teclado ou pelas teclas `W`, `A`, `S` e `D`.
- Prevenção de uma virada imediata na direção oposta, evitando que a cobra volte diretamente sobre si mesma.
- Detecção de colisões com as bordas e com o próprio corpo.
- Mensagens de fim de jogo e de vitória, com opção de reiniciar usando `R`.

## 🧰 Requisitos

- Python 3.
- Tkinter, utilizado para criar a janela e desenhar o jogo. Ele normalmente já acompanha as instalações padrão do Python para Windows e macOS.

O jogo usa apenas bibliotecas incluídas no Python (`tkinter` e `random`); não é necessário instalar pacotes adicionais.

## ▶️ Como executar

1. Instale o Python 3, se ainda não estiver instalado.
2. Baixe ou clone este repositório.
3. Abra um terminal na pasta do projeto e execute:

```bash
python Jogo_cobrinha.py
```

No Windows, se o comando `python` não funcionar, tente:

```powershell
py Jogo_cobrinha.py
```

## 🧠 Como o código funciona

Toda a lógica do jogo está no arquivo [`Jogo_cobrinha.py`](./Jogo_cobrinha.py). O programa usa uma grade lógica: cada posição da cobra e da comida é guardada como um par de coordenadas `(x, y)`. Essas coordenadas representam células, não pixels; na hora de desenhar, são multiplicadas pelo tamanho da célula.

### Janela e configuração

No início do arquivo, algumas constantes definem o tamanho das células, as dimensões do tabuleiro e o intervalo entre movimentos. O Tkinter cria a janela e um `Canvas`, que funciona como a área de desenho.

### Estado da partida

As variáveis principais guardam:

- `cobra`: lista de coordenadas do corpo; o primeiro item é a cabeça.
- `comida`: coordenada da comida ou `None` quando não há uma posição livre.
- `direcao_x` e `direcao_y`: deslocamento da cobra a cada movimento.
- `pontos`: quantidade de comidas coletadas.
- `fim_de_jogo` e `venceu`: indicam se a partida terminou e se o jogador venceu.

### Desenho

A função `desenhar()` limpa o `Canvas` e redesenha a cobra, a comida, a pontuação e, quando necessário, a mensagem de encerramento. A cobra é desenhada com retângulos verdes e a comida com um círculo vermelho.

### Comida

A função `criar_comida()` procura as posições da grade que não estão ocupadas pela cobra e escolhe uma delas aleatoriamente. Se todas estiverem ocupadas, não há mais espaço livre e a partida pode terminar com vitória.

### Movimento e colisões

A função `mover_cobra()` calcula a próxima posição da cabeça e verifica se ela saiu do tabuleiro ou atingiu o corpo. Ao comer, a cobra cresce e a pontuação aumenta; caso contrário, o último segmento é removido, mantendo o tamanho. A função `root.after()` agenda o próximo movimento sem bloquear a janela.

### Teclado e reinício

A função `pressionar_tecla()` associa as setas e as teclas `W`, `A`, `S` e `D` às direções da cobra. Depois do fim da partida, a tecla `R` chama `reiniciar()`, que restaura a posição inicial, a direção, a pontuação e o estado do jogo.

Por fim, `root.mainloop()` mantém a janela aberta e permite que o Tkinter processe os desenhos, o teclado e os movimentos.

## 📁 Estrutura do projeto

```text
.
├── Jogo_cobrinha.py   # Código e lógica do jogo
└── README.md          # Apresentação e instruções do projeto
```

## 🛠️ Tecnologias

- **Python** — regras, estado e movimentação do jogo.
- **Tkinter** — janela, desenho e leitura das teclas.
- **Git e GitHub** — versionamento e publicação do projeto.
