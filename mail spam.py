import setuptools.errors
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, qApp, \
    QTextEdit
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import smtplib


class mail(QWidget):
    def __init__(self):
        super().__init__()

        self.init_uni()

    def init_uni(self):
        self.cikis=QPushButton("Çıkış")
        self.mail_konusu = QLineEdit()
        self.yazi5 = QLabel('imvhaexvtjnpqrfw')

        self.yazi4 = QLabel('abdullahaykal104@gmail.com')
        self.yazi_alani = QTextEdit('xxramazanxx31@gmail.com''\n'
                                    'abdullahaykal104@gmail.com''\n'
                                    'imvhaexvtjnpqrfw')
        self.yazi2 = QLabel('*Ne yazmak istersiniz*')
        self.buton = QPushButton('Gönder')
        self.yazi = QLabel('')
        self.yazi1 = QLabel('**Gönderilecek E-postayı Giriniz**')
        self.atilacak_posta = QLineEdit()

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.buton)
        h_box.addWidget(self.cikis)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi2)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.yazi1)
        v_box.addWidget(self.atilacak_posta)
        v_box.addStretch()

        v_box.addStretch()
        v_box.addStretch()

        v_box.addStretch()

        v_box.addStretch()


        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.buton.clicked.connect(self.click)
        self.cikis.clicked.connect(self.click)

        self.setWindowTitle('****Mail Spam Uygulaması****')
        self.show()

    def click(self):
        sender=self.sender()
        if sender.text()=="Gönder":
            while True:
                msj=MIMEMultipart()

                yazi = self.yazi_alani.toPlainText()
                govde = MIMEText(yazi, 'plain')
                msj.attach(govde)
                try:
                    maill = smtplib.SMTP('smtp.gmail.com', 587)
                    maill.ehlo()
                    maill.starttls()
                    maill.login(self.yazi4.text(), self.yazi5.text())
                    maill.sendmail(self.yazi4.text(), self.atilacak_posta.text(), msj.as_string())
                    maill.close()
                except:
                    self.yazi.setText('Hatalı')
            
        else:
            qApp.exit()


app = QApplication(sys.argv)
mail1 = mail()
mail1.setGeometry(20, 70, 300, 300)
sys.exit(app.exec_())
