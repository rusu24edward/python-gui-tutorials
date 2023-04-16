# tutorial_01.py - Basics of PyQt

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("PyQt Application")
main_window.setGeometry(100, 100, 280, 80) # location, size
msg = QLabel("<h1>Christ is risen!</h1>", parent=main_window)
msg.move(40, 20) # Coordinate in parent window

# Any widget can be the top-level window, as long as it doesn't have a parent.
# When a widget is a top-level window, PyQT provides a title bar and turns it
# into a normal window. So unlesss you want your widget to have its own window,
# then you have to specify a parent

main_window.show() # Schedules a "paint event"
sys.exit(app.exec()) # Run application's event loop. Wrap in sys exit to ensure
# that the resources are cleanly released
