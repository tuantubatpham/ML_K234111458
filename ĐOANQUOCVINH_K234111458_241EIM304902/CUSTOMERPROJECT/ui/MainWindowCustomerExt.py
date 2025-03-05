import functools
from audioop import reverse
from types import NoneType

from PyQt6.QtWidgets import QPushButton

from ui.MainWindowCustomer import Ui_MainWindow


class MainWindowCustomerExt(Ui_MainWindow):
    def __init__(self):
        self.customers=[]
    def dataSimulation(self):
        self.customers.append({"Mã":"Cus1","Ten":"Obama","Age":40,"LoaiKH":"Tiềm năng"})
        self.customers.append({"Mã": "Cus2", "Ten": "Putin", "Age": 68, "LoaiKH":"Trung Thành"})
        self.customers.append({"Mã": "Cus3", "Ten": "Hồ Cẩm Đào", "Age": 55, "LoaiKH":"Thường"})
        self.customers.append({"Mã": "Cus4", "Ten": "Kim Un Un", "Age": 42, "LoaiKH":"Trung Thành"})
        self.customers.append({"Mã": "Cus5", "Ten": "Trump", "Age": 78, "LoaiKH":"Thường"})
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlots()

    def showWindow(self):
        self.MainWindow.show()

    def showCusIntoGUI(self):
        for customer in self.customers:
            ma=customer["Mã"]
            ten=customer["Ten"]
            tuoi=customer["Age"]
            loaikh=customer["LoaiKH"]
            buttonCustomer=QPushButton()
            infor=f"Mã={ma};Tên={ten};Tuổi={tuoi}"
            buttonCustomer.setText(infor)
            if loaikh=="Tiềm năng":
                style="background-color:pink;font-size:15pt"
            elif loaikh=="Trung Thành":
                style = "background-color:blue;font-size:15pt"
            else:
                style="background-color:green;font-size:15pt"
            buttonCustomer.setStyleSheet(style)
            self.verticalLayoutCus.addWidget(buttonCustomer)
            #ĐÂY LÀ CÁCH VIẾT TÀO LAO
            #buttonCustomer.clicked.connect(self.show_detail(customer))
            buttonCustomer.clicked.connect(functools.partial(self.show_detail,customer))
    def show_detail(self,customer):
        ma = customer["Mã"]
        ten = customer["Ten"]
        tuoi = customer["Age"]
        loaikh = customer["LoaiKH"]
        self.lineEditMa.setText(ma)
        self.lineEditTen.setText(ten)
        self.lineEditTuoi.setText(f"{tuoi}")
        if loaikh=="Tiềm năng":
            self.radioButtonTN.setChecked(True)
            self.radioButtonTT.setChecked(False)
            self.radioButtonT.setChecked(False)
        elif loaikh=="Trung thành":
            self.radioButtonTN.setChecked(False)
            self.radioButtonTT.setChecked(True)
            self.radioButtonT.setChecked(False)
        else:
            self.radioButtonTN.setChecked(False)
            self.radioButtonTT.setChecked(False)
            self.radioButtonT.setChecked(True)
    def setupSignalandSlots(self):
        self.pushButtonNEW.clicked.connect(self.xuly_moi)
        self.pushButtonSAVE.clicked.connect(self.xuly_luu)
        self.pushButtonSX.clicked.connect(self.xuly_sx)
    def xuly_moi(self):
        self.lineEditMa.setText("")
        self.lineEditTen.setText("")
        self.lineEditTuoi.setText("")
        self.radioButtonTN.setChecked(False)
        self.radioButtonTT.setChecked(False)
        self.radioButtonT.setChecked(False)
        self.lineEditMa.setFocus()
    def xuly_luu(self):
        ma=self.lineEditMa.text()
        ten=self.lineEditTen.text()
        tuoi=int(self.lineEditTuoi.text())
        loaikh="Tiềm năng"
        if self.radioButtonTT.isChecked():
            loaikh="Trung Thành"
        elif self.radioButtonT.isChecked():
            loaikh="Thường"
        self.customers.append({"Mã":ma,"Ten":ten,"Age":tuoi,"LoaiKH":loaikh})
        #B1: Xóa dữ liệu trên giao diện đi
        for i in reversed(range(self.verticalLayoutCus.count())):
            self.verticalLayoutCus.itemAt(i).widget().setParent(None)
        #B2: Nạp lại dữ liệu mới lên giao diện
        self.showCusIntoGUI()
    def xuly_sx(self):
        for i in range(len(self.customers)):
            for j in range(i+1,len(self.customers)):
                customeri=self.customers[i]
                customerj=self.customers[j]
                if customeri["Age"]>customerj["Age"]:
                    self.customers[i]=customerj
                    self.customers[j]=customeri
        for i in reverse(range(self.verticalLayoutCus.count())):
            self.verticalLayoutCus.itemAt(i).widget().setParent(NoneType)