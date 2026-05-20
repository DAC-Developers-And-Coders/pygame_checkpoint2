import pygame

jogador = {
    'nome': 'John',
    'full_hp' : 3,
    'hp': 3
}

inimigo = {
    'nome': 'Mary',
    'full_hp' : 4,
    'hp': 4
}

timer = None
no_fim = False
pode_clicar = True
timer_batalha = None
garota_spawn = False

fechar_diario_garota = pygame.Rect(702,20,50,50)
fechar_foto_garota = pygame.Rect(702,20,50,50)
fechar_foto_familia = pygame.Rect(702,20,50,50)
fechar_foto_mary_julia = pygame.Rect(702,20,50,50)
fechar_cruz_mary = pygame.Rect(702,20,50,50)
fechar_cruz_rosalia = pygame.Rect(702,20,50,50)
fechar_cruz_william = pygame.Rect(702,20,50,50)
fechar_documento_padre = pygame.Rect(702,20,50,50)