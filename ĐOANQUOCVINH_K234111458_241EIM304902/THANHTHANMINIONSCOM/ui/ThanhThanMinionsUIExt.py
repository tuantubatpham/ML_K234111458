from ui.ThanhThanMinionsUI import Ui_MainWindow


class ThanhThanMinionsUIExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()
        self.num_red_bear = 0
        self.num_yellow_bear = 0
        self.num_white_bear = 0
        self.price_red_bear=5
        self.price_yellow_bear =10
        self.price_white_bear=15

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalsAndSlots(self):
        self.pushButtonBuy.clicked.connect(self.Buy)
        self.pushButtonClose.clicked.connect(self.MainWindow.close)

    def Buy(self):
        if self.radioButtonRB.isChecked():
            self.num_red_bear+=self.quantity()
        elif self.radioButtonYB.isChecked():
            self.num_yellow_bear+=self.quantity()
        elif self.radioButtoWB.isChecked():
            self.num_white_bear+=self.quantity()
        self.update_statistics()

    def quantity(self):
        if self.radioButtonBuy1.isChecked():
            return 1
        elif self.radioButtonBuy2.isChecked():
            return 2
        elif self.radioButtonBuy3.isChecked():
            return 3
        return 0

    def update_statistics(self):
        self.lineEditNumRb.setText(str(self.num_red_bear))
        self.lineEditNumYb.setText(str(self.num_yellow_bear))
        self.lineEditNumWb.setText(str(self.num_white_bear))
        value_red_bear=self.num_red_bear*self.price_red_bear
        value_yellow_bear=self.num_yellow_bear*self.price_yellow_bear
        value_white_bear=self.num_white_bear*self.price_white_bear
        total_bears=self.num_red_bear+self.num_yellow_bear + self.num_white_bear
        total_value=value_red_bear+value_yellow_bear + value_white_bear
        self.lineEditValueRB.setText(f"{value_red_bear}USD")
        self.lineEditValueYB.setText(f"{value_yellow_bear}USD")
        self.lineEditValueWB.setText(f"{value_white_bear}USD")
        self.lineEditNumall.setText(str(total_bears))
        self.lineEditValueAll.setText(f"{total_value}USD")
