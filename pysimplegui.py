from PySimpleGUI import PySimpleGUI as sg

#layout
theme_name_list = sg.theme_list()
print(theme_name_list)
sg.theme('Reds')
layout = [
    [sg.Text('Usuário'),sg.Input(key = 'usuario',size=(20,2))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*',size=(20,2))],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]


]
#Janela
janela = sg.Window('Tela de Login', layout)

#Ler Usuarios

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'Ricardo' and valores ['senha'] == '123456':
            print("Bem vindo a minha primeira janela")
        else:
            print("Usuario ou senha nao cadastrados")
