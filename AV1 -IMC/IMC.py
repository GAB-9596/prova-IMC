import PySimpleGUI as sg

sg.theme('LightGrayl')  


layout = [ 
            [sg.Text('IMC')],
            [sg.Text('Massa'), sg.Input(key='-MASS-', size=(10,1))],
            [sg.Text('Altura'), sg.Input(key='-HIGH-', size=(10,1))],
            [sg.Button('Calcular')]
         ]


window = sg.Window('IMC', layout=layout, font="Monaco 18 ", element_justification='center')


while True:
    event, value = window.read()
    print(event, value)
    massa =  float(value['-MASS-'])
    altura = float(value['-HIGH-'])
    imc = massa/(altura**2)
    sg.Popup(f'Seu imc é {imc:.2f}',font='26')
    if event == sg.WIN_CLOSED or event == 'Exit':    
      break
window.close()
    
