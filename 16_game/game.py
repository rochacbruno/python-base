import os
import random
import pygame as pg
import pygame.locals as keys

# Constantes
DIR = os.path.abspath(os.path.dirname(__file__))
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (60, 220, 0)
AMARELO = (255, 240, 60)
CINZA = (50, 50, 50)
TAMANHO_JANELA = (800, 800)

# Variaveis
tamanho = largura, altura = TAMANHO_JANELA
largura_estrada = int(largura / 1.6)
largura_separador = int(largura / 200)
lado_direito = largura / 2 + largura_estrada / 4
lado_esquerdo = largura / 2 - largura_estrada / 4
velocidade = 1

# Jogadores
jogador = pg.image.load(os.path.join(DIR, "player", "player.png"))
jogador = pg.transform.scale(jogador, (150, 150))
posicao_do_jogador = jogador.get_rect()
posicao_do_jogador.center = lado_direito, altura * 0.8

# Janela principal
pg.init()
tela = pg.display.set_mode(tamanho)
pg.display.set_caption("Catch a beer")
tela.fill(VERDE)
pg.display.update()

# Fontes
letra = pg.font.SysFont("Comic Sans MS", 30)
letra_grande = pg.font.SysFont("Comic Sans MS", 90)


def carrega_cerveja_aleatoria():
    i = random.randint(1, 5)
    cerveja = pg.image.load(os.path.join(DIR, "beers", f"{i}.png"))
    cerveja = pg.transform.scale(cerveja, (100, 100))
    posicao_da_cerveja = cerveja.get_rect()
    if random.randint(0, 1) == 0:
        posicao_da_cerveja.center = lado_direito, altura * 0.2
    else:
        posicao_da_cerveja.center = lado_esquerdo, altura * 0.2
    return cerveja, posicao_da_cerveja


# Valores de inicialização do jogo
cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()
bebeu = 0
rodadas = 0
executando = True
pausado = True
perdas = 0

# Loop principal
while executando:
    rodadas += 1

    # Fica mais rápido com o tempo
    if rodadas == 5000:
        velocidade += 0.15
        rodadas = 0
        print("Level UP", velocidade)

    # Detecção de colisão (bebeu a cerveja)
    if (
        10 < (posicao_do_jogador[1] - posicao_da_cerveja[1]) < 30
        and posicao_do_jogador[0] == posicao_da_cerveja[0] - 25
    ):
        bebeu += 1
        sound = random.choice(["sensacional.mp3", "olha_so.mp3"])
        pg.mixer.music.load(os.path.join(DIR, "sound", sound))
        pg.mixer.music.play(0)
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()

    # Animação da cerveja saindo do ponto inicial da reta Y (vertical)
    # E se movimentando a cada rodada
    posicao_da_cerveja[1] += velocidade

    # Captura Eventos do Pygame (teclas pressionadas)
    for event in pg.event.get():
        if event.type == keys.QUIT:
            executando = False
        if event.type == keys.KEYDOWN:
            if event.key in (keys.K_a, keys.K_LEFT):
                posicao_do_jogador = posicao_do_jogador.move(
                    (-int(largura_estrada / 2), 0)
                )
            if event.key in (keys.K_d, keys.K_RIGHT):
                posicao_do_jogador = posicao_do_jogador.move(
                    (int(largura_estrada / 2), 0)
                )

    # Desenha a estrada no meio da tela
    pg.draw.rect(
        tela,
        CINZA,
        (largura / 2 - largura_estrada / 2, 0, largura_estrada, altura),
    )

    # Desenha o separador da estrada
    pg.draw.rect(
        tela,
        AMARELO,
        (largura / 2 - largura_separador / 2, 0, largura_separador, altura),
    )

    # Borda esquerda
    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 - largura_estrada / 2 + largura_separador * 2,
            0,
            largura_separador,
            altura,
        ),
    )
    # Borda direita
    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 + largura_estrada / 2 - largura_separador * 3,
            0,
            largura_separador,
            altura,
        ),
    )

    # Titulo
    titulo = letra.render(
        f"Catch a Beer! bebeu: {bebeu} vacilou: {perdas}", 1, BRANCO, PRETO
    )
    tela.blit(titulo, (largura / 5, 0))

    # Adiciona jogador e imagens na tela
    tela.blit(jogador, posicao_do_jogador)
    tela.blit(cerveja, posicao_da_cerveja)

    # Recarrega os gráficos na tela em suas posições alteradas no loop
    pg.display.update()

    # Espera o jogador pressionar uma tecla
    while pausado:
        msg = letra.render("Press any key to start", True, AMARELO, PRETO)
        tela.blit(msg, (largura / 4, 100))
        pg.display.update()
        for event in pg.event.get():
            if event.type == keys.KEYDOWN:
                pg.mixer.music.load(os.path.join(DIR, "sound", "vai.mp3"))
                pg.mixer.music.play(0)
                pausado = False

    # Verifica se o jogador deixou a cerveja cair
    if posicao_da_cerveja[1] > altura:
        perdas += 1
        cerveja, posicao_da_cerveja = carrega_cerveja_aleatoria()

    # Se cairem 3 cervejas o jogo acaba
    if perdas > 3:
        msg = letra_grande.render("GAME OVER", True, AMARELO, PRETO)
        pg.mixer.music.load(os.path.join(DIR, "sound", "zika.mp3"))
        pg.mixer.music.play(0)
        tela.blit(msg, (largura / 4, 100))
        pg.display.update()
        wait_key = True
        while wait_key:
            for event in pg.event.get():
                if event.type == keys.KEYDOWN:
                    wait_key = executando = False
        pg.quit()

pg.quit()
