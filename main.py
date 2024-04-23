import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Kalkulator kalorii")
        self.ui.dodaj.clicked.connect(self.dodaniePosilku)
        self.ui.dodaj.clicked.connect(self.sumaKalorii)
        self.posilki = []
        self.images = ["1.jpg", "2.jpg", "3.jpg"]

    def dodaniePosilku(self):
        if (self.ui.nazwaPosilku.text() != ''):
            self.posilki.append(self.ui.liczbaKalorii.value())
            self.ui.listaPosilkow.addItem(self.ui.nazwaPosilku.text() + ' ' + self.ui.liczbaKalorii.text())
            sumaKalorii = sum(self.posilki)
            self.ui.sumaKalorii.setText("Suma kalorii: "+str(sumaKalorii))
    def sumaKalorii(self):
        if self.ui.kobieta.isChecked() or self.ui.mezczyzna.isChecked():
            if self.ui.malaAktywnosc.isChecked() or self.ui.sredniaAktywnosc.isChecked() or self.ui.duzaAktywnosc.isChecked():
                if self.ui.kobieta.isChecked():
                    if self.ui.malaAktywnosc.isChecked():
                        zapotrzebowanie = 1700
                    elif self.ui.sredniaAktywnosc.isChecked():
                        zapotrzebowanie = 1900
                    elif self.ui.duzaAktywnosc.isChecked():
                        zapotrzebowanie = 2100
                elif self.ui.mezczyzna.isChecked():
                    if self.ui.malaAktywnosc.isChecked():
                        zapotrzebowanie = 1900
                    elif self.ui.malaAktywnosc.isChecked():
                        zapotrzebowanie = 2200
                    elif self.ui.malaAktywnosc.isChecked():
                        zapotrzebowanie = 2500
                sumaKalorii = 0
                for i in self.posilki:
                    sumaKalorii += i

                if sumaKalorii < (zapotrzebowanie * 0.8):
                    pixmap = QPixmap(f'./images/{self.images[0]}')
                    pixmap = pixmap.scaled(self.ui.zdjecie.width(), self.ui.zdjecie.height())
                    self.ui.zdjecie.setPixmap(pixmap)
                    self.ui.sumaKalorii.setStyleSheet("background-color: rgb(0, 255, 0);")
                if sumaKalorii > (zapotrzebowanie * 0.8) and self.ui.liczbaKalorii.value() < zapotrzebowanie:
                    self.ui.sumaKalorii.setStyleSheet("background-color: rgb(0, 0, 0);")
                    pixmap = QPixmap(f'./images/{self.images[1]}')
                    pixmap = pixmap.scaled(self.ui.zdjecie.width(), self.ui.zdjecie.height())
                    self.ui.zdjecie.setPixmap(pixmap)

                if sumaKalorii > zapotrzebowanie:
                    self.ui.sumaKalorii.setStyleSheet("background-color: rgb(255, 0, 0);")
                    pixmap = QPixmap(f'./images/{self.images[2]}')
                    pixmap = pixmap.scaled(self.ui.zdjecie.width(), self.ui.zdjecie.height())
                    self.ui.zdjecie.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()


    sys.exit(app.exec())
