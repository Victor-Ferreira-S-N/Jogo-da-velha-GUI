"""
Jogo da Velha em Janela Gráfica usando PyAutoGUI

"""

import PySimpleGUI as sg
sg.theme('LightBlue')

x_image = "X.png"
o_image = "o.png"
empty = "empty.png"
vez = 1

def gera_tabuleiro():  # Tabuleiro para fins de verificação de jogada e resultado
    tabuleiro = [' ', ' ', ' ',
                 ' ', ' ', ' ',
                 ' ', ' ', ' ']
    return tabuleiro


def verifica_jogada(tabuleiro, posicao):  # Verifica se o campo a ser preenchido está vazio
    if tabuleiro[posicao] == ' ':
        return True
    else:
        return False


def verifica_resultado(tabuleiro):  # Verifica se há um vencedor, se "deu velha" ou se o jogo deve prosseguir
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] and tabuleiro[0] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[0]} Venceu!')
        return True
    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5] and tabuleiro[3] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[3]} Venceu!')
        return True
    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8] and tabuleiro[6] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[6]} Venceu!')
        return True
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6] and tabuleiro[0] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[0]} Venceu!')
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] and tabuleiro[1] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[1]} Venceu!')
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] and tabuleiro[2] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[2]} Venceu!')
        return True
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[0]} Venceu!')
        return True
    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2] != ' ':
        window['-OUTPUT-'].update(f'Jogador {tabuleiro[2]} Venceu!')
        return True
    else:
        if not ' ' in tabuleiro:
            window['-OUTPUT-'].update('Deu velha!')
            return True
        else:
            return False


def joga_x():
    if event == '0': window['0'].update(image_filename=x_image, image_subsample=5)
    if event == '1': window['1'].update(image_filename=x_image, image_subsample=5)
    if event == '2': window['2'].update(image_filename=x_image, image_subsample=5)
    if event == '3': window['3'].update(image_filename=x_image, image_subsample=5)
    if event == '4': window['4'].update(image_filename=x_image, image_subsample=5)
    if event == '5': window['5'].update(image_filename=x_image, image_subsample=5)
    if event == '6': window['6'].update(image_filename=x_image, image_subsample=5)
    if event == '7': window['7'].update(image_filename=x_image, image_subsample=5)
    if event == '8': window['8'].update(image_filename=x_image, image_subsample=5)
    return event


def joga_o():
    if event == '0': window['0'].update(image_filename=o_image, image_subsample=5)
    if event == '1': window['1'].update(image_filename=o_image, image_subsample=5)
    if event == '2': window['2'].update(image_filename=o_image, image_subsample=5)
    if event == '3': window['3'].update(image_filename=o_image, image_subsample=5)
    if event == '4': window['4'].update(image_filename=o_image, image_subsample=5)
    if event == '5': window['5'].update(image_filename=o_image, image_subsample=5)
    if event == '6': window['6'].update(image_filename=o_image, image_subsample=5)
    if event == '7': window['7'].update(image_filename=o_image, image_subsample=5)
    if event == '8': window['8'].update(image_filename=o_image, image_subsample=5)
    return event


def game_window():
    layout = [
        [sg.Push(), sg.Text(f'Jogador 1: X'), sg.Push(), sg.Text(f'Jogador 2: ◯'), sg.Push()],
        [sg.Push(), sg.Button('Jogar', k='-JOGAR-', tooltip='Iniciar o jogo'), sg.Push()],
        [sg.Push(),
         sg.Button(k='0', expand_x=True, image_source=empty, image_subsample=5),
         sg.Button(k='1', expand_x=True, image_source=empty, image_subsample=5),
         sg.Button(k='2', expand_x=True, image_source=empty, image_subsample=5),
         sg.Push()],
        [sg.Push(),
         sg.Button(k='3', expand_x=True, image_source=empty, image_subsample=5),
         sg.Button(k='4', expand_x=True, image_source=empty, image_subsample=5),
         sg.Button(k='5', expand_x=True, image_source=empty, image_subsample=5),
         sg.Push()],
        [sg.Push(),
         sg.Button(k='6', expand_x=True, image_source=empty, image_subsample=5),
         sg.Button(k='7', expand_x=True, image_source=empty, image_subsample=5),
         sg.Button(k='8', expand_x=True, image_source=empty, image_subsample=5),
         sg.Push()],
        [sg.Text('', k='-OUTPUT-'), sg.Push(), sg.Button('Reiniciar', k='-REINICIAR-', tooltip='Limpar o tabuleiro')]
    ]

    return sg.Window('Jogo da Velha', layout, size=(400, 420))


window = game_window()
tabuleiro = gera_tabuleiro()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-REINICIAR-':
        vez = 1
        window.close()
        tabuleiro = gera_tabuleiro()
        window = game_window()

    if event == '-JOGAR-':
        while not verifica_resultado(tabuleiro):
            if vez == -1:
                window['-OUTPUT-'].update('Vez de: Jogador 2 (o)')
            else:
                window['-OUTPUT-'].update('Vez de: Jogador 1 (x)')
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if vez == 1:
                if event in ['0','1','2','3','4','5','6','7','8']:
                    if not verifica_jogada(tabuleiro, int(event)):
                        window['-OUTPUT-'].update('Campo já preenchido.')
                    else:
                        tabuleiro[int(event)] = 'X'
                        joga_x()
                        vez = vez * -1  # Altera o sinal de 1
                else:
                    window['-OUTPUT-'].update('Jogada inválida, tente novamente.')
            else:
                if event in ['0','1','2','3','4','5','6','7','8']:
                    if not verifica_jogada(tabuleiro, int(event)):
                        window['-OUTPUT-'].update('Campo já preenchido.')
                    else:
                        tabuleiro[int(event)] = 'o'
                        joga_o()
                        vez = vez * -1  # Altera o sinal de 1


window.close()
