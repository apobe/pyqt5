
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QLineEdit
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class toplu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.sil=QPushButton("Resmi Sil")
        self.resimbuton=QLabel()
        self.resimac=QPushButton("Resim Aç")
        self.foto1=QLabel()
        self.foto=QPixmap("indir.png").scaled(250,200)
        self.foto1.setPixmap(self.foto)
        self.benimmail=QLabel("abdullahaykal104@gmail.com")
        self.benimsifrem=QLabel("imvhaexvtjnpqrfw")
        self.yazi=QLabel()
        self.yazı_alani=QTextEdit()
        self.yazı=QLabel("Gönderilecek e postaları yazınız :")
        self.gonder=QPushButton("Gönder")
        self.cıkıs=QPushButton("Çıkış")
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Aç")
        self.mail=QLineEdit()
        v_box=QVBoxLayout()
        v_box.addWidget(self.foto1)
        v_box.addWidget(self.resimbuton)
        v_box.addStretch()
        v_box.addWidget(self.yazı_alani)
        v_box.addStretch()
        v_box.addWidget(self.yazı)
        v_box.addStretch()
        v_box.addWidget(self.mail)
        v_box.addWidget(self.yazi)
        h_box=QHBoxLayout()
        h_box.addWidget(self.gonder)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.resimac)
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.sil)
        h_box.addWidget(self.cıkıs)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle('****Mail Spam Uyglaması****')
        self.gonder.clicked.connect(self.click)
        self.ac.clicked.connect(self.click)
        self.temizle.clicked.connect(self.click)
        self.cıkıs.clicked.connect(self.click)
        self.resimac.clicked.connect(self.click)
        self.sil.clicked.connect(self.click)
        self.setGeometry(150,100,400,100)
        self.show()

    def click(self):
        sender=self.sender()
        if sender.text()=="Gönder":
            while True:
                msj=MIMEMultipart()
                yazi = self.yazı_alani.toPlainText()
                govde = MIMEText(yazi, 'plain')
                msj.attach(govde)
                try:
                    maill = smtplib.SMTP('smtp.gmail.com', 587)
                    maill.ehlo()
                    maill.starttls()
                    maill.login(self.benimmail.text(),self.benimsifrem.text())
                    email_addresses = self.mail.text().split(",")
                    for email_address in email_addresses:
                        maill.sendmail(self.benimmail.text(),email_address.strip(), msj.as_string())
                    maill.close()
                    self.yazi.setText("Gönderildi")
                except:
                    self.yazi.setText('Hatalı')
        elif sender.text()=="Aç":
            dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
            with open(dosya_ismi[0],"r",encoding="utf-8") as file:
                self.yazı_alani.setText(file.read())
        elif sender.text()=="Temizle":
            self.yazı_alani.clear() 
        elif sender.text()=="Resim Aç":
            dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
            asıl=dosya_ismi[0]
            pixmap = QPixmap(asıl).scaled(250, 200)
            self.resimbuton.setPixmap(pixmap)
        elif sender.text()=="Resmi Sil":
            self.resimbuton.clear()
        else:
            qApp.exit()
            
app=QApplication(sys.argv)
toplu1=toplu()
toplu1.show()
sys.exit(app.exec_())