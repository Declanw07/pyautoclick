import sys

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from pyautoclick.settings import APPLICATION_NAME
from pyautoclick.backend.windows import get_processes


class Main(QtWidgets.QMainWindow):
    """
    The main application UI window.
    """

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setObjectName(APPLICATION_NAME)
        self.setWindowTitle(APPLICATION_NAME)
        self.resize(540, 150)

        self.window_combo = QtWidgets.QComboBox()
        self.click_button_combo = QtWidgets.QComboBox()
        self.hold_click_checkbox = QtWidgets.QCheckBox()
        self.click_delay_spinbox = QtWidgets.QSpinBox()
        self.start_stop_pushbutton = QtWidgets.QPushButton()

        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.addRow('Window:', self.window_combo)
        self.form_layout.addRow('Click Button:', self.click_button_combo)
        self.form_layout.addRow('Hold Click:', self.hold_click_checkbox)
        self.form_layout.addRow('Click Delay (ms):', self.click_delay_spinbox)

        self.grid_layout = QtWidgets.QGridLayout()

        self.grid_layout.addLayout(self.form_layout, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.start_stop_pushbutton, 1, 0, 1, 2)

        widget = QtWidgets.QWidget()
        widget.setLayout(self.grid_layout)
        self.setCentralWidget(widget)

        self.populate_windows()

    def populate_windows(self):
        for process in sorted(get_processes(), key=lambda x: x.pid):
            self.window_combo.addItem(
                '{_name} - PID: {_pid}'.format(**process.__dict__)
            )


def run():
    """
    Main entry point to run the application
    """
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    run()
