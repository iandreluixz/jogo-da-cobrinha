import random
import tkinter as tk

TAMANHO_CELULA = 20
LARGURA = 400
ALTURA = 400
VELOCIDADE = 120

root = tk.Tk()
root.title("Jogo da Cobrinha")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=LARGURA,
    height=ALTURA,
    bg="black",
    highlightthickness=0
)
canvas.pack()


def criar_comida():
    posicoes_livres = [
        (x, y)
        for x in range(LARGURA // TAMANHO_CELULA)
        for y in range(ALTURA // TAMANHO_CELULA)
        if (x, y) not in cobra
    ]

    if not posicoes_livres:
        return None

    return random.choice(posicoes_livres)


def desenhar():
    canvas.delete("all")

    for x, y in cobra:
        canvas.create_rectangle(
            x * TAMANHO_CELULA,
            y * TAMANHO_CELULA,
            (x + 1) * TAMANHO_CELULA,
            (y + 1) * TAMANHO_CELULA,
            fill="lime"
        )

    if comida is not None:
        x, y = comida
        canvas.create_oval(
            x * TAMANHO_CELULA,
            y * TAMANHO_CELULA,
            (x + 1) * TAMANHO_CELULA,
            (y + 1) * TAMANHO_CELULA,
            fill="red"
        )

    canvas.create_text(
        45, 15,
        text=f"Pontos: {pontos}",
        fill="white",
        font=("Arial", 12)
    )

    if fim_de_jogo:
        mensagem = "Você venceu!" if venceu else "Fim de jogo!"
        canvas.create_text(
            LARGURA // 2,
            ALTURA // 2,
            text=f"{mensagem}\nPressione R para recomeçar",
            fill="white",
            font=("Arial", 18),
            justify="center"
        )


def mover_cobra():
    global cobra, comida, pontos, fim_de_jogo, venceu

    if fim_de_jogo:
        return

    cabeca_x, cabeca_y = cobra[0]
    nova_cabeca = (cabeca_x + direcao_x, cabeca_y + direcao_y)

    x, y = nova_cabeca
    saiu_da_tela = (
        x < 0
        or x >= LARGURA // TAMANHO_CELULA
        or y < 0
        or y >= ALTURA // TAMANHO_CELULA
    )

    comeu = nova_cabeca == comida

   
    corpo_verificado = cobra if comeu else cobra[:-1]

    if saiu_da_tela or nova_cabeca in corpo_verificado:
        fim_de_jogo = True
        desenhar()
        return

    cobra.insert(0, nova_cabeca)

    if comeu:
        pontos += 1
        comida = criar_comida()

        if comida is None:
            fim_de_jogo = True
            venceu = True
    else:
        cobra.pop()

    desenhar()

    if not fim_de_jogo:
        root.after(VELOCIDADE, mover_cobra)


def reiniciar():
    global cobra, comida, direcao_x, direcao_y
    global pontos, fim_de_jogo, venceu

    cobra = [(10, 10), (9, 10), (8, 10)]
    direcao_x = 1
    direcao_y = 0
    pontos = 0
    fim_de_jogo = False
    venceu = False
    comida = criar_comida()

    desenhar()
    root.after(VELOCIDADE, mover_cobra)


def pressionar_tecla(evento):
    global direcao_x, direcao_y

    tecla = evento.keysym.lower()

    if fim_de_jogo:
        if tecla == "r":
            reiniciar()
        return

    direcoes = {
        "up": (0, -1),
        "w": (0, -1),
        "down": (0, 1),
        "s": (0, 1),
        "left": (-1, 0),
        "a": (-1, 0),
        "right": (1, 0),
        "d": (1, 0)
    }

    if tecla not in direcoes:
        return

    nova_direcao_x, nova_direcao_y = direcoes[tecla]

   
    if (
        nova_direcao_x != -direcao_x
        or nova_direcao_y != -direcao_y
    ):
        direcao_x = nova_direcao_x
        direcao_y = nova_direcao_y


cobra = []
comida = None
direcao_x = 1
direcao_y = 0
pontos = 0
fim_de_jogo = True
venceu = False

root.bind("<KeyPress>", pressionar_tecla)
reiniciar()
root.mainloop()