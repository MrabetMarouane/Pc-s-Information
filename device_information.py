#Merci d'installer les bibliotheques necéssaires (pip install + nom de la bibliotheque)

from PySide6 import QtWidgets
import socket
import urllib.request
import uuid
import platform

# Récupérer l'adresse IP locale
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
local_ip_address = s.getsockname()[0]

# Récupérer l'adresse IP externe
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# Récupérer l'adresse MAC
mac_address = uuid.getnode()
mac_address_hex = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0, 8*6, 8)][::-1])

# Récupérer le nom du système d'exploitation
os = platform.system()


class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computer Information")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()

        self.set_data()

    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel('Computer Information')
        self.lbl_title.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.lbl_hostname = QtWidgets.QLabel('Hostname:')
        self.lbl_LAN = QtWidgets.QLabel('LAN IP Address:')
        self.lbl_MAC = QtWidgets.QLabel('MAC Address:')
        self.lbl_WAN = QtWidgets.QLabel('WAN IP Address:')
        self.lbl_System = QtWidgets.QLabel('System:')

        self.LEdit_hostname = QtWidgets.QLineEdit()
        self.LEdit_hostname.setReadOnly(True)
        self.LEdit_LAN = QtWidgets.QLineEdit()
        self.LEdit_LAN.setReadOnly(True)
        self.LEdit_MAC = QtWidgets.QLineEdit()
        self.LEdit_MAC.setReadOnly(True)
        self.LEdit_WAN = QtWidgets.QLineEdit()
        self.LEdit_WAN.setReadOnly(True)
        self.LEdit_System = QtWidgets.QLineEdit()
        self.LEdit_System.setReadOnly(True)

        self.btn_Exit = QtWidgets.QPushButton("Exit")
        self.btn_Exit.clicked.connect(self.close)

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()

    def add_widgets_to_layouts(self):
        self.layoutH0.addWidget(self.lbl_title)

        self.layoutH1.addWidget(self.lbl_hostname)
        self.layoutH1.addWidget(self.LEdit_hostname)

        self.layoutH2.addWidget(self.lbl_LAN)
        self.layoutH2.addWidget(self.LEdit_LAN)

        self.layoutH3.addWidget(self.lbl_MAC)
        self.layoutH3.addWidget(self.LEdit_MAC)

        self.layoutH4.addWidget(self.lbl_WAN)
        self.layoutH4.addWidget(self.LEdit_WAN)

        self.layoutH5.addWidget(self.lbl_System)
        self.layoutH5.addWidget(self.LEdit_System)

        self.layoutH6.addWidget(self.btn_Exit)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)
        self.setLayout(self.layoutV)

    def set_data(self):
        self.LEdit_hostname.setText(platform.node())
        print(platform.node())

        self.LEdit_LAN.setText(local_ip_address)
        print(f"IP Address: {local_ip_address}")

        self.LEdit_MAC.setText(mac_address_hex)
        print(f"The MAC adress is :{mac_address_hex}")

        self.LEdit_WAN.setText(external_ip)
        print(f"The MAC adress is :{external_ip}")


        self.LEdit_System.setText(os)
        print("Your OS is : ", os)


app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()

