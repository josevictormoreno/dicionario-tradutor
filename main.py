import PySimpleGUI as sg
from tradutor import tradutor

sg.theme('Material1')
layout = [[sg.Text('Tradutor')],
          [sg.Text('Texto: '), sg.InputText()],
          [sg.Button('Traduzir', key='entrada'), sg.Button('Cancel')],
          [sg.Combo(['Portugues', 'Espanhol', 'Ingles', 'Frances', 'Italiano'], enable_events=True, key='combo')],
          [sg.Output(size=(40, 2))]]

window = sg.Window('Tradutor do ze', layout)
teste = ''
while True:
    event, values = window.read()
    teste = values[0]
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'entrada':
        print(tradutor(values[0], values['combo']))

window.close()