# tutorial_03.py - Using matplotlib

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import PySimpleGUI as sg

matplotlib.use("TkAgg")

# embed figure in PySimpleGUI canvas
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(
        side='top', fill='both', expand=1
    )
    return figure_canvas_agg

# Create figure
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, 0.01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# Create GUI window
layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="_CANVAS_")],
    [sg.Button("All done")]
]

main_window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18"
)

draw_figure(main_window["_CANVAS_"].TKCanvas, fig)
event, values = main_window.read() # Don't need loop because no interaction
main_window.close()
