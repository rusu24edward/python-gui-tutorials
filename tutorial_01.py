# tutorial_01.py - simple event loop

import PySimpleGUI as sg

layout = [[sg.Text("Christ is risen!")], [sg.Button("Indeed He is risen")]]

main_window = sg.Window("Resurrection", layout)

# GUI needs to run inside event loop. All events are processed in this loop
while True:
    event, values = main_window.read()
    if event == "Indeed He is risen" or event == sg.WIN_CLOSED:
        break

main_window.close()
