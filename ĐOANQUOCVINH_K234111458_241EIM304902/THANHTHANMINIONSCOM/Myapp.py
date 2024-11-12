from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.ThanhThanMinionsUIExt import ThanhThanMinionsUIExt

app=QApplication([])
mainwindow=QMainWindow()
myui=ThanhThanMinionsUIExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()