from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, qApp,QTextEdit
import sys
import requests
from bs4 import BeautifulSoup
class veri_alma(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.random=QPushButton("random")
        self.temizle=QPushButton("Temizle")
        self.gon=QLabel("")
        self.buton=QPushButton("Ezan bilgileri için ıklayınız")
        self.buton1 = QPushButton("Döviz bilgileri için tıklayınız")
        self.buton2=QPushButton("Çıkış")
        self.byk_yazi=QTextEdit()
        h_box=QHBoxLayout()
        h_box.addWidget(self.gon)
        h_box.addWidget(self.byk_yazi)
        h_box.addStretch()
        h_box.addWidget(self.buton)
        h_box.addWidget(self.buton1)
        h_box.addWidget(self.buton2)
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.random)
        v_box=QVBoxLayout()
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("**İNTERTTEN VERİ ALMA**")
        self.random.clicked.connect(self.click)
        self.buton.clicked.connect(self.click)
        self.buton1.clicked.connect(self.click)
        self.buton2.clicked.connect(self.click)
        self.temizle.clicked.connect(self.click)
        self.show()

    def click(self):
        sender=self.sender()
        if sender.text()=="Ezan bilgileri için ıklayınız":
            url="https://www.sabah.com.tr/diyarbakir-namaz-vakitleri"
            a=requests.get(url)
            b=a.content
            c=BeautifulSoup(b,"html.parser")
            d=c.find_all("table")
            for i in d:
                self.byk_yazi.setText(i.text.strip())
        elif sender.text()=="Döviz bilgileri için tıklayınız":
            url="https://www.doviz.com/"
            f=requests.get(url)
            g=f.content
            h=BeautifulSoup(g,"html.parser")
            j=h.find_all("div",{"class":"market-data"})
            for k in j:
                self.byk_yazi.setText(k.text.strip())
        elif sender.text()=="Çıkış":
            qApp.exit()
        elif sender.text()=="random":
            url="https://www.chess.com/game/live/73070644213"
            a=requests.get(url)
            b=a.content
            c=BeautifulSoup(b,"html.parser")
            d=c.find_all("span",{"class","tabs-label"})
            for i in d:
                self.byk_yazi.setText(i.text.strip())
        else:
            self.byk_yazi.clear()
app=QApplication(sys.argv)
veri1=veri_alma()
sys.exit(app.exec_())
