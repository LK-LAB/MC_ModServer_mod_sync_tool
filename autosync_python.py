from http import server
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from ui_main import Ui_Dialog
import qdarktheme

#window = loader.load("main_ui.ui", parentWidget=None)

class MainUIWidget(QMainWindow, Ui_Dialog):
    def __init__(self, parent = None, ui_file = None):
        super(MainUIWidget, self).__init__(parent)
        #if ui_file is not None:
        self. setupUi(self)
        self.sync_button.clicked.connect(self.sync_button_clicked)
        self.server_connect_button.clicked.connect(self.server_connect_clicked)

    def server_connect_clicked(self):
        server_ip = self.server_ip_input.text()
        server_port = self.server_port_input.text()
        print("connecting %s:%s"%(server_ip, server_port))
        self.output_area.appendPlainText("connecting %s:%s"%(server_ip, server_port))

    def sync_button_clicked(self):
        print("clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainUIWidget()
    app.setStyleSheet(qdarktheme.load_stylesheet("light"))
    myWindow.show()
    app.exec_()