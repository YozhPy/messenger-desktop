import time
import pickle
from PyQt5 import QtCore
import threading

# Мониторинг входящих сообщений
class message_monitor(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(dict)
    server_socket = None

    def __init__(self, parent=None):
        self.send_voice_thread = threading.Thread(target=self.send_voice)
        self.stop_send_voice_thread = True
        QtCore.QThread.__init__(self, parent)

    def run(self):
        print(f'server_socket: {self.server_socket}')

        while True:
            if self.server_socket != None:
                message = self.server_socket.recv(256000)
                pickle_dec = pickle.loads(message)
                print(pickle_dec)
                self.mysignal.emit(pickle_dec)

            # time.sleep(.001)

    # Отправить зашифрованное сообщение на сервер
    def send_encrypt(self, payload: dict):
        # if payload.get('action', None) in ['REGISTER', 'LOGIN']:
        #     payload['data'] = [credential for credential in payload['data']]

        if payload['action'] == 'SEND_VOICE':
            if self.stop_send_voice_thread != False:
                self.stop_send_voice_thread = False
                self.send_voice_thread.start()
            self.server_socket.send(pickle.dumps(payload))
        else:
            self.server_socket.send(pickle.dumps(payload))

        if payload ['action'] == 'EXIT_ROOM' and not self.stop_send_voice_thread:
            self.stop_send_voice_thread = True


    def send_voice(self):
        while not self.stop_send_voice_thread:
            self.mysignal.emit({'action': "SEND_VOICE", 'data': ''})
            time.sleep(.2)

