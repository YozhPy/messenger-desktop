import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QMessageBox
from windows.voice_chat import Ui_VoiceChat


# Окно с настройками клиента
class VoiceRoomPanel(QtWidgets.QMainWindow):
    def __init__(self, parent=None, signal=None):
        super().__init__(parent)
        self.voice_chat_ui = Ui_VoiceChat()
        self.voice_chat_ui.setupUi(self)
        self.setWindowTitle("Voice chat")

        # Сигнал для возврата в интерфейс
        self.signal = signal

        self.voice_chat_ui.exit_btn.clicked.connect(self.exit_room)

        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

    def exit_room(self):
        self.signal.emit({'action': 'EXIT_ROOM', 'data': ""})

    # def send_message_to_chat(self):
    #     message_text = self.text_chat_ui.message.text()
    #     if message_text:
    #         self.signal.emit({'action': 'SEND_MESSAGE', 'data': message_text})
    #     else:
    #         message = "Enter smth to send!"
    #         QtWidgets.QMessageBox.about(self, "Error", message)

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Oh, we will miss you! Do you want to disconnect from voice room?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            self.signal.emit({'action': 'EXIT', 'data': ""})
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_panel = VoiceRoomPanel()
    login_panel.show()
    sys.exit(app.exec_())
