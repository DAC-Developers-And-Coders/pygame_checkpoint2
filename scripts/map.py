from scripts.assets import imagens
import scripts.game_state as gs

lugar_atual = 'Menu'
overlay_ativo = None

lugares = {
    'Inicio': {
        'imagem': imagens['hall_entrada'],
        'imagem_garota': None,
    },

    'Sala': {
        'imagem': imagens['sala'],
        'imagem_garota': imagens['garota_sala'],

        'overlay_foto_familia': {
            'imagem': imagens['familia_foto'],
            'fechar': gs.fechar_foto_familia
        }
    },

    'Cozinha': {
        'imagem': imagens['cozinha'],
        'imagem_garota': imagens['garota_cozinha'],
    },

    'Porao': {
        'imagem': imagens['porao'],
        'imagem_garota': imagens['garota_porao'],

        'overlay_documento_padre': {
            'imagem': imagens['documento_padre'],
            'fechar': gs.fechar_documento_padre
        }
    },

    'SegundoAndar': {
        'imagem': imagens['corredor_andar2'],
        'imagem_garota': None,
    },

    'QuartoPais': {
        'imagem': imagens['quarto_pais'],
        'imagem_garota': imagens['garota_quarto_pais'],

        'overlay_foto_garota': {
            'imagem': imagens['garota_foto'],
            'fechar': gs.fechar_foto_garota
        }
    },

    'Sotao': {
        'imagem': imagens['sotao'],
        'imagem_garota': imagens['garota_sotao'],

        'overlay_mary': {
            'imagem': imagens['cruz_mary'],
            'fechar': gs.fechar_cruz_mary
        },

        'overlay_rosalia': {
            'imagem': imagens['cruz_rosalia'],
            'fechar': gs.fechar_cruz_rosalia
        },

        'overlay_william': {
            'imagem': imagens['cruz_william'],
            'fechar': gs.fechar_cruz_william
        }
    },

    'QuartoFilha': {
        'imagem': imagens['quarto_filha'],
        'imagem_garota': imagens['garota_quarto_filha'],

        'overlay_diario': {
            'imagem': imagens['garota_diario'],
            'fechar': gs.fechar_diario_garota
        },

        'overlay_foto': {
            'imagem': imagens['foto_mary_julia'],
            'fechar': gs.fechar_foto_mary_julia
        }
    }
}
# endregion