from GameManager import *
from combat import *

pygame.init()
pygame.mixer.init()

jogador = {
    'nome': 'John',
    'hp': 3
}

inimigo = {
    'nome': 'Mary',
    'hp': 4
}

em_combate = False
inimigo_aparece = False
em_evento = False
sala_evento = None
ultima_rolagem = None

if inimigo_aparece:
    em_combate = True

LARGURA = 1920
ALTURA = 1080
BRANCO = (255,255,255)
CINZA = (128, 128, 128)
PRETO = (0,0,0)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('CP2')

clock = pygame.time.Clock()
fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 50)

texto_menu = fonte_menu.render('The Visit', True, BRANCO)
texto_combate = fonte_geral.render('[E] Exorcizar', True, BRANCO)

textos_ruins = [fonte_geral.render('Você não consegue cumprir sua', True, BRANCO),
                    fonte_geral.render('missão de exorcizar Mary...', True, BRANCO),
                    fonte_geral.render('A alma dela nunca encontrará descanso', True, BRANCO),
                    fonte_geral.render('e você é o culpado.', True, BRANCO)]

textos_bons = [fonte_geral.render('Você cumpre sua missão de', True, BRANCO),
                fonte_geral.render('salvar a alma de Mary...', True, BRANCO),
                fonte_geral.render('Agora ela poderá começar uma nova vida', True, BRANCO),
                fonte_geral.render('e encontrar o descanso eterno.', True, BRANCO)]

botoes = [fonte_geral.render('Jogar', True, BRANCO), fonte_geral.render('Sair', True, BRANCO)]

sotao = pygame.image.load('./images/attic.png').convert()
porao = pygame.image.load('./images/basement.png').convert()
cozinha = pygame.image.load('./images/kitchen.png').convert()
sala = pygame.image.load('./images/living-room.png').convert()
menu_image = pygame.image.load('./images/house-exterior.png').convert()
quarto_filha = pygame.image.load('./images/daughter-room.png').convert()
hall_entrada = pygame.image.load('./images/entrance-hall.png').convert()
quarto_pais = pygame.image.load('./images/parents-bedroom.png').convert()
corredor_andar2 = pygame.image.load('./images/upstairs-hallway.png').convert()
garota_sotao = pygame.image.load('./images/girl/girl_attic.png').convert()
garota_porao = pygame.image.load('./images/girl/girl_basement.png').convert()
garota_cozinha = pygame.image.load('./images/girl/girl_kitchen.png').convert()
garota_sala = pygame.image.load('./images/girl/girl_living_room.png').convert()
garota_quarto_pais = pygame.image.load('./images/girl/girl_parents_bedroom.png').convert()
garota_quarto_filha = pygame.image.load('./images/girl/girl_bedroom.png').convert()
garota_diario_original = pygame.image.load('./images/girl/girl_diary.png').convert()
garota_diario = pygame.transform.scale(garota_diario_original, (450, 650))
garota_foto_original = pygame.image.load('./images/girl/girl_photo.png').convert()
garota_foto = pygame.transform.scale(garota_foto_original, (450, 498))

som_porta_geral = pygame.mixer.Sound('./sfx/opening_default_door.mp3')
som_porta_menu = pygame.mixer.Sound('./sfx/opening_main_door.mp3')
som_escada = pygame.mixer.Sound('./sfx/stairs_footsteps.mp3')
som_acerto = pygame.mixer.Sound('./sfx/girl_hurt_sound.mp3')
som_passos = pygame.mixer.Sound('./sfx/footsteps.mp3')
som_risada = pygame.mixer.Sound('./sfx/girl_laught.mp3')
som_ambiente = './sfx/ambiance.mp3'

no_fim = False
no_menu = True
na_sala = False
no_porao = False
no_sotao = False
na_cozinha = False
garota_spawn = False
no_quarto_pais = False
no_quarto_filha = False
no_segundo_andar = False
no_primeiro_andar = False
mostrar_foto_garota = False
mostrar_diario_garota = False

fechar_diario_garota = pygame.Rect(702,20,50,50)
fechar_foto_garota = pygame.Rect(702,20,50,50)

pode_clicar = True
timer = None

try:
    pygame.mixer.music.load('./sfx/menu_music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
except pygame.error as e:
    print(f'Erro ao carregar musica {e}')

def mudar_musica_menu():
    pygame.mixer.music.stop()

    if not no_menu:
        pygame.mixer.music.load(som_ambiente)
    else:
        pygame.mixer.music.load('./sfx/menu_music.mp3')

    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    som_porta_menu.play()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if mostrar_diario_garota:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if fechar_diario_garota.collidepoint(evento.pos):
                    mostrar_diario_garota = False
            continue

        if mostrar_foto_garota:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if fechar_foto_garota.collidepoint(evento.pos):
                    mostrar_foto_garota = False
            continue

        if evento.type == pygame.MOUSEBUTTONDOWN and pode_clicar:
            if no_menu:
                no_menu = verificar_iniciar_jogo(None, evento)

                if not no_menu:
                    mudar_musica_menu()
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
                    garota_spawn = checar_encontro()
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
                    garota_spawn = checar_encontro()
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

                if verificar_mesa_quarto_pais(evento):
                    mostrar_foto_garota = True
            elif no_quarto_filha:
                no_segundo_andar = verificar_retornar_a1(evento, 'D')
                x, y = evento.pos

                if no_segundo_andar:
                    no_quarto_filha = False

                if verificar_mesa_quarto_filha(evento):
                    mostrar_diario_garota = True

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
            garota_spawn = checar_encontro()
        elif timer[1] == 'Porao' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            no_porao = True
            garota_spawn = checar_encontro()
        elif timer[1] == 'Sotao' and pygame.time.get_ticks() - timer[0] >= 2000:
            timer = None
            no_sotao = True
            garota_spawn = checar_encontro()
        elif timer[1] == 'Fim' and pygame.time.get_ticks() - timer[0] >= 10000:
            timer = None

            no_fim = False
            no_menu = True

            jogador['hp'] = 3
            inimigo['hp'] = 4

            garota_spawn = False

            na_sala = False
            na_cozinha = False
            no_porao = False
            no_sotao = False
            no_quarto_pais = False
            no_quarto_filha = False
            no_segundo_andar = False
            no_primeiro_andar = False

            mudar_musica_menu()
        pode_clicar = True
        pygame.event.clear(pygame.MOUSEBUTTONDOWN)

    tecla_pressionada = pygame.key.get_pressed()

    if no_menu:
        no_menu = verificar_iniciar_jogo(tecla_pressionada)

        (na_sala, no_primeiro_andar, no_segundo_andar, na_cozinha, no_porao, no_quarto_pais, no_sotao, no_quarto_filha,
         mostrar_diario_garota, mostrar_foto_garota) = (
            False, False, False, False, False, False, False, False, False, False)

        if not no_menu:
            mudar_musica_menu()
            no_primeiro_andar = True

        garota_spawn = False
        gerenciar_menu(botoes, fonte_geral, CINZA, BRANCO, PRETO, tela, menu_image, texto_menu)
    elif no_primeiro_andar:
        gerenciar_tela(tela, hall_entrada)
        garota_spawn = False
    elif na_sala:
        if garota_spawn:
            gerenciar_tela(tela, garota_sala, True)
        else:
            gerenciar_tela(tela, sala, True)
    elif na_cozinha:
        if garota_spawn:
            gerenciar_tela(tela, garota_cozinha)
        else:
            gerenciar_tela(tela, cozinha)
    elif no_porao:
        if garota_spawn:
            gerenciar_tela(tela, garota_porao)
        else:
            gerenciar_tela(tela, porao)
    elif no_segundo_andar:
        gerenciar_tela(tela, corredor_andar2)
        garota_spawn = False
    elif no_quarto_pais:
        if garota_spawn:
            gerenciar_tela(tela, garota_quarto_pais)
        else:
            gerenciar_tela(tela, quarto_pais)
    elif no_sotao:
        if garota_spawn:
            gerenciar_tela(tela, garota_sotao)
        else:
            gerenciar_tela(tela, sotao)
    elif no_quarto_filha:
        if garota_spawn:
            gerenciar_tela(tela, garota_quarto_filha)
        else:
            gerenciar_tela(tela, quarto_filha)

    if not no_menu and not garota_spawn and not no_fim:
        no_menu = verificar_tecla_pressionada(tecla_pressionada, True)

        if no_menu:
            mudar_musica_menu()

    if mostrar_diario_garota and no_quarto_filha:
        gerenciar_tela(tela, garota_diario)
        texto_x = fonte_geral.render('X', True, (255, 255, 255))
        tela.blit(texto_x, (fechar_diario_garota.x + 12, fechar_diario_garota.y + 2))

    if mostrar_foto_garota and no_quarto_pais:
        gerenciar_tela(tela, garota_foto)
        texto_x = fonte_geral.render('X', True, (255, 255, 255))
        tela.blit(texto_x, (fechar_foto_garota.x + 12, fechar_foto_garota.y + 2))

    if garota_spawn:
        pode_clicar = False
        ganhador = gerenciar_combate(tela, texto_combate, tecla_pressionada)

        if ganhador is not None:
            if ganhador == 'Jogador':
                inimigo['hp'] -= 1
                som_acerto.play()
            else:
                jogador['hp'] -= 1
                som_risada.play()

            pode_clicar = True
            garota_spawn = False

    if no_fim:
        tela.fill(PRETO)
        altura = 100

        if jogador['hp'] <= 0:
            for texto in textos_ruins:
                tela.blit(texto, (236, altura))
                altura += 100
        elif inimigo['hp'] <= 0:
            for texto in textos_bons:
                tela.blit(texto, (236, altura))
                altura += 100

    if jogador['hp'] <= 0 and not no_fim:
        timer = [pygame.time.get_ticks(), 'Fim']
        pode_clicar = False
        no_fim = True
    elif inimigo['hp'] <= 0 and not no_fim:
        timer = [pygame.time.get_ticks(), 'Fim']
        pode_clicar = False
        no_fim = True

    pygame.display.flip()
    clock.tick(60)