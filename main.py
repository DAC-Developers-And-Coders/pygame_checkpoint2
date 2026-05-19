from GameManager import *
from combat import combate, checar_encontro


pygame.init()

jogador = {
    'nome': 'John',
    'hp': 3
}

inimigo = {
    'nome': 'Mary',
    'hp': 3
}

em_combate = False
inimigo_aparece = False
em_evento = False
sala_evento = None
ultima_rolagem = None

if inimigo_aparece:
    em_combate = True

#CONFIG GERAL
LARGURA = 1920
ALTURA = 1080
BRANCO = (255,255,255)
CINZA = (128, 128, 128)
PRETO = (0,0,0)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("CP2")

clock = pygame.time.Clock()
fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 50)

texto_menu = fonte_menu.render("FAITH", True, BRANCO)

botoes = [fonte_geral.render("Jogar", True, BRANCO), fonte_geral.render("Sair", True, BRANCO)]

#IMAGENS
sotao = pygame.image.load("./images/attic.png").convert()
porao = pygame.image.load("./images/basement.png").convert()
cozinha = pygame.image.load("./images/kitchen.png").convert()
sala = pygame.image.load("./images/living-room.png").convert()
menu_image = pygame.image.load("./images/house-exterior.png").convert()
quarto_filha = pygame.image.load("./images/daughter-room.png").convert()
hall_entrada = pygame.image.load("./images/entrance-hall.png").convert()
quarto_pais = pygame.image.load("./images/parents-bedroom.png").convert()
corredor_andar2 = pygame.image.load("./images/upstairs-hallway.png").convert()
garota_sotao = pygame.image.load("./images/girl/girl_attic.png").convert()
garota_porao = pygame.image.load("./images/girl/girl_basement.png").convert()
garota_cozinha = pygame.image.load("./images/girl/girl_kitchen.png").convert()
garota_sala = pygame.image.load("./images/girl/girl_living_room.png").convert()
garota_quarto_pais = pygame.image.load("./images/girl/girl_parents_bedroom.png").convert()
garota_quarto_filha = pygame.image.load("./images/girl/girl_bedroom.png").convert()
garota_diario_original = pygame.image.load("./images/girl/girl_diary.png").convert()
garota_diario = pygame.transform.scale(garota_diario_original, (450, 650))
garota_foto = pygame.image.load("./images/girl/girl_photo.png").convert()

no_menu = True
na_sala = False
no_porao = False
no_sotao = False
na_cozinha = False
no_quarto_pais = False
no_quarto_filha = False
no_segundo_andar = False
no_primeiro_andar = False
na_sala_garota = False
no_porao_garota = False
no_sotao_garota = False
na_cozinha_garota = False
no_quarto_pais_garota = False
no_quarto_filha_garota = False
mostrar_diario_garota = False

fechar_diario_garota = pygame.Rect(702,20,50,50)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mostrar_diario_garota:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if fechar_diario_garota.collidepoint(evento.pos):
                    mostrar_diario_garota = False
            continue

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if no_menu:
                no_menu = verificar_iniciar_jogo(None, evento)

                if not no_menu:
                    no_primeiro_andar = True
                else:
                    verificar_sair_jogo(evento)
            elif (not no_menu and not na_sala and not na_cozinha and not no_porao and not no_segundo_andar and not no_sotao
                  and not no_quarto_pais and not no_quarto_filha and no_primeiro_andar):
                no_segundo_andar = verificar_segundo_andar(evento)
                na_sala = verificar_sala(evento)
                na_cozinha = verificar_cozinha(evento)
                no_porao = verificar_porao(evento)

                if no_segundo_andar or na_sala or na_cozinha or no_porao:
                    no_primeiro_andar = False
            elif (not no_menu and not na_sala and not na_cozinha and not no_porao and not no_primeiro_andar and not no_sotao
                  and not no_quarto_pais and not no_quarto_filha and no_segundo_andar):
                no_sotao = verificar_sotao(evento)
                no_quarto_pais = verificar_quarto_pais(evento)
                no_quarto_filha = verificar_quarto_filha(evento)
                no_primeiro_andar = verificar_retornar_a1(evento, 'S')

                if no_quarto_pais or no_sotao or no_quarto_filha or no_primeiro_andar:
                    no_segundo_andar = False
            elif na_sala:
                no_primeiro_andar = verificar_retornar_a1(evento, 'L')

                if no_primeiro_andar:
                    na_sala = False
            elif na_cozinha:
                no_primeiro_andar = verificar_retornar_a1(evento, 'K')

                if no_primeiro_andar:
                    na_cozinha = False
            elif no_porao:
                no_primeiro_andar = verificar_retornar_a1(evento, 'B')

                if no_primeiro_andar:
                    no_porao = False
            elif no_sotao:
                no_segundo_andar = verificar_retornar_a1(evento, 'A')

                if no_segundo_andar:
                    no_sotao = False
            elif no_quarto_pais:
                no_segundo_andar = verificar_retornar_a1(evento, 'P')

                if no_segundo_andar:
                    no_quarto_pais = False
            elif no_quarto_filha:
                no_segundo_andar = verificar_retornar_a1(evento, 'D')
                x, y = evento.pos
                print(x, y)

                if no_segundo_andar:
                    no_quarto_filha = False

                if verificar_mesa_quarto_filha(evento):
                    mostrar_diario_garota = True



    tecla_pressionada = pygame.key.get_pressed()

    if no_menu:
        no_menu = verificar_iniciar_jogo(tecla_pressionada)
        (na_sala, no_primeiro_andar, no_segundo_andar, na_cozinha, no_porao, no_quarto_pais, no_sotao, no_quarto_filha, mostrar_diario_garota) = (
            False, False, False, False, False, False, False, False, False)
        if not no_menu:
            no_primeiro_andar = True
        gerenciar_menu(botoes, fonte_geral, CINZA, BRANCO, PRETO, tela, menu_image, texto_menu)
    elif no_primeiro_andar:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, hall_entrada)
    elif na_sala:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, sala)
    elif na_cozinha:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, cozinha)
    elif no_porao:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, porao)
    elif no_segundo_andar:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, corredor_andar2)
    elif no_quarto_pais:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, quarto_pais)
    elif no_sotao:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, sotao)
    elif no_quarto_filha:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
        gerenciar_tela(tela, quarto_filha)
        if mostrar_diario_garota:
            no_menu = verificar_tecla_pressionada(tecla_pressionada, True)
            gerenciar_tela(tela, garota_diario)
            texto_x = fonte_geral.render("X", True, (255, 255, 255))
            tela.blit(texto_x, (fechar_diario_garota.x + 12, fechar_diario_garota.y + 2))


    pygame.display.flip()
    clock.tick(60)