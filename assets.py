import pygame
import constants as const

imagens = {
    'sotao' : pygame.image.load('./images/attic.png').convert(),
    'porao' : pygame.image.load('./images/basement.png').convert(),
    'cozinha' : pygame.image.load('./images/kitchen.png').convert(),
    'sala' : pygame.image.load('./images/living-room.png').convert(),
    'menu_imagem' : pygame.image.load('./images/house-exterior.png').convert(),
    'quarto_filha' : pygame.image.load('./images/daughter-room.png').convert(),
    'hall_entrada' : pygame.image.load('./images/entrance-hall.png').convert(),
    'quarto_pais' : pygame.image.load('./images/parents-bedroom.png').convert(),
    'corredor_andar2' : pygame.image.load('./images/upstairs-hallway.png').convert(),
    'garota_sotao' : pygame.image.load('./images/girl/girl_attic.png').convert(),
    'garota_porao' : pygame.image.load('./images/girl/girl_basement.png').convert(),
    'garota_cozinha' : pygame.image.load('./images/girl/girl_kitchen.png').convert(),
    'garota_sala' : pygame.image.load('./images/girl/girl_living_room.png').convert(),
    'garota_quarto_pais' : pygame.image.load('./images/girl/girl_parents_bedroom.png').convert(),
    'garota_quarto_filha' : pygame.image.load('./images/girl/girl_bedroom.png').convert(),
    'garota_diario' : pygame.image.load('./images/girl/girl_diary.png').convert(),
    'garota_foto' : pygame.image.load('./images/girl/girl_photo.png').convert(),
    'familia_foto' : pygame.image.load('./images/girl/family_photo.png').convert(),
    'foto_mary_julia' : pygame.image.load('./images/girl/mary_and_julia.png').convert(),
    'cruz_mary' : pygame.image.load('./images/girl/mary_cross.png').convert(),
    'cruz_rosalia' : pygame.image.load('./images/girl/rosalia_cross.png').convert(),
    'cruz_william' : pygame.image.load('./images/girl/william_cross.png').convert(),
    'documento_padre' : pygame.image.load('./images/girl/priest_document.png').convert()
}

imagens['garota_diario'] = pygame.transform.scale(imagens['garota_diario'], (450, 650))
imagens['garota_foto'] = pygame.transform.scale(imagens['garota_foto'], (450, 498))
imagens['familia_foto'] = pygame.transform.scale(imagens['familia_foto'], (450, 498))
imagens['foto_mary_julia'] = pygame.transform.scale(imagens['foto_mary_julia'], (450, 498))
imagens['cruz_mary'] = pygame.transform.scale(imagens['cruz_mary'], (450, 498))
imagens['cruz_rosalia'] = pygame.transform.scale(imagens['cruz_rosalia'], (450, 498))
imagens['cruz_william'] = pygame.transform.scale(imagens['cruz_william'], (450, 498))
imagens['documento_padre'] = pygame.transform.scale(imagens['documento_padre'], (450, 650))

fonte_menu = pygame.font.Font('./fonts/NightsideDemoRegular.ttf', 100)
fonte_geral = pygame.font.Font('./fonts/DevilCandle.otf', 50)
fonte_pequena = pygame.font.Font('./fonts/DevilCandle.otf', 30)
fonte_numeros = pygame.font.SysFont('arial', 30)

texto_x = fonte_geral.render('X', True, const.BRANCO)
texto_menu = fonte_menu.render('The Visit', True, const.BRANCO)
texto_combate = fonte_geral.render('[E] Exorcizar', True, const.BRANCO)

textos_ruins = [fonte_geral.render('Você não consegue cumprir sua', True, const.BRANCO),
                    fonte_geral.render('missão de exorcizar Mary...', True, const.BRANCO),
                    fonte_geral.render('A alma dela nunca encontrará descanso', True, const.BRANCO),
                    fonte_geral.render('e você é o culpado.', True, const.BRANCO)]

textos_bons = [fonte_geral.render('Você cumpre sua missão de', True, const.BRANCO),
                fonte_geral.render('salvar a alma de Mary...', True, const.BRANCO),
                fonte_geral.render('Agora ela poderá começar uma nova vida', True, const.BRANCO),
                fonte_geral.render('e encontrar o descanso eterno.', True, const.BRANCO)]

botoes = [fonte_geral.render('Jogar', True, const.BRANCO), fonte_geral.render('Sair', True, const.BRANCO)]

som_porta_geral = pygame.mixer.Sound('./sfx/opening_default_door.mp3')
som_porta_menu = pygame.mixer.Sound('./sfx/opening_main_door.mp3')
som_escada = pygame.mixer.Sound('./sfx/stairs_footsteps.mp3')
som_acerto = pygame.mixer.Sound('./sfx/girl_hurt_sound.mp3')
som_passos = pygame.mixer.Sound('./sfx/footsteps.mp3')
som_risada = pygame.mixer.Sound('./sfx/girl_laught.mp3')
som_ambiente = './sfx/ambiance.mp3'