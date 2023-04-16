# Tutorial 04 - Using openCV

import cv2
import numpy as np
import PySimpleGUI as sg

def main():
    sg.theme('LightGreen')

    # First, we have a layout for displaying the image and for controlling the
    # image modifications available in cv2.
    layout = [
        [sg.Text("OpenCV Demo", size=(60, 1), justification='center')],
        [sg.Image(filename="", key='_IMAGE_')],
        [sg.Radio("None", "Radio", True, size=(10, 1))],
        [
            sg.Radio("threshold", "Radio", size=(10, 1), key="_THRESH_"),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(40, 15),
                key="_THRESH_SLIDER_"
            )
        ],
        [
            sg.Radio("canny", "Radio", size=(10, 1), key="_CANNY_"),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation='h',
                size=(20, 15),
                key="_CANNY_SLIDER_A_"
            ),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation='h',
                size=(20, 15),
                key="_CANNY_SLIDER_B_"
            )
        ],
        [
            sg.Radio("blur", "Radio", size=(10, 1), key="_BLUR_"),
            sg.Slider(
                (1, 11),
                1,
                1,
                orientation='h',
                size=(40, 15),
                key="_BLUR_SLIDER_"
            )
        ],
        [
            sg.Radio("hue", "Radio", size=(10, 1), key="_HUE_"),
            sg.Slider(
                (0, 255),
                0,
                1,
                orientation='h',
                size=(40, 15),
                key="_HUE_SLIDER_"
            )
        ],
        [
            sg.Radio("enhance", "Radio", size=(10, 1), key="_ENHANCE_"),
            sg.Slider(
                (1, 255),
                128,
                1,
                orientation='h',
                size=(40, 15),
                key="_ENHANCE_SLIDER_"
            )
        ],
        [sg.Button("All Done", size=(10, 1))]
    ]

    # The image source is going to be a video capture.
    window = sg.Window("OpenCV Integration", layout, location=(800, 400))
    cap = cv2.VideoCapture(0)

    # The event loop will grab the frame and modify it according to the configuration
    # in the layout controls.
    while True: # Event loop
        event, values = window.read(timeout=20)
        if event == "All Done" or event == sg.WIN_CLOSED:
            break

        ref, frame = cap.read()

        if values["_THRESH_"]:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)[:, :, 0]
            frame = cv2.threshold(
                frame, values["_THRESH_SLIDER_"], 255, cv2.THRESH_BINARY
            )[1]
        elif values["_CANNY_"]:
            frame = cv2.Canny(
                frame, values["_CANNY_SLIDER_A_"], values["_CANNY_SLIDER_B_"]
            )
        elif values["_BLUR_"]:
            frame = cv2.GaussianBlur(frame, (21, 21), values["_BLUR_SLIDER_"])
        elif values["_HUE_"]:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            frame[:, :, 0] += int(values["_HUE_SLIDER_"])
            frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        elif values["_ENHANCE_"]:
            enhance_value = values["_ENHANCE_SLIDER_"] / 40
            clahe = cv2.createCLAHE(clipLimit=enhance_value, tileGridSize=(8, 8))
            lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        # Now that the frame object has been modified, we display the result in
        # the image part of the layout
        image_bytes = cv2.imencode(".png", frame)[1].tobytes()
        window["_IMAGE_"].update(data=image_bytes)

    window.close()

main()
