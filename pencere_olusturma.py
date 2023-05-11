app = QtWidgets.QApplication(sys.argv)

self.yenik = QtWidgets.QLineEdit()
self.yenip = QtWidgets.QLineEdit()
self.yenib = QtWidgets.QPushButton()
ad2 = self.yenik.text()
par2 = self.yenip.text()
v1_box = QtWidgets.QVBoxLayout()
v1_box.addWidget(self.yenik)
v1_box.addWidget(self.yenip)
v1_box.addWidget(self.yenib)

h1_box = QtWidgets.QHBoxLayout()
h1_box.addStretch()
h1_box.addLayout(v1_box)
h1_box.addStretch()
self.setLayout(h1_box)
self.show()

pencere = QtWidgets.QWidget()

pencere.setWindowTitle("PyQt5 Ders 1")

pencere.show()

self.cursor.execute("insert into base values(?,?)", (ad2, par2))
sys.exit(app.exec_())