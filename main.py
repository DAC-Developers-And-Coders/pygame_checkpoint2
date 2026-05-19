from GameManager import *

pygame.init()
pygame.mixer.init()

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

sotao = pygame.image.load("./images/attic.png").convert()
porao = pygame.image.load("./images/basement.png").convert()
cozinha = pygame.image.load("./images/kitchen.png").convert()
sala = pygame.image.load("./images/living-room.png").convert()
menu_image = pygame.image.load("./images/house-exterior.png").convert()
quarto_filha = pygame.image.load("./images/daughter-room.png").convert()
hall_entrada = pygame.image.load("./images/entrance-hall.png").convert()
quarto_pais = pygame.image.load("./images/parents-bedroom.png").convert()
corredor_andar2 = pygame.image.load("./images/upstairs-hallway.png").convert()

som_porta_menu = pygame.mixer.Sound("./sfx/opening_main_door.mp3")
som_porta_geral = pygame.mixer.Sound("./sfx/opening_default_door.mp3")
som_escada = pygame.mixer.Sound("./sfx/stairs_footsteps.mp3")
som_passos = pygame.mixer.Sound("./sfx/footsteps.mp3")

no_menu = True
na_sala = False
no_porao = False
no_sotao = False
na_cozinha = False
no_quarto_pais = False
no_quarto_filha = False
no_segundo_andar = False
no_primeiro_andar = False

pode_clicar = True
timer = None

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
            if no_menu:
                no_menu = verificar_iniciar_jogo(None, evento)

                if not no_menu:
                    som_porta_menu.play()
                    timer = [pygame.time.get_ticks(), 'Inicio']
                    pode_clicar = False
                else:
                    verificar_sair_jogo(evento)
            elif (not no_menu and not na_sala and not na_cozinha and not no_porao and not no_segundo_andar and not no_sotao
                  and not no_quarto_pais and not no_quarto_filha and no_primeiro_andar):
                no_segundo_andar_verificacao = verificar_segundo_andar(evento)
                na_sala = verificar_sala(evento)
                na_cozinha_verificacao = verificar_cozinha(evento)
                no_porao_verificacao = verificar_porao(evento)

                if no_segundo_andar_verificacao or na_sala or na_cozinha_verificacao or no_porao_verificacao:
                    no_primeiro_andar = False

                if na_cozinha_verificacao:
                    som_passos.play()
                    timer = [pygame.time.get_ticks(), 'Cozinha']
                    pode_clicar = False
                elif no_porao_verificacao:
                    som_passos.play()
                    timer = [pygame.time.get_ticks(), 'Porao']
                    pode_clicar = False

                if na_sala:
                    som_porta_geral.play()
                elif no_segundo_andar_verificacao:
                    som_escada.play()
                    timer = [pygame.time.get_ticks(), 'Escada']
                    pode_clicar = False
            elif (not no_menu and not na_sala and not na_cozinha and not no_porao and not no_primeiro_andar and not no_sotao
                  and not no_quarto_pais and not no_quarto_filha and no_segundo_andar):
                no_sotao_verificacao = verificar_sotao(evento)
                no_quarto_pais = verificar_quarto_pais(evento)
                no_quarto_filha = verificar_quarto_filha(evento)
                no_primeiro_andar_verificacao = verificar_retornar_a1(evento, 'S')

                if no_quarto_pais or no_sotao_verificacao or no_quarto_filha or no_primeiro_andar_verificacao:
                    no_segundo_andar = False

                if no_quarto_pais or no_quarto_filha:
                    som_porta_geral.play()
                if no_sotao_verificacao:
                    som_passos.play()
                    timer = [pygame.time.get_ticks(), 'Sotao']
                    pode_clicar = False
                if no_primeiro_andar_verificacao:
                    som_escada.play()
                    timer = [pygame.time.get_ticks(), 'Inicio']
                    pode_clicar = False

            elif na_sala:
                no_primeiro_andar = verificar_retornar_a1(evento, 'L')

                if no_primeiro_andar:
                    na_sala = False
            elif na_cozinha:
                no_primeiro_andar = verificar_retornar_a1(evento, 'K')

                if no_primeiro_andar:
                    som_porta_geral.play()
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

                if no_segundo_andar:
                    no_quarto_filha = False

    if timer is not None:
        if timer[1] == 'Inicio' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            no_primeiro_andar = True
        elif timer[1] == 'Escada' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            no_segundo_andar = True
        elif timer[1] == 'Cozinha' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            na_cozinha = True
        elif timer[1] == 'Porao' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            no_porao = True
        elif timer[1] == 'Sotao' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            no_sotao = True
        pode_clicar = True
        pygame.event.clear(pygame.MOUSEBUTTONDOWN)


    tecla_pressionada = pygame.key.get_pressed()

    if no_menu:
        no_menu = verificar_iniciar_jogo(tecla_pressionada)
        (na_sala, no_primeiro_andar, no_segundo_andar, na_cozinha, no_porao, no_quarto_pais, no_sotao, no_quarto_filha) = (
            False, False, False, False, False, False, False, False)
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

    pygame.display.flip()
    clock.tick(60)