import PySimpleGUI as sg
import server

# using PySimpleGUI as a GUI library draw a window with a button, when the button is clicked run a function that will connect to the server
def draw_window():
    layout = [[sg.Text('Connect to Server')],
              [sg.Input(key='host'), sg.Input(key='port', size=(5, 1), default_value='10000')],
              [sg.Button('Connect')]]
    window = sg.Window('Client', layout)
    while True:
        event, values = window.read()
        if event == 'Connect':
            server.connect(values['host'], values['port'])
            break
    window.close()



def main():
    draw_window()


if __name__ == '__main__':
    main()
