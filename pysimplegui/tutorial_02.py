# tutorial_02.py - image viewer

import os

import PySimpleGUI as sg

## Build the layout: two main columns

# key parameter is used to identify specific element in the GUI
# enable_events parameter turns on/off events for an element

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(
            default_text="/home/eddie/coding/abmarl/docs/src/.images",
            size=(25, 1),
            enable_events=True,
            key="-FOLDER-"
        ),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key='-FILE LIST-'
        )
    ]
]

image_viewer_column = [
    [sg.Text("Choose an image from the list on the left.")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key='-IMAGE-')],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VerticalSeparator(),
        sg.Column(image_viewer_column)
    ]
]

## Create the window and run event loop
main_window = sg.Window("Image viewer", layout)
while True:
    # Event is the key string of whichever element the user interacts with
    # values is a dict mapping from the widget's key to some value
    event, values = main_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    elif event == "-FOLDER-": # User interacting with In box
        folder_value = values['-FOLDER-']
        try:
            file_list = os.listdir(folder_value)
        except:
            file_list = []

        file_names = [
            file_name for file_name in file_list
            if os.path.isfile(os.path.join(folder_value, file_name))
                and file_name.lower().endswith((".png", ".gif", ".jpg"))
        ]
        main_window["-FILE LIST-"].update(file_names)

    elif event == "-FILE LIST-": # File was chosen from listbox
        # try:
        # Join the current folder with the file that is selected
        file_name = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )
        # Display the path of the selected file
        main_window["-TOUT-"].update(file_name)
        # Display the image
        main_window["-IMAGE-"].update(filename=file_name)
        # except:
        #     pass

main_window.close()
