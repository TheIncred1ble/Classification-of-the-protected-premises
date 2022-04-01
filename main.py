import sys
import Main_Window
import Report_Window
import reportDlg
import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox


class ReportWindow(QtWidgets.QMainWindow, Report_Window.Ui_MainWindow):
    # login_data = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okk = True


class MainWindow(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.reportWindow = None
        self.pushButton.clicked.connect(self.check)
        self.t1_Dbe.clicked.connect(self.t1_Dbe_click)
        self.t1_Wbe.clicked.connect(self.t1_Wbe_click)
        self.t2_Dbe.clicked.connect(self.t2_Dbe_click)
        self.t2_Wbe.clicked.connect(self.t2_Wbe_click)
        self.t3_Dbe.clicked.connect(self.t3_Dbe_click)
        self.t3_Wbe.clicked.connect(self.t3_Wbe_click)
        self.t4_Dbe.clicked.connect(self.t4_Dbe_click)
        self.t4_Wbe.clicked.connect(self.t4_Wbe_click)
        self.ready1 = False
        self.ready1d = False
        self.ready1w = False
        self.ready2 = False
        self.ready2d = False
        self.ready2w = False
        self.ready3 = False
        self.ready3d = False
        self.ready3w = False
        self.ready4 = False
        self.ready4d = False
        self.ready4w = False

        # Категории выделенных помещений
        self.ktg1 = [46, 47, 47, 48, 49, 50, 52, 53, 54, 55, 56, 56, 56, 56, 56, 55]
        self.ktg2 = [41, 42, 42, 43, 44, 45, 47, 48, 49, 50, 51, 51, 51, 51, 51, 50]
        self.ktg3 = [36, 37, 37, 38, 39, 40, 42, 43, 44, 45, 46, 46, 46, 46, 46, 45]

        # Ограждения
        # Кирпичные
        self.kir1 = [35, 39, 39, 40, 40, 40, 41, 42, 44, 46, 48, 50, 52, 54, 55, 57]
        self.kir2 = [39, 41, 42, 43, 44, 46, 48, 51, 53, 55, 58, 60, 62, 64, 64, 64]
        self.kir3 = [43, 44, 45, 46, 48, 50, 52, 55, 57, 59, 61, 62, 64, 65, 65, 65]
        self.kir4 = [45, 45, 47, 49, 52, 54, 56, 59, 61, 63, 65, 66, 68, 70, 70, 70]
        self.kir5 = [46, 47, 49, 52, 55, 56, 58, 60, 62, 64, 67, 68, 69, 70, 70, 70]
        # Железобетонные
        self.zhb1 = [32, 32, 33, 34, 36, 36, 35, 35, 36, 37, 38, 41, 44, 47, 48, 50]
        self.zhb2 = [32, 34, 34, 35, 35, 35, 35, 35, 37, 39, 41, 43, 45, 48, 50, 52]
        self.zhb3 = [38, 40, 40, 40, 40, 41, 42, 44, 46, 48, 50, 51, 53, 55, 57, 58]
        self.zhb4 = [43, 43, 44, 45, 47, 48, 49, 51, 54, 57, 60, 61, 62, 63, 63, 63]
        self.zhb5 = [41, 42, 42, 43, 44, 46, 48, 51, 53, 56, 59, 61, 63, 65, 65, 65]
        self.zhb6 = [45, 45, 46, 48, 50, 52, 55, 58, 61, 63, 65, 67, 68, 69, 69, 69]
        self.zhb7 = [47, 48, 50, 52, 55, 57, 59, 61, 63, 66, 68, 68, 69, 70, 70, 70]
        self.zhb8 = [53, 55, 57, 59, 61, 63, 66, 68, 68, 69, 70, 70, 70, 70, 70, 70]
        # Гипсобетонные
        self.gbp1 = [32, 32, 33, 35, 37, 37, 37, 37, 38, 40, 42, 44, 46, 48, 50, 51]
        # Стена из шлакоблоков
        self.shb1 = [42, 42, 42, 42, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 61, 62]
        # Древесно-стружечная плита
        self.dsp1 = [23, 23, 24, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]

        # Окна
        # Одинарное остекление
        self.onw1 = [17, 17, 17, 17, 17, 18, 20, 22, 24, 26, 28, 29, 30, 31, 31, 31]
        self.onw2 = [18, 18, 19, 21, 23, 24, 25, 26, 27, 29, 31, 31, 31, 32, 32, 32]
        self.onw3 = [22, 22, 22, 22, 22, 23, 24, 26, 28, 29, 30, 29, 28, 27, 26, 26]
        # Двойное остекление
        self.tww1 = [15, 15, 16, 18, 20, 24, 28, 32, 35, 38, 41, 44, 47, 49, 48, 47]
        self.tww2 = [20, 21, 23, 26, 29, 32, 35, 38, 40, 42, 44, 46, 48, 50, 50, 49]
        self.tww3 = [20, 21, 24, 27, 31, 34, 36, 38, 40, 43, 46, 47, 48, 49, 46, 42]
        self.tww4 = [24, 25, 27, 30, 33, 36, 39, 41, 43, 45, 47, 47, 48, 48, 45, 42]
        self.tww5 = [22, 23, 24, 25, 27, 30, 33, 36, 38, 40, 42, 43, 44, 45, 45, 45]
        self.tww6 = [26, 27, 28, 29, 30, 32, 32, 37, 39, 41, 43, 44, 45, 46, 46, 47]
        self.tww7 = [21, 21, 25, 29, 33, 35, 37, 39, 42, 45, 47, 48, 49, 50, 50, 50]
        self.tww8 = [28, 28, 30, 33, 36, 38, 40, 41, 43, 45, 48, 50, 52, 54, 54, 55]
        self.tww9 = [34, 34, 36, 38, 40, 42, 43, 44, 46, 48, 50, 51, 51, 52, 52, 53]
        # Тройное остекление
        self.thw1 = [25, 25, 28, 32, 36, 37, 39, 41, 44, 47, 50, 51, 52, 53, 53, 54]
        self.thw2 = [34, 34, 35, 37, 39, 40, 42, 44, 46, 48, 50, 51, 52, 53, 53, 54]
        self.thw3 = [30, 30, 33, 36, 39, 40, 41, 42, 45, 47, 49, 50, 51, 52, 54, 56]

        # Двери
        # Щитовая дверь, облицованная фанерой с двух сторон (без прокладки, с прокладкой)
        self.sdf1 = [20, 21, 21, 22, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24]
        self.sdf2 = [25, 27, 27, 27, 27, 28, 30, 32, 33, 34, 35, 35, 35, 34, 34, 35]
        # Щитовая дверь из древесноволокнистых плит со стекловатой (без прокладки, с прокладкой)
        self.sds1 = [23, 25, 25, 26, 26, 28, 29, 30, 30, 31, 31, 30, 29, 28, 28, 29]
        self.sds2 = [25, 28, 28, 29, 30, 31, 32, 33, 34, 35, 36, 35, 34, 32, 31, 31]
        # Филенчатая дверь (без прокладки, с прокладкой)
        self.fld1 = [10, 12, 13, 13, 14, 14, 15, 16, 18, 20, 22, 22, 22, 22, 22, 21]
        self.fld2 = [15, 18, 18, 19, 19, 20, 21, 23, 25, 28, 30, 31, 32, 33, 33, 33]
        # Типовая дверь П-327 (без прокладки, с прокладкой)
        self.tdp1 = [13, 13, 16, 19, 23, 26, 29, 31, 32, 32, 33, 33, 34, 34, 35, 35]
        self.tdp2 = [29, 29, 29, 30, 30, 30, 31, 31, 31, 32, 33, 33, 34, 34, 36, 38]
        # Дверь изолирующая облегченная
        self.diob = [16, 18, 22, 26, 30, 33, 36, 39, 40, 41, 42, 43, 44, 45, 44, 43]
        # Дверь изолирующая двойная с зазором > 200 мм
        self.dido = [22, 25, 30, 36, 42, 47, 51, 55, 56, 57, 58, 58, 59, 60, 60, 60]
        # Дверь звукоизолирующая тяжелая
        self.dzt1 = [23, 24, 28, 32, 36, 39, 42, 45, 47, 49, 51, 51, 50, 50, 50, 50]
        # Дверь звукоизолирующая двойная с зазором > 300 мм тяжелая
        self.dzd1 = [31, 34, 38, 42, 46, 51, 56, 60, 62, 64, 65, 65, 65, 65, 65, 65]
        # Двери двойные с облицовкой тамбура тяжелые
        self.ddot = [40, 45, 49, 53, 58, 61, 63, 65, 67, 69, 70, 70, 70, 70, 70, 70]

        # Пол/потолок
        # Железобетонное сплошное перекрытие
        self.pzs1 = [35, 35, 38, 42, 46, 49, 51, 53, 54, 55, 55, 55, 56, 56, 57, 58]
        self.pzs2 = [37, 37, 40, 43, 46, 50, 54, 57, 60, 63, 65, 66, 67, 67, 67, 67]
        # Железобетонное многопустотное перекрытие с плавающим полом
        self.pzm1 = [38, 38, 40, 42, 44, 46, 48, 50, 53, 55, 57, 59, 61, 63, 63, 64]
        self.pzm2 = [38, 38, 39, 41, 43, 46, 50, 53, 56, 59, 62, 66, 70, 73, 73, 73]
        self.pzm3 = [38, 38, 40, 43, 46, 50, 54, 58, 62, 66, 70, 72, 73, 74, 74, 75]
        self.pzm4 = [41, 41, 41, 41, 40, 43, 47, 50, 52, 54, 56, 57, 58, 58, 59, 59]
        self.pzm5 = [40, 40, 41, 42, 44, 46, 49, 52, 55, 58, 60, 62, 63, 64, 63, 61]
        self.pzm6 = [40, 40, 40, 40, 39, 42, 45, 49, 52, 55, 58, 60, 61, 62, 61, 60]
        self.pzm7 = [42, 42, 43, 45, 47, 50, 53, 56, 58, 59, 60, 62, 64, 65, 66, 67]
        self.pzm8 = [52, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 77, 78]

        # Уменьшенные значения для категорий
        self.ktg1m1 = [0] * 16
        self.ktg1m2 = [0] * 16
        self.ktg1m3 = [0] * 16
        self.ktg1m4 = [0] * 16
        self.ktg2m1 = [0] * 16
        self.ktg2m2 = [0] * 16
        self.ktg2m3 = [0] * 16
        self.ktg2m4 = [0] * 16
        self.ktg3m1 = [0] * 16
        self.ktg3m2 = [0] * 16
        self.ktg3m3 = [0] * 16
        self.ktg3m4 = [0] * 16
        for i in range(16):
            self.ktg1m1[i] = self.ktg1[i] - 1
            self.ktg1m2[i] = self.ktg1[i] - 2
            self.ktg1m3[i] = self.ktg1[i] - 3
            self.ktg1m4[i] = self.ktg1[i] - 4
        for i in range(16):
            self.ktg2m1[i] = self.ktg2[i] - 1
            self.ktg2m2[i] = self.ktg2[i] - 2
            self.ktg2m3[i] = self.ktg2[i] - 3
            self.ktg2m4[i] = self.ktg2[i] - 4
        for i in range(16):
            self.ktg3m1[i] = self.ktg3[i] - 1
            self.ktg3m2[i] = self.ktg3[i] - 2
            self.ktg3m3[i] = self.ktg3[i] - 3
            self.ktg3m4[i] = self.ktg3[i] - 4

    def CalcR(self, R1, R2):
        self.RC = R1 - R2
        if self.RC > 0:
            return self.RC
        else:
            return 0

    def Calc_Res(self, nWall, nEls):
        self.sumR = 0
        self.nR = 0
        self.chk = True
        self.num = 0
        self.x = 1
        self.s2 = 0.0
        self.s3 = 0.0
        self.sa = 0.0
        self.s1 = 0.0

        self.P1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.P2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.P3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.dR = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.tR = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        nKat = 0
        ks = 0  # 1 дверь, 2 окно, 3 дверь с окном

        if nWall == 1:
            self.s1 = self.t1_Wb.value()
            if self.txtSn == 1:
                self.P1 = self.kir1
            elif self.txtSn == 2:
                self.P1 = self.kir2
            elif self.txtSn == 3:
                self.P1 = self.kir3
            elif self.txtSn == 4:
                self.P1 = self.kir4
            elif self.txtSn == 5:
                self.P1 = self.kir5
            elif self.txtSn == 6:
                self.P1 = self.zhb1
            elif self.txtSn == 7:
                self.P1 = self.zhb2
            elif self.txtSn == 8:
                self.P1 = self.zhb3
            elif self.txtSn == 9:
                self.P1 = self.zhb4
            elif self.txtSn == 10:
                self.P1 = self.zhb5
            elif self.txtSn == 11:
                self.P1 = self.zhb6
            elif self.txtSn == 12:
                self.P1 = self.zhb7
            elif self.txtSn == 13:
                self.P1 = self.zhb8
            elif self.txtSn == 14:
                self.P1 = self.gbp1
            elif self.txtSn == 15:
                self.P1 = self.shb1
            elif self.txtSn == 16:
                self.P1 = self.dsp1

            if self.t1_Dbe.isChecked() and self.t1_Wbe.isChecked():
                ks = 3
            elif self.t1_Dbe.isChecked() and not self.t1_Wbe.isChecked():
                ks = 1
            elif self.t1_Wbe.isChecked() and not self.t1_Dbe.isChecked():
                ks = 2

            if ks == 1 or ks == 3:
                self.s2 = self.t1_DWb.value()
                self.s3 = self.t1_WWb.value()
                if self.txtDn == 1:
                    self.P2 = self.sdf1
                elif self.txtDn == 2:
                    self.P2 = self.sdf2
                elif self.txtDn == 3:
                    self.P2 = self.sds1
                elif self.txtDn == 4:
                    self.P2 = self.sds2
                elif self.txtDn == 5:
                    self.P2 = self.fld1
                elif self.txtDn == 6:
                    self.P2 = self.fld2
                elif self.txtDn == 7:
                    self.P2 = self.tdp1
                elif self.txtDn == 8:
                    self.P2 = self.tdp2
                elif self.txtDn == 9:
                    self.P2 = self.diob
                elif self.txtDn == 10:
                    self.P2 = self.dido
                elif self.txtDn == 11:
                    self.P2 = self.dzt1
                elif self.txtDn == 12:
                    self.P2 = self.dzd1
                elif self.txtDn == 13:
                    self.P2 = self.ddot

                if self.txtWn == 1:
                    self.P3 = self.onw1
                elif self.txtWn == 2:
                    self.P3 = self.onw2
                elif self.txtWn == 3:
                    self.P3 = self.onw3
                elif self.txtWn == 4:
                    self.P3 = self.tww1
                elif self.txtWn == 5:
                    self.P3 = self.tww2
                elif self.txtWn == 6:
                    self.P3 = self.tww3
                elif self.txtWn == 7:
                    self.P3 = self.tww4
                elif self.txtWn == 8:
                    self.P3 = self.tww5
                elif self.txtWn == 9:
                    self.P3 = self.tww6
                elif self.txtWn == 10:
                    self.P3 = self.tww7
                elif self.txtWn == 11:
                    self.P3 = self.tww8
                elif self.txtWn == 12:
                    self.P3 = self.tww9
                elif self.txtWn == 13:
                    self.P3 = self.thw1
                elif self.txtWn == 14:
                    self.P3 = self.thw2
                elif self.txtWn == 15:
                    self.P3 = self.thw3

            elif ks == 2:
                self.s2 = self.t1_WWb.value()
                if self.txtWn == 1:
                    self.P2 = self.onw1
                elif self.txtWn == 2:
                    self.P2 = self.onw2
                elif self.txtWn == 3:
                    self.P2 = self.onw3
                elif self.txtWn == 4:
                    self.P2 = self.tww1
                elif self.txtWn == 5:
                    self.P2 = self.tww2
                elif self.txtWn == 6:
                    self.P2 = self.tww3
                elif self.txtWn == 7:
                    self.P2 = self.tww4
                elif self.txtWn == 8:
                    self.P2 = self.tww5
                elif self.txtWn == 9:
                    self.P2 = self.tww6
                elif self.txtWn == 10:
                    self.P2 = self.tww7
                elif self.txtWn == 11:
                    self.P2 = self.tww8
                elif self.txtWn == 12:
                    self.P2 = self.tww9
                elif self.txtWn == 13:
                    self.P2 = self.thw1
                elif self.txtWn == 14:
                    self.P2 = self.thw2
                elif self.txtWn == 15:
                    self.P2 = self.thw3

        elif nWall == 2:
            self.s1 = self.t2_Wb.value()
            if self.txtSn2 == 1:
                self.P1 = self.kir1
            elif self.txtSn2 == 2:
                self.P1 = self.kir2
            elif self.txtSn2 == 3:
                self.P1 = self.kir3
            elif self.txtSn2 == 4:
                self.P1 = self.kir4
            elif self.txtSn2 == 5:
                self.P1 = self.kir5
            elif self.txtSn2 == 6:
                self.P1 = self.zhb1
            elif self.txtSn2 == 7:
                self.P1 = self.zhb2
            elif self.txtSn2 == 8:
                self.P1 = self.zhb3
            elif self.txtSn2 == 9:
                self.P1 = self.zhb4
            elif self.txtSn2 == 10:
                self.P1 = self.zhb5
            elif self.txtSn2 == 11:
                self.P1 = self.zhb6
            elif self.txtSn2 == 12:
                self.P1 = self.zhb7
            elif self.txtSn2 == 13:
                self.P1 = self.zhb8
            elif self.txtSn2 == 14:
                self.P1 = self.gbp1
            elif self.txtSn2 == 15:
                self.P1 = self.shb1
            elif self.txtSn2 == 16:
                self.P1 = self.dsp1

            if self.t2_Dbe.isChecked() and self.t2_Wbe.isChecked():
                ks = 3
            elif self.t2_Dbe.isChecked() and not self.t2_Wbe.isChecked():
                ks = 1
            elif self.t2_Wbe.isChecked() and not self.t2_Dbe.isChecked():
                ks = 2

            if ks == 1 or ks == 3:
                self.s2 = self.t2_DWb.value()
                self.s3 = self.t2_WWb.value()
                if self.txtDn2 == 1:
                    self.P2 = self.sdf1
                elif self.txtDn2 == 2:
                    self.P2 = self.sdf2
                elif self.txtDn2 == 3:
                    self.P2 = self.sds1
                elif self.txtDn2 == 4:
                    self.P2 = self.sds2
                elif self.txtDn2 == 5:
                    self.P2 = self.fld1
                elif self.txtDn2 == 6:
                    self.P2 = self.fld2
                elif self.txtDn2 == 7:
                    self.P2 = self.tdp1
                elif self.txtDn2 == 8:
                    self.P2 = self.tdp2
                elif self.txtDn2 == 9:
                    self.P2 = self.diob
                elif self.txtDn2 == 10:
                    self.P2 = self.dido
                elif self.txtDn2 == 11:
                    self.P2 = self.dzt1
                elif self.txtDn2 == 12:
                    self.P2 = self.dzd1
                elif self.txtDn2 == 13:
                    self.P2 = self.ddot

                if self.txtWn2 == 1:
                    self.P3 = self.onw1
                elif self.txtWn2 == 2:
                    self.P3 = self.onw2
                elif self.txtWn2 == 3:
                    self.P3 = self.onw3
                elif self.txtWn2 == 4:
                    self.P3 = self.tww1
                elif self.txtWn2 == 5:
                    self.P3 = self.tww2
                elif self.txtWn2 == 6:
                    self.P3 = self.tww3
                elif self.txtWn2 == 7:
                    self.P3 = self.tww4
                elif self.txtWn2 == 8:
                    self.P3 = self.tww5
                elif self.txtWn2 == 9:
                    self.P3 = self.tww6
                elif self.txtWn2 == 10:
                    self.P3 = self.tww7
                elif self.txtWn2 == 11:
                    self.P3 = self.tww8
                elif self.txtWn2 == 12:
                    self.P3 = self.tww9
                elif self.txtWn2 == 13:
                    self.P3 = self.thw1
                elif self.txtWn2 == 14:
                    self.P3 = self.thw2
                elif self.txtWn2 == 15:
                    self.P3 = self.thw3

            elif ks == 2:
                self.s2 = self.t2_WWb.value()
                if self.txtWn2 == 1:
                    self.P2 = self.onw1
                elif self.txtWn2 == 2:
                    self.P2 = self.onw2
                elif self.txtWn2 == 3:
                    self.P2 = self.onw3
                elif self.txtWn2 == 4:
                    self.P2 = self.tww1
                elif self.txtWn2 == 5:
                    self.P2 = self.tww2
                elif self.txtWn2 == 6:
                    self.P2 = self.tww3
                elif self.txtWn2 == 7:
                    self.P2 = self.tww4
                elif self.txtWn2 == 8:
                    self.P2 = self.tww5
                elif self.txtWn2 == 9:
                    self.P2 = self.tww6
                elif self.txtWn2 == 10:
                    self.P2 = self.tww7
                elif self.txtWn2 == 11:
                    self.P2 = self.tww8
                elif self.txtWn2 == 12:
                    self.P2 = self.tww9
                elif self.txtWn2 == 13:
                    self.P2 = self.thw1
                elif self.txtWn2 == 14:
                    self.P2 = self.thw2
                elif self.txtWn2 == 15:
                    self.P2 = self.thw3


        elif nWall == 3:
            self.s1 = self.t3_Wb.value()
            if self.txtSn3 == 1:
                self.P1 = self.kir1
            elif self.txtSn3 == 2:
                self.P1 = self.kir2
            elif self.txtSn3 == 3:
                self.P1 = self.kir3
            elif self.txtSn3 == 4:
                self.P1 = self.kir4
            elif self.txtSn3 == 5:
                self.P1 = self.kir5
            elif self.txtSn3 == 6:
                self.P1 = self.zhb1
            elif self.txtSn3 == 7:
                self.P1 = self.zhb2
            elif self.txtSn3 == 8:
                self.P1 = self.zhb3
            elif self.txtSn3 == 9:
                self.P1 = self.zhb4
            elif self.txtSn3 == 10:
                self.P1 = self.zhb5
            elif self.txtSn3 == 11:
                self.P1 = self.zhb6
            elif self.txtSn3 == 12:
                self.P1 = self.zhb7
            elif self.txtSn3 == 13:
                self.P1 = self.zhb8
            elif self.txtSn3 == 14:
                self.P1 = self.gbp1
            elif self.txtSn3 == 15:
                self.P1 = self.shb1
            elif self.txtSn3 == 16:
                self.P1 = self.dsp1

            if self.t3_Dbe.isChecked() and self.t3_Wbe.isChecked():
                ks = 3
            elif self.t3_Dbe.isChecked() and not self.t3_Wbe.isChecked():
                ks = 1
            elif self.t3_Wbe.isChecked() and not self.t3_Dbe.isChecked():
                ks = 2

            if ks == 1 or ks == 3:
                self.s2 = self.t3_DWb.value()
                self.s3 = self.t3_WWb.value()
                if self.txtDn3 == 1:
                    self.P2 = self.sdf1
                elif self.txtDn3 == 2:
                    self.P2 = self.sdf2
                elif self.txtDn3 == 3:
                    self.P2 = self.sds1
                elif self.txtDn3 == 4:
                    self.P2 = self.sds2
                elif self.txtDn3 == 5:
                    self.P2 = self.fld1
                elif self.txtDn3 == 6:
                    self.P2 = self.fld2
                elif self.txtDn3 == 7:
                    self.P2 = self.tdp1
                elif self.txtDn3 == 8:
                    self.P2 = self.tdp2
                elif self.txtDn3 == 9:
                    self.P2 = self.diob
                elif self.txtDn3 == 10:
                    self.P2 = self.dido
                elif self.txtDn3 == 11:
                    self.P2 = self.dzt1
                elif self.txtDn3 == 12:
                    self.P2 = self.dzd1
                elif self.txtDn3 == 13:
                    self.P2 = self.ddot

                if self.txtWn3 == 1:
                    self.P3 = self.onw1
                elif self.txtWn3 == 2:
                    self.P3 = self.onw2
                elif self.txtWn3 == 3:
                    self.P3 = self.onw3
                elif self.txtWn3 == 4:
                    self.P3 = self.tww1
                elif self.txtWn3 == 5:
                    self.P3 = self.tww2
                elif self.txtWn3 == 6:
                    self.P3 = self.tww3
                elif self.txtWn3 == 7:
                    self.P3 = self.tww4
                elif self.txtWn3 == 8:
                    self.P3 = self.tww5
                elif self.txtWn3 == 9:
                    self.P3 = self.tww6
                elif self.txtWn3 == 10:
                    self.P3 = self.tww7
                elif self.txtWn3 == 11:
                    self.P3 = self.tww8
                elif self.txtWn3 == 12:
                    self.P3 = self.tww9
                elif self.txtWn3 == 13:
                    self.P3 = self.thw1
                elif self.txtWn3 == 14:
                    self.P3 = self.thw2
                elif self.txtWn3 == 15:
                    self.P3 = self.thw3

            elif ks == 2:
                self.s2 = self.t3_WWb.value()
                if self.txtWn3 == 1:
                    self.P2 = self.onw1
                elif self.txtWn3 == 2:
                    self.P2 = self.onw2
                elif self.txtWn3 == 3:
                    self.P2 = self.onw3
                elif self.txtWn3 == 4:
                    self.P2 = self.tww1
                elif self.txtWn3 == 5:
                    self.P2 = self.tww2
                elif self.txtWn3 == 6:
                    self.P2 = self.tww3
                elif self.txtWn3 == 7:
                    self.P2 = self.tww4
                elif self.txtWn3 == 8:
                    self.P2 = self.tww5
                elif self.txtWn3 == 9:
                    self.P2 = self.tww6
                elif self.txtWn3 == 10:
                    self.P2 = self.tww7
                elif self.txtWn3 == 11:
                    self.P2 = self.tww8
                elif self.txtWn3 == 12:
                    self.P2 = self.tww9
                elif self.txtWn3 == 13:
                    self.P2 = self.thw1
                elif self.txtWn3 == 14:
                    self.P2 = self.thw2
                elif self.txtWn3 == 15:
                    self.P2 = self.thw3

        elif nWall == 4:
            self.s1 = self.t4_Wb.value()
            if self.txtSn4 == 1:
                self.P1 = self.kir1
            elif self.txtSn4 == 2:
                self.P1 = self.kir2
            elif self.txtSn4 == 3:
                self.P1 = self.kir3
            elif self.txtSn4 == 4:
                self.P1 = self.kir4
            elif self.txtSn4 == 5:
                self.P1 = self.kir5
            elif self.txtSn4 == 6:
                self.P1 = self.zhb1
            elif self.txtSn4 == 7:
                self.P1 = self.zhb2
            elif self.txtSn4 == 8:
                self.P1 = self.zhb3
            elif self.txtSn4 == 9:
                self.P1 = self.zhb4
            elif self.txtSn4 == 10:
                self.P1 = self.zhb5
            elif self.txtSn4 == 11:
                self.P1 = self.zhb6
            elif self.txtSn4 == 12:
                self.P1 = self.zhb7
            elif self.txtSn4 == 13:
                self.P1 = self.zhb8
            elif self.txtSn4 == 14:
                self.P1 = self.gbp1
            elif self.txtSn4 == 15:
                self.P1 = self.shb1
            elif self.txtSn4 == 16:
                self.P1 = self.dsp1

            if self.t4_Dbe.isChecked() and self.t4_Wbe.isChecked():
                ks = 3
            elif self.t4_Dbe.isChecked() and not self.t4_Wbe.isChecked():
                ks = 1
            elif self.t4_Wbe.isChecked() and not self.t4_Dbe.isChecked():
                ks = 2

            if ks == 1 or ks == 3:
                self.s2 = self.t4_DWb.value()
                self.s3 = self.t4_WWb.value()
                if self.txtDn4 == 1:
                    self.P2 = self.sdf1
                elif self.txtDn4 == 2:
                    self.P2 = self.sdf2
                elif self.txtDn4 == 3:
                    self.P2 = self.sds1
                elif self.txtDn4 == 4:
                    self.P2 = self.sds2
                elif self.txtDn4 == 5:
                    self.P2 = self.fld1
                elif self.txtDn4 == 6:
                    self.P2 = self.fld2
                elif self.txtDn4 == 7:
                    self.P2 = self.tdp1
                elif self.txtDn4 == 8:
                    self.P2 = self.tdp2
                elif self.txtDn4 == 9:
                    self.P2 = self.diob
                elif self.txtDn4 == 10:
                    self.P2 = self.dido
                elif self.txtDn4 == 11:
                    self.P2 = self.dzt1
                elif self.txtDn4 == 12:
                    self.P2 = self.dzd1
                elif self.txtDn4 == 13:
                    self.P2 = self.ddot

                if self.txtWn4 == 1:
                    self.P3 = self.onw1
                elif self.txtWn4 == 2:
                    self.P3 = self.onw2
                elif self.txtWn4 == 3:
                    self.P3 = self.onw3
                elif self.txtWn4 == 4:
                    self.P3 = self.tww1
                elif self.txtWn4 == 5:
                    self.P3 = self.tww2
                elif self.txtWn4 == 6:
                    self.P3 = self.tww3
                elif self.txtWn4 == 7:
                    self.P3 = self.tww4
                elif self.txtWn4 == 8:
                    self.P3 = self.tww5
                elif self.txtWn4 == 9:
                    self.P3 = self.tww6
                elif self.txtWn4 == 10:
                    self.P3 = self.tww7
                elif self.txtWn4 == 11:
                    self.P3 = self.tww8
                elif self.txtWn4 == 12:
                    self.P3 = self.tww9
                elif self.txtWn4 == 13:
                    self.P3 = self.thw1
                elif self.txtWn4 == 14:
                    self.P3 = self.thw2
                elif self.txtWn4 == 15:
                    self.P3 = self.thw3

            elif ks == 2:
                self.s2 = self.t4_WWb.value()
                if self.txtWn4 == 1:
                    self.P2 = self.onw1
                elif self.txtWn4 == 2:
                    self.P2 = self.onw2
                elif self.txtWn4 == 3:
                    self.P2 = self.onw3
                elif self.txtWn4 == 4:
                    self.P2 = self.tww1
                elif self.txtWn4 == 5:
                    self.P2 = self.tww2
                elif self.txtWn4 == 6:
                    self.P2 = self.tww3
                elif self.txtWn4 == 7:
                    self.P2 = self.tww4
                elif self.txtWn4 == 8:
                    self.P2 = self.tww5
                elif self.txtWn4 == 9:
                    self.P2 = self.tww6
                elif self.txtWn4 == 10:
                    self.P2 = self.tww7
                elif self.txtWn4 == 11:
                    self.P2 = self.tww8
                elif self.txtWn4 == 12:
                    self.P2 = self.tww9
                elif self.txtWn4 == 13:
                    self.P2 = self.thw1
                elif self.txtWn4 == 14:
                    self.P2 = self.thw2
                elif self.txtWn4 == 15:
                    self.P2 = self.thw3

        elif nWall == 5:
            if self.txtSn5 == 1:
                self.P1 = self.pzs1
            elif self.txtSn5 == 2:
                self.P1 = self.pzs2
            elif self.txtSn5 == 3:
                self.P1 = self.pzm1
            elif self.txtSn5 == 4:
                self.P1 = self.pzm2
            elif self.txtSn5 == 5:
                self.P1 = self.pzm3
            elif self.txtSn5 == 6:
                self.P1 = self.pzm4
            elif self.txtSn5 == 7:
                self.P1 = self.pzm5
            elif self.txtSn5 == 8:
                self.P1 = self.pzm6
            elif self.txtSn5 == 9:
                self.P1 = self.pzm7
            elif self.txtSn5 == 10:
                self.P1 = self.pzm8

        elif nWall == 6:
            if self.txtSn6 == 1:
                self.P1 = self.pzs1
            elif self.txtSn6 == 2:
                self.P1 = self.pzs2
            elif self.txtSn6 == 3:
                self.P1 = self.pzm1
            elif self.txtSn6 == 4:
                self.P1 = self.pzm2
            elif self.txtSn6 == 5:
                self.P1 = self.pzm3
            elif self.txtSn6 == 6:
                self.P1 = self.pzm4
            elif self.txtSn6 == 7:
                self.P1 = self.pzm5
            elif self.txtSn6 == 8:
                self.P1 = self.pzm6
            elif self.txtSn6 == 9:
                self.P1 = self.pzm7
            elif self.txtSn6 == 10:
                self.P1 = self.pzm8

        self.sa = self.s1 + self.s2 + self.s3

        self.dA = [25, 18, 14, 9, 6, 5, 4]
        self.ki = [0.01, 0.03, 0.12, 0.2, 0.3, 0.26, 0.07]
        self.gr = [53, 66, 66, 61, 56, 53, 49]
        self.ps = [61, 54, 49, 45, 42, 40, 38]

        # self.Qq = [self.P1[1], self.P1[4], self.P1[7], self.P1[10], self.P1[13], self.P1[15], self.P1[15]]

        self.qi = [10, 10, 10, 10, 10, 10, 10]
        self.Qi = [10, 10, 10, 10, 10, 10, 10]
        self.pi = [10, 10, 10, 10, 10, 10, 10]
        self.Ri = [10, 10, 10, 10, 10, 10, 10]

        if nEls == 1:
            self.Qq = [self.P1[1], self.P1[4], self.P1[7], self.P1[10], self.P1[13], self.P1[15], self.P1[15]]
            while self.chk:
                for i in range(16):
                    self.sumR = self.sumR + self.CalcR(self.ktg1[i] - self.num, self.P1[i])
                if self.sumR < 32:
                    self.nR = self.sumR
                    self.chk = False
                self.num = self.num + 1
                self.sumR = 0
            if self.num > 10:
                print("Категория худшая")
                nKat = 0
            else:
                print("xR = ", self.nR)
                print("R = ", self.ktg1[7] - (self.num - 1))
                nKat = self.ktg1[7] - (self.num - 1)
        elif nEls == 2:
            self.nS = self.sa / self.s2
            while self.chk:
                for j in range(16):
                    self.dR[j] = self.P1[j] - int(
                        10 * math.log10((self.nS + math.pow(10, 0.1 * (self.P1[j] - self.P2[j]))) / (1 + self.nS)))
                self.Qq = [self.dR[1], self.dR[4], self.dR[7], self.dR[10], self.dR[13], self.dR[15], self.dR[15]]
                for k in range(16):
                    self.sumR = self.sumR + self.CalcR(self.ktg1[k] - self.num, self.dR[k])
                if self.sumR < 32:
                    self.nR = self.sumR
                    self.chk = False
                self.num = self.num + 1
                self.sumR = 0
            if self.num > 10:
                print("Категория худшая")
                nKat = 0
            else:
                print("xR = ", self.nR)
                print("R = ", self.ktg1[7] - (self.num - 1))
                nKat = self.ktg1[7] - (self.num - 1)
        elif nEls == 3:
            while self.chk:
                for l in range(16):
                    self.tR[l] = int(10 * math.log10(self.sa / (
                            (self.s1 / math.pow(10, 0.1 * self.P1[l])) + (self.s2 / math.pow(10, 0.1 * self.P2[l])) + (
                            self.s3 / math.pow(10, 0.1 * self.P3[l])))))
                self.Qq = [self.tR[1], self.tR[4], self.tR[7], self.tR[10], self.tR[13], self.tR[15], self.tR[15]]
                for m in range(16):
                    self.sumR = self.sumR + self.CalcR(self.ktg1[m] - self.num, self.tR[m])
                if self.sumR < 32:
                    self.nR = self.sumR
                    self.chk = False
                self.num = self.num + 1
                self.sumR = 0
            if self.num > 10:
                print("Категория худшая")
                nKat = 0
            else:
                print("xR = ", self.nR)
                print("R = ", self.ktg1[7] - (self.num - 1))
                nKat = self.ktg1[7] - (self.num - 1)

        for i in range(7):
            self.qi[i] = self.gr[i] - self.Qq[i] - self.ps[i]
            self.Qi[i] = self.qi[i] - self.dA[i]
            if self.Qi[i] > 0:
                self.pi[i] = 1 - (
                            (0.78 + 5.46 * math.exp(-4.3 * math.pow(10, -3) * math.pow((27.3 - self.Qi[i]), 2))) / (
                            1 + math.pow(10, (0.1 * self.Qi[i]))))
            else:
                self.pi[i] = (0.78 + 5.46 * math.exp(
                    -4.3 * math.pow(10, -3) * math.pow((27.3 - math.fabs(self.Qi[i])), 2))) / (
                                     1 + math.pow(10, (0.1 * math.fabs(self.Qi[i]))))
            self.Ri[i] = self.pi[i] * self.ki[i]

        self.Rr = 0
        for i in range(7):
            self.Rr = self.Rr + self.Ri[i]

        self.Sr = 0
        if self.Rr <= 0.15:
            self.Sr = 4 * math.pow(self.Rr, 1.43)
        elif 0.15 < self.Rr <= 0.7:
            self.Sr = 1.1 * (1 - 1.17 * math.exp(-2.9 * self.Rr))
        else:
            self.Sr = 1.01 * (1 - 9.1 * math.exp(-6.9 * self.Rr))

        self.Wr = 0
        if self.Rr < 0.15:
            self.Wr = 1.54 * math.pow(self.Rr, 0.25) * (1 - math.exp(-11 * self.Rr))
        else:
            self.Wr = 1 - math.exp(-(11 * self.Rr) / (1 + 0.7 * self.Rr))

        print("R =", self.Rr)
        print("S =", self.Sr)
        print("W =", self.Wr)

        return [nKat, self.Rr, self.Sr, self.Wr]

    def check(self):
        if self.t1_Wb.value() != 0.0 and self.t2_Wb.value() != 0.0 and self.t3_Wb.value() != 0.0 and self.t4_Wb.value() != 0.0:

            # Проверка введенности данных для 1й стены
            if self.t1_Dbe.isChecked():
                if self.t1_DWb.value() != 0.0:
                    self.ready1d = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready1d = True
            if self.t1_Wbe.isChecked():
                if self.t1_WWb.value() != 0.0:
                    self.ready1w = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready1w = True
            if self.ready1d and self.ready1w:
                self.ready1 = True

            # Проверка введенности данных для 2й стены
            if self.t2_Dbe.isChecked():
                if self.t2_DWb.value() != 0.0:
                    self.ready2d = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready2d = True
            if self.t2_Wbe.isChecked():
                if self.t2_WWb.value() != 0.0:
                    self.ready2w = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready2w = True
            if self.ready2d and self.ready2w:
                self.ready2 = True

            # Проверка введенности данных для 3й стены
            if self.t3_Dbe.isChecked():
                if self.t3_DWb.value() != 0.0:
                    self.ready3d = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready3d = True
            if self.t3_Wbe.isChecked():
                if self.t3_WWb.value() != 0.0:
                    self.ready3w = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready3w = True
            if self.ready3d and self.ready3w:
                self.ready3 = True

            # Проверка введенности данных для 4й стены
            if self.t4_Dbe.isChecked():
                if self.t4_DWb.value() != 0.0:
                    self.ready4d = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready4d = True
            if self.t4_Wbe.isChecked():
                if self.t4_WWb.value() != 0.0:
                    self.ready4w = True
                else:
                    print("Сделать указатель на ошибку")
            else:
                self.ready4w = True
            if self.ready4d and self.ready4w:
                self.ready4 = True

            # Общая проверка данных
            if self.ready1 and self.ready2 and self.ready3 and self.ready4:
                print("Здесь будут все вычисления и тому подобное")
                self.R1 = 0  # Значение для 1 стены
                self.R2 = 0  # Значение для 2 стены
                self.R3 = 0  # Значение для 3 стены
                self.R4 = 0  # Значение для 4 стены
                self.R5 = 0  # Значение для пола
                self.R6 = 0  # Значение для потолка

                # 1 стена
                self.sa1 = self.t1_Wb.value()
                self.s21 = self.t1_DWb.value()
                self.s31 = self.t1_WWb.value()
                self.txtSs = self.t1_Mb.currentText()
                self.txtSn = 0
                if self.txtSs == "Кирпичная стена (0.5 кирпича)":
                    self.txtSn = 1
                elif self.txtSs == "Кирпичная стена (1 кирпич)":
                    self.txtSn = 2
                elif self.txtSs == "Кирпичная стена (1.5 кирпича)":
                    self.txtSn = 3
                elif self.txtSs == "Кирпичная стена (2 кирпича)":
                    self.txtSn = 4
                elif self.txtSs == "Кирпичная стена (2.5 кирпича)":
                    self.txtSn = 5
                elif self.txtSs == "Стена из железобетонных блоков (40 мм)":
                    self.txtSn = 6
                elif self.txtSs == "Стена из железобетонных блоков (50 мм)":
                    self.txtSn = 7
                elif self.txtSs == "Стена из железобетонных блоков (100 мм)":
                    self.txtSn = 8
                elif self.txtSs == "Стена из железобетонных блоков (160 мм)":
                    self.txtSn = 9
                elif self.txtSs == "Стена из железобетонных блоков (200 мм)":
                    self.txtSn = 10
                elif self.txtSs == "Стена из железобетонных блоков (300 мм)":
                    self.txtSn = 11
                elif self.txtSs == "Стена из железобетонных блоков (400 мм)":
                    self.txtSn = 12
                elif self.txtSs == "Стена из железобетонных блоков (800 мм)":
                    self.txtSn = 13
                elif self.txtSs == "Гипсобетонные плиты (95 мм)":
                    self.txtSn = 14
                elif self.txtSs == "Стена из шлакоблоков (220 мм)":
                    self.txtSn = 15
                elif self.txtSs == "Перегородка из древесно-стружечной плиты (20 мм)":
                    self.txtSn = 16

                self.txtDs = self.t1_DMb.currentText()
                self.txtDn = 0
                if self.txtDs == "Щитовая дверь, облицованная фанерой с двух сторон, без прокладки":
                    self.txtDn = 1
                elif self.txtDs == "Щитовая дверь, облицованная фанерой с двух сторон, с прокладкой из пористой резины":
                    self.txtDn = 2
                elif self.txtDs == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, без прокладки":
                    self.txtDn = 3
                elif self.txtDs == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, с прокладкой из пористой резины":
                    self.txtDn = 4
                elif self.txtDs == "Филенчатая дверь без прокладки":
                    self.txtDn = 5
                elif self.txtDs == "Филенчатая дверь с прокладкой из пористой резины":
                    self.txtDn = 6
                elif self.txtDs == "Типовая дверь П-327 без прокладки":
                    self.txtDn = 7
                elif self.txtDs == "Типовая дверь П-327 с прокладкой из пористой резины":
                    self.txtDn = 8
                elif self.txtDs == "Дверь, изолирующая, облегченная":
                    self.txtDn = 9
                elif self.txtDs == "Дверь, изолирующая, двойная с зазором > 200 мм, облегченная":
                    self.txtDn = 10
                elif self.txtDs == "Дверь звукоизолирующая, тяжелая":
                    self.txtDn = 11
                elif self.txtDs == "Дверь, звукоизолирующая, двойная с зазором > 300 мм, тяжелая":
                    self.txtDn = 12
                elif self.txtDs == "Двери двойные с облицовкой тамбура, тяжелые":
                    self.txtDn = 13

                # print(self.txtDn, " это ", self.txtDs)

                self.txtWs = self.t1_WMb.currentText()
                self.txtWn = 0
                if self.txtWs == "Одинарное остекление (3 мм)":
                    self.txtWn = 1
                elif self.txtWs == "Одинарное остекление (4 мм)":
                    self.txtWn = 2
                elif self.txtWs == "Одинарное остекление (6 мм)":
                    self.txtWn = 3
                elif self.txtWs == "Двойное остекление с воздушным промежутком (3-57-3 мм)":
                    self.txtWn = 4
                elif self.txtWs == "Двойное остекление с воздушным промежутком (3-90-3 мм)":
                    self.txtWn = 5
                elif self.txtWs == "Двойное остекление с воздушным промежутком (4-57-4 мм)":
                    self.txtWn = 6
                elif self.txtWs == "Двойное остекление с воздушным промежутком (4-90-4 мм)":
                    self.txtWn = 7
                elif self.txtWs == "Двойное остекление с воздушным промежутком (6-57-6 мм)":
                    self.txtWn = 8
                elif self.txtWs == "Двойное остекление с воздушным промежутком (6-90-6 мм)":
                    self.txtWn = 9
                elif self.txtWs == "Двойное остекление с воздушным промежутком (4-100-4 мм)":
                    self.txtWn = 10
                elif self.txtWs == "Двойное остекление с воздушным промежутком (4-200-4 мм)":
                    self.txtWn = 11
                elif self.txtWs == "Двойное остекление с воздушным промежутком (4-400-4 мм)":
                    self.txtWn = 12
                elif self.txtWs == "Тройное остекление с воздушным промежутком (4-16-4-200-3 мм)":
                    self.txtWn = 13
                elif self.txtWs == "Тройное остекление с воздушным промежутком (4-16-4-650-3 мм)":
                    self.txtWn = 14
                elif self.txtWs == "Тройное остекление с воздушным промежутком (4-16-7-200-4 мм)":
                    self.txtWn = 15

                # print(self.txtWn, "это", self.txtWs)
                # 1 стена

                # 2 стена
                self.sa2 = self.t2_Wb.value()
                self.s22 = self.t2_DWb.value()
                self.s32 = self.t2_WWb.value()
                self.txtSs2 = self.t2_Mb.currentText()
                self.txtSn2 = 0
                if self.txtSs2 == "Кирпичная стена (0.5 кирпича)":
                    self.txtSn2 = 1
                elif self.txtSs2 == "Кирпичная стена (1 кирпич)":
                    self.txtSn2 = 2
                elif self.txtSs2 == "Кирпичная стена (1.5 кирпича)":
                    self.txtSn2 = 3
                elif self.txtSs2 == "Кирпичная стена (2 кирпича)":
                    self.txtSn2 = 4
                elif self.txtSs2 == "Кирпичная стена (2.5 кирпича)":
                    self.txtSn2 = 5
                elif self.txtSs2 == "Стена из железобетонных блоков (40 мм)":
                    self.txtSn2 = 6
                elif self.txtSs2 == "Стена из железобетонных блоков (50 мм)":
                    self.txtSn2 = 7
                elif self.txtSs2 == "Стена из железобетонных блоков (100 мм)":
                    self.txtSn2 = 8
                elif self.txtSs2 == "Стена из железобетонных блоков (160 мм)":
                    self.txtSn2 = 9
                elif self.txtSs2 == "Стена из железобетонных блоков (200 мм)":
                    self.txtSn2 = 10
                elif self.txtSs2 == "Стена из железобетонных блоков (300 мм)":
                    self.txtSn2 = 11
                elif self.txtSs2 == "Стена из железобетонных блоков (400 мм)":
                    self.txtSn2 = 12
                elif self.txtSs2 == "Стена из железобетонных блоков (800 мм)":
                    self.txtSn2 = 13
                elif self.txtSs2 == "Гипсобетонные плиты (95 мм)":
                    self.txtSn2 = 14
                elif self.txtSs2 == "Стена из шлакоблоков (220 мм)":
                    self.txtSn2 = 15
                elif self.txtSs2 == "Перегородка из древесно-стружечной плиты (20 мм)":
                    self.txtSn2 = 16

                self.txtDs2 = self.t2_DMb.currentText()
                self.txtDn2 = 0
                if self.txtDs2 == "Щитовая дверь, облицованная фанерой с двух сторон, без прокладки":
                    self.txtDn2 = 1
                elif self.txtDs2 == "Щитовая дверь, облицованная фанерой с двух сторон, с прокладкой из пористой резины":
                    self.txtDn2 = 2
                elif self.txtDs2 == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, без прокладки":
                    self.txtDn2 = 3
                elif self.txtDs2 == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, с прокладкой из пористой резины":
                    self.txtDn2 = 4
                elif self.txtDs2 == "Филенчатая дверь без прокладки":
                    self.txtDn2 = 5
                elif self.txtDs2 == "Филенчатая дверь с прокладкой из пористой резины":
                    self.txtDn2 = 6
                elif self.txtDs2 == "Типовая дверь П-327 без прокладки":
                    self.txtDn2 = 7
                elif self.txtDs2 == "Типовая дверь П-327 с прокладкой из пористой резины":
                    self.txtDn2 = 8
                elif self.txtDs2 == "Дверь, изолирующая, облегченная":
                    self.txtDn2 = 9
                elif self.txtDs2 == "Дверь, изолирующая, двойная с зазором > 200 мм, облегченная":
                    self.txtDn2 = 10
                elif self.txtDs2 == "Дверь звукоизолирующая, тяжелая":
                    self.txtDn2 = 11
                elif self.txtDs2 == "Дверь, звукоизолирующая, двойная с зазором > 300 мм, тяжелая":
                    self.txtDn2 = 12
                elif self.txtDs2 == "Двери двойные с облицовкой тамбура, тяжелые":
                    self.txtDn2 = 13

                # print(self.txtDn, " это ", self.txtDs)

                self.txtWs2 = self.t2_WMb.currentText()
                self.txtWn2 = 0
                if self.txtWs2 == "Одинарное остекление (3 мм)":
                    self.txtWn2 = 1
                elif self.txtWs2 == "Одинарное остекление (4 мм)":
                    self.txtWn2 = 2
                elif self.txtWs2 == "Одинарное остекление (6 мм)":
                    self.txtWn2 = 3
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (3-57-3 мм)":
                    self.txtWn2 = 4
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (3-90-3 мм)":
                    self.txtWn2 = 5
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (4-57-4 мм)":
                    self.txtWn2 = 6
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (4-90-4 мм)":
                    self.txtWn2 = 7
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (6-57-6 мм)":
                    self.txtWn2 = 8
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (6-90-6 мм)":
                    self.txtWn2 = 9
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (4-100-4 мм)":
                    self.txtWn2 = 10
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (4-200-4 мм)":
                    self.txtWn2 = 11
                elif self.txtWs2 == "Двойное остекление с воздушным промежутком (4-400-4 мм)":
                    self.txtWn2 = 12
                elif self.txtWs2 == "Тройное остекление с воздушным промежутком (4-16-4-200-3 мм)":
                    self.txtWn2 = 13
                elif self.txtWs2 == "Тройное остекление с воздушным промежутком (4-16-4-650-3 мм)":
                    self.txtWn2 = 14
                elif self.txtWs2 == "Тройное остекление с воздушным промежутком (4-16-7-200-4 мм)":
                    self.txtWn2 = 15

                # print(self.txtWn2, "это", self.txtWs2)
                # 2 стена

                # 3 стена
                self.sa3 = self.t3_Wb.value()
                self.s23 = self.t3_DWb.value()
                self.s33 = self.t3_WWb.value()
                self.txtSs3 = self.t3_Mb.currentText()
                self.txtSn3 = 0
                if self.txtSs3 == "Кирпичная стена (0.5 кирпича)":
                    self.txtSn3 = 1
                elif self.txtSs3 == "Кирпичная стена (1 кирпич)":
                    self.txtSn3 = 2
                elif self.txtSs3 == "Кирпичная стена (1.5 кирпича)":
                    self.txtSn3 = 3
                elif self.txtSs3 == "Кирпичная стена (2 кирпича)":
                    self.txtSn3 = 4
                elif self.txtSs3 == "Кирпичная стена (2.5 кирпича)":
                    self.txtSn3 = 5
                elif self.txtSs3 == "Стена из железобетонных блоков (40 мм)":
                    self.txtSn3 = 6
                elif self.txtSs3 == "Стена из железобетонных блоков (50 мм)":
                    self.txtSn3 = 7
                elif self.txtSs3 == "Стена из железобетонных блоков (100 мм)":
                    self.txtSn3 = 8
                elif self.txtSs3 == "Стена из железобетонных блоков (160 мм)":
                    self.txtSn3 = 9
                elif self.txtSs3 == "Стена из железобетонных блоков (200 мм)":
                    self.txtSn3 = 10
                elif self.txtSs3 == "Стена из железобетонных блоков (300 мм)":
                    self.txtSn3 = 11
                elif self.txtSs3 == "Стена из железобетонных блоков (400 мм)":
                    self.txtSn3 = 12
                elif self.txtSs3 == "Стена из железобетонных блоков (800 мм)":
                    self.txtSn3 = 13
                elif self.txtSs3 == "Гипсобетонные плиты (95 мм)":
                    self.txtSn3 = 14
                elif self.txtSs3 == "Стена из шлакоблоков (220 мм)":
                    self.txtSn3 = 15
                elif self.txtSs3 == "Перегородка из древесно-стружечной плиты (20 мм)":
                    self.txtSn3 = 16

                self.txtDs3 = self.t3_DMb.currentText()
                self.txtDn3 = 0
                if self.txtDs3 == "Щитовая дверь, облицованная фанерой с двух сторон, без прокладки":
                    self.txtDn3 = 1
                elif self.txtDs3 == "Щитовая дверь, облицованная фанерой с двух сторон, с прокладкой из пористой резины":
                    self.txtDn3 = 2
                elif self.txtDs3 == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, без прокладки":
                    self.txtDn3 = 3
                elif self.txtDs3 == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, с прокладкой из пористой резины":
                    self.txtDn3 = 4
                elif self.txtDs3 == "Филенчатая дверь без прокладки":
                    self.txtDn3 = 5
                elif self.txtDs3 == "Филенчатая дверь с прокладкой из пористой резины":
                    self.txtDn3 = 6
                elif self.txtDs3 == "Типовая дверь П-327 без прокладки":
                    self.txtDn3 = 7
                elif self.txtDs3 == "Типовая дверь П-327 с прокладкой из пористой резины":
                    self.txtDn3 = 8
                elif self.txtDs3 == "Дверь, изолирующая, облегченная":
                    self.txtDn3 = 9
                elif self.txtDs3 == "Дверь, изолирующая, двойная с зазором > 200 мм, облегченная":
                    self.txtDn3 = 10
                elif self.txtDs3 == "Дверь звукоизолирующая, тяжелая":
                    self.txtDn3 = 11
                elif self.txtDs3 == "Дверь, звукоизолирующая, двойная с зазором > 300 мм, тяжелая":
                    self.txtDn3 = 12
                elif self.txtDs3 == "Двери двойные с облицовкой тамбура, тяжелые":
                    self.txtDn3 = 13

                # print(self.txtDn, " это ", self.txtDs)

                self.txtWs3 = self.t3_WMb.currentText()
                self.txtWn3 = 0
                if self.txtWs3 == "Одинарное остекление (3 мм)":
                    self.txtWn3 = 1
                elif self.txtWs3 == "Одинарное остекление (4 мм)":
                    self.txtWn3 = 2
                elif self.txtWs3 == "Одинарное остекление (6 мм)":
                    self.txtWn3 = 3
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (3-57-3 мм)":
                    self.txtWn3 = 4
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (3-90-3 мм)":
                    self.txtWn3 = 5
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (4-57-4 мм)":
                    self.txtWn3 = 6
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (4-90-4 мм)":
                    self.txtWn3 = 7
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (6-57-6 мм)":
                    self.txtWn3 = 8
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (6-90-6 мм)":
                    self.txtWn3 = 9
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (4-100-4 мм)":
                    self.txtWn3 = 10
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (4-200-4 мм)":
                    self.txtWn3 = 11
                elif self.txtWs3 == "Двойное остекление с воздушным промежутком (4-400-4 мм)":
                    self.txtWn3 = 12
                elif self.txtWs3 == "Тройное остекление с воздушным промежутком (4-16-4-200-3 мм)":
                    self.txtWn3 = 13
                elif self.txtWs3 == "Тройное остекление с воздушным промежутком (4-16-4-650-3 мм)":
                    self.txtWn3 = 14
                elif self.txtWs3 == "Тройное остекление с воздушным промежутком (4-16-7-200-4 мм)":
                    self.txtWn3 = 15

                # print(self.txtWn3, "это", self.txtWs3)
                # 3 стена

                # 4 стена
                self.sa4 = self.t4_Wb.value()
                self.s24 = self.t4_DWb.value()
                self.s34 = self.t4_WWb.value()
                self.txtSs4 = self.t4_Mb.currentText()
                self.txtSn4 = 0
                if self.txtSs4 == "Кирпичная стена (0.5 кирпича)":
                    self.txtSn4 = 1
                elif self.txtSs4 == "Кирпичная стена (1 кирпич)":
                    self.txtSn4 = 2
                elif self.txtSs4 == "Кирпичная стена (1.5 кирпича)":
                    self.txtSn4 = 3
                elif self.txtSs4 == "Кирпичная стена (2 кирпича)":
                    self.txtSn4 = 4
                elif self.txtSs4 == "Кирпичная стена (2.5 кирпича)":
                    self.txtSn4 = 5
                elif self.txtSs4 == "Стена из железобетонных блоков (40 мм)":
                    self.txtSn4 = 6
                elif self.txtSs4 == "Стена из железобетонных блоков (50 мм)":
                    self.txtSn4 = 7
                elif self.txtSs4 == "Стена из железобетонных блоков (100 мм)":
                    self.txtSn4 = 8
                elif self.txtSs4 == "Стена из железобетонных блоков (160 мм)":
                    self.txtSn4 = 9
                elif self.txtSs4 == "Стена из железобетонных блоков (200 мм)":
                    self.txtSn4 = 10
                elif self.txtSs4 == "Стена из железобетонных блоков (300 мм)":
                    self.txtSn4 = 11
                elif self.txtSs4 == "Стена из железобетонных блоков (400 мм)":
                    self.txtSn4 = 12
                elif self.txtSs4 == "Стена из железобетонных блоков (800 мм)":
                    self.txtSn4 = 13
                elif self.txtSs4 == "Гипсобетонные плиты (95 мм)":
                    self.txtSn4 = 14
                elif self.txtSs4 == "Стена из шлакоблоков (220 мм)":
                    self.txtSn4 = 15
                elif self.txtSs4 == "Перегородка из древесно-стружечной плиты (20 мм)":
                    self.txtSn4 = 16

                self.txtDs4 = self.t4_DMb.currentText()
                self.txtDn4 = 0
                if self.txtDs4 == "Щитовая дверь, облицованная фанерой с двух сторон, без прокладки":
                    self.txtDn4 = 1
                elif self.txtDs4 == "Щитовая дверь, облицованная фанерой с двух сторон, с прокладкой из пористой резины":
                    self.txtDn4 = 2
                elif self.txtDs4 == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, без прокладки":
                    self.txtDn4 = 3
                elif self.txtDs4 == "Щитовая дверь из древесноволокнистых плит с зазором, заполненным стекловатой, с прокладкой из пористой резины":
                    self.txtDn4 = 4
                elif self.txtDs4 == "Филенчатая дверь без прокладки":
                    self.txtDn4 = 5
                elif self.txtDs4 == "Филенчатая дверь с прокладкой из пористой резины":
                    self.txtDn4 = 6
                elif self.txtDs4 == "Типовая дверь П-327 без прокладки":
                    self.txtDn4 = 7
                elif self.txtDs4 == "Типовая дверь П-327 с прокладкой из пористой резины":
                    self.txtDn4 = 8
                elif self.txtDs4 == "Дверь, изолирующая, облегченная":
                    self.txtDn4 = 9
                elif self.txtDs4 == "Дверь, изолирующая, двойная с зазором > 200 мм, облегченная":
                    self.txtDn4 = 10
                elif self.txtDs4 == "Дверь звукоизолирующая, тяжелая":
                    self.txtDn4 = 11
                elif self.txtDs4 == "Дверь, звукоизолирующая, двойная с зазором > 300 мм, тяжелая":
                    self.txtDn4 = 12
                elif self.txtDs4 == "Двери двойные с облицовкой тамбура, тяжелые":
                    self.txtDn4 = 13

                # print(self.txtDn, " это ", self.txtDs)

                self.txtWs4 = self.t4_WMb.currentText()
                self.txtWn4 = 0
                if self.txtWs4 == "Одинарное остекление (3 мм)":
                    self.txtWn4 = 1
                elif self.txtWs4 == "Одинарное остекление (4 мм)":
                    self.txtWn4 = 2
                elif self.txtWs4 == "Одинарное остекление (6 мм)":
                    self.txtWn4 = 3
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (3-57-3 мм)":
                    self.txtWn4 = 4
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (3-90-3 мм)":
                    self.txtWn4 = 5
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (4-57-4 мм)":
                    self.txtWn4 = 6
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (4-90-4 мм)":
                    self.txtWn4 = 7
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (6-57-6 мм)":
                    self.txtWn4 = 8
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (6-90-6 мм)":
                    self.txtWn4 = 9
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (4-100-4 мм)":
                    self.txtWn4 = 10
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (4-200-4 мм)":
                    self.txtWn4 = 11
                elif self.txtWs4 == "Двойное остекление с воздушным промежутком (4-400-4 мм)":
                    self.txtWn4 = 12
                elif self.txtWs4 == "Тройное остекление с воздушным промежутком (4-16-4-200-3 мм)":
                    self.txtWn4 = 13
                elif self.txtWs4 == "Тройное остекление с воздушным промежутком (4-16-4-650-3 мм)":
                    self.txtWn4 = 14
                elif self.txtWs4 == "Тройное остекление с воздушным промежутком (4-16-7-200-4 мм)":
                    self.txtWn4 = 15

                # print(self.txtWn4, "это", self.txtWs4)
                # 4 стена

                # пол/потолок
                self.txtSs5 = self.t5_Mb1.currentText()
                self.txtSs6 = self.t5_Mb2.currentText()
                self.txtSn5 = 0
                self.txtSn6 = 0
                if self.txtSs5 == "Железобетонное сплошное перекрытие (120 мм)":
                    self.txtSn5 = 1
                elif self.txtSs5 == "Железобетонное сплошное перекрытие (140 мм)":
                    self.txtSn5 = 2
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 1":
                    self.txtSn5 = 3
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 2":
                    self.txtSn5 = 4
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 3":
                    self.txtSn5 = 5
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 4":
                    self.txtSn5 = 6
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 5":
                    self.txtSn5 = 7
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 6":
                    self.txtSn5 = 8
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 7":
                    self.txtSn5 = 9
                elif self.txtSs5 == "Железобетонное многопустотное перекрытие с плавающим полом - 8":
                    self.txtSn5 = 10

                if self.txtSs6 == "Железобетонное сплошное перекрытие (120 мм)":
                    self.txtSn6 = 1
                elif self.txtSs6 == "Железобетонное сплошное перекрытие (140 мм)":
                    self.txtSn6 = 2
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 1":
                    self.txtSn6 = 3
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 2":
                    self.txtSn6 = 4
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 3":
                    self.txtSn6 = 5
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 4":
                    self.txtSn6 = 6
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 5":
                    self.txtSn6 = 7
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 6":
                    self.txtSn6 = 8
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 7":
                    self.txtSn6 = 9
                elif self.txtSs6 == "Железобетонное многопустотное перекрытие с плавающим полом - 8":
                    self.txtSn6 = 10

                # print(self.txtSn6)
                numEls1 = 1
                numEls2 = 1
                numEls3 = 1
                numEls4 = 1

                if self.t1_Dbe.isChecked():
                    numEls1 = numEls1 + 1
                if self.t1_Wbe.isChecked():
                    numEls1 = numEls1 + 1

                if self.t2_Dbe.isChecked():
                    numEls2 = numEls2 + 1
                if self.t2_Wbe.isChecked():
                    numEls2 = numEls2 + 1

                if self.t3_Dbe.isChecked():
                    numEls3 = numEls3 + 1
                if self.t3_Wbe.isChecked():
                    numEls3 = numEls3 + 1

                if self.t4_Dbe.isChecked():
                    numEls4 = numEls4 + 1
                if self.t4_Wbe.isChecked():
                    numEls4 = numEls4 + 1

                self.R1 = self.Calc_Res(1, numEls1)[0]
                self.R2 = self.Calc_Res(2, numEls2)[0]
                self.R3 = self.Calc_Res(3, numEls3)[0]
                self.R4 = self.Calc_Res(4, numEls4)[0]
                self.R5 = self.Calc_Res(5, 1)[0]
                self.R6 = self.Calc_Res(6, 1)[0]

                self.Rr1 = self.Calc_Res(1, numEls1)[1]
                self.Rr2 = self.Calc_Res(2, numEls2)[1]
                self.Rr3 = self.Calc_Res(3, numEls3)[1]
                self.Rr4 = self.Calc_Res(4, numEls4)[1]
                self.Rr5 = self.Calc_Res(5, 1)[1]
                self.Rr6 = self.Calc_Res(6, 1)[1]

                self.Sr1 = self.Calc_Res(1, numEls1)[2]
                self.Sr2 = self.Calc_Res(2, numEls2)[2]
                self.Sr3 = self.Calc_Res(3, numEls3)[2]
                self.Sr4 = self.Calc_Res(4, numEls4)[2]
                self.Sr5 = self.Calc_Res(5, 1)[2]
                self.Sr6 = self.Calc_Res(6, 1)[2]

                self.Wr1 = self.Calc_Res(1, numEls1)[3]
                self.Wr2 = self.Calc_Res(2, numEls2)[3]
                self.Wr3 = self.Calc_Res(3, numEls3)[3]
                self.Wr4 = self.Calc_Res(4, numEls4)[3]
                self.Wr5 = self.Calc_Res(5, 1)[3]
                self.Wr6 = self.Calc_Res(6, 1)[3]

                self.Rr1p = self.Rr1 * 100
                self.Rr2p = self.Rr2 * 100
                self.Rr3p = self.Rr3 * 100
                self.Rr4p = self.Rr4 * 100
                self.Rr5p = self.Rr5 * 100
                self.Rr6p = self.Rr6 * 100

                self.Sr1p = self.Sr1 * 100
                self.Sr2p = self.Sr2 * 100
                self.Sr3p = self.Sr3 * 100
                self.Sr4p = self.Sr4 * 100
                self.Sr5p = self.Sr5 * 100
                self.Sr6p = self.Sr6 * 100

                self.Wr1p = self.Wr1 * 100
                self.Wr2p = self.Wr2 * 100
                self.Wr3p = self.Wr3 * 100
                self.Wr4p = self.Wr4 * 100
                self.Wr5p = self.Wr5 * 100
                self.Wr6p = self.Wr6 * 100

                print("R1 =", self.R1)
                print("R2 =", self.R2)
                print("R3 =", self.R3)
                print("R4 =", self.R4)
                print("R5 =", self.R5)
                print("R6 =", self.R6)

                self.kr1 = 'Речь абсолютно не понятна'
                self.kr2 = 'Речь предельно допустимая (требуются многократные переспросы одного и того же материала с передачей отдельных слов по буквам при полном напряжении слуха)'
                self.kr3 = 'Речь удовлетворительная (трудно разговаривать, необходимы переспросы)'
                self.kr4 = 'Речь хорошая (возникает необходимость в отдельных переспросах редко встречающихся слов или названий)'
                self.kr5 = 'Речь отличная (понятность полная, без переспросов)'
                self.raR1 = self.kr1
                self.raR2 = self.kr1
                self.raR3 = self.kr1
                self.raR4 = self.kr1
                self.raR5 = self.kr1
                self.raR6 = self.kr1

                if self.Wr1 < 0.75:
                    self.raR1 = self.kr1
                elif 0.75 <= self.Wr1 < 0.85:
                    self.raR1 = self.kr2
                elif 0.85 <= self.Wr1 < 0.9:
                    self.raR1 = self.kr3
                elif 0.9 <= self.Wr1 < 0.95:
                    self.raR1 = self.kr4
                else:
                    self.raR1 = self.kr5

                if self.Wr2 < 0.75:
                    self.raR2 = self.kr1
                elif 0.75 <= self.Wr2 < 0.85:
                    self.raR2 = self.kr2
                elif 0.85 <= self.Wr2 < 0.9:
                    self.raR2 = self.kr3
                elif 0.9 <= self.Wr2 < 0.95:
                    self.raR2 = self.kr4
                else:
                    self.raR2 = self.kr5

                if self.Wr3 < 0.75:
                    self.raR3 = self.kr1
                elif 0.75 <= self.Wr3 < 0.85:
                    self.raR3 = self.kr2
                elif 0.85 <= self.Wr3 < 0.9:
                    self.raR3 = self.kr3
                elif 0.9 <= self.Wr3 < 0.95:
                    self.raR3 = self.kr4
                else:
                    self.raR3 = self.kr5

                if self.Wr4 < 0.75:
                    self.raR4 = self.kr1
                elif 0.75 <= self.Wr4 < 0.85:
                    self.raR4 = self.kr2
                elif 0.85 <= self.Wr4 < 0.9:
                    self.raR4 = self.kr3
                elif 0.9 <= self.Wr4 < 0.95:
                    self.raR4 = self.kr4
                else:
                    self.raR4 = self.kr5

                if self.Wr5 < 0.75:
                    self.raR5 = self.kr1
                elif 0.75 <= self.Wr5 < 0.85:
                    self.raR5 = self.kr2
                elif 0.85 <= self.Wr5 < 0.9:
                    self.raR5 = self.kr3
                elif 0.9 <= self.Wr5 < 0.95:
                    self.raR5 = self.kr4
                else:
                    self.raR5 = self.kr5

                if self.Wr6 < 0.75:
                    self.raR6 = self.kr1
                elif 0.75 <= self.Wr6 < 0.85:
                    self.raR6 = self.kr2
                elif 0.85 <= self.Wr6 < 0.9:
                    self.raR6 = self.kr3
                elif 0.9 <= self.Wr6 < 0.95:
                    self.raR6 = self.kr4
                else:
                    self.raR6 = self.kr5


                self.k1 = 53
                self.k2 = 48
                self.k3 = 43

                # 1 стена информация
                if self.R1 >= self.k1:
                    self.kat1 = 1
                elif self.R1 >= self.k2 and self.R1 < self.k1:
                    self.kat1 = 2
                elif self.R1 >= self.k3 and self.R1 < self.k2:
                    self.kat1 = 3
                else:
                    self.kat1 = 0

                # 2 стена информация
                if self.R2 >= self.k1:
                    self.kat2 = 1
                elif self.R2 >= self.k2 and self.R2 < self.k1:
                    self.kat2 = 2
                elif self.R2 >= self.k3 and self.R2 < self.k2:
                    self.kat2 = 3
                else:
                    self.kat2 = 0

                # 3 стена информация
                if self.R3 >= self.k1:
                    self.kat3 = 1
                elif self.R3 >= self.k2 and self.R3 < self.k1:
                    self.kat3 = 2
                elif self.R3 >= self.k3 and self.R3 < self.k2:
                    self.kat3 = 3
                else:
                    self.kat3 = 0

                # 4 стена информация
                if self.R4 >= self.k1:
                    self.kat4 = 1
                elif self.R4 >= self.k2 and self.R4 < self.k1:
                    self.kat4 = 2
                elif self.R4 >= self.k3 and self.R4 < self.k2:
                    self.kat4 = 3
                else:
                    self.kat4 = 0

                # Пол информация
                if self.R5 >= self.k1:
                    self.kat5 = 1
                elif self.R5 >= self.k2 and self.R5 < self.k1:
                    self.kat5 = 2
                elif self.R5 >= self.k3 and self.R5 < self.k2:
                    self.kat5 = 3
                else:
                    self.kat5 = 0

                # Потолок информация
                if self.R6 >= self.k1:
                    self.kat6 = 1
                elif self.R6 >= self.k2 and self.R6 < self.k1:
                    self.kat6 = 2
                elif self.R6 >= self.k3 and self.R6 < self.k2:
                    self.kat6 = 3
                else:
                    self.kat6 = 0

                #self.close()
                #self.reportWindow = ReportWindow()
                #self.reportWindow.show()

                self.okat = 0
                if self.kat1 == 0 or self.kat2 == 0 or self.kat3 == 0 or self.kat4 == 0 or self.kat5 == 0 or self.kat6 == 0:
                    self.okat = 0
                else:
                    self.okat = max(self.kat1, self.kat2, self.kat3, self.kat4, self.kat5, self.kat6)

                self.okatxt = 'Не подходит под выделенное помещение'
                if self.okat == 1:
                    self.okatxt = 'Помещение подходит под категорию для обработки сведений, содержащих гриф "Особой важности"'
                elif self.okat == 2:
                    self.okatxt = 'Помещение подходит под категорию для обработки сведений, содержащих гриф "Совершенно секретно"'
                elif self.okat == 3:
                    self.okatxt = 'Помещение подходит под категорию для обработки сведений, содержащих гриф "Секретно"'


                txtreport = 'Категория для первой стены: ' + str(self.kat1) + '\n' + \
                            'Категория для второй стены: ' + str(self.kat2) + '\n' + \
                            'Категория для третьей стены: ' + str(self.kat3) + '\n' + \
                            'Категория для четвертой стены: ' + str(self.kat4) + '\n' + \
                            'Категория для пола: ' + str(self.kat5) + '\n' + \
                            'Категория для потолка: ' + str(self.kat6) + '\n' + \
                            'Общая категория помещения: ' + str(self.okat) + '\n' + \
                            self.okatxt + '\n' + '\n' + \
                            'Для учета защиты речевой информации были расчитаны параметры:' + '\n' + \
                            'R - интегральный индекс артикуляции;' + '\n' + \
                            'S - слоговая разборчивость;' + '\n' + \
                            'W - словесная разборчивость;' + '\n' + \
                            'И была определена разборчивость речи.' + '\n' + '\n' + \
                            'Для первой стены:' + '\n' + \
                            'R = ' + str(round(self.Rr1, 5)) + ' (' + str(round(self.Rr1p, 2)) + '%)' + '\n' + \
                            'S = ' + str(round(self.Sr1, 5)) + ' (' + str(round(self.Sr1p, 2)) + '%)' + '\n' + \
                            'W = ' + str(round(self.Wr1, 5)) + ' (' + str(round(self.Wr1p, 2)) + '%)' + '\n' + \
                            'Разборчивость речи: ' + self.raR1 + '\n' + '\n' + \
                            'Для второй стены:' + '\n' + \
                            'R = ' + str(round(self.Rr2, 5)) + ' (' + str(round(self.Rr2p, 2)) + '%)' + '\n' + \
                            'S = ' + str(round(self.Sr2, 5)) + ' (' + str(round(self.Sr2p, 2)) + '%)' + '\n' + \
                            'W = ' + str(round(self.Wr2, 5)) + ' (' + str(round(self.Wr2p, 2)) + '%)' + '\n' + \
                            'Разборчивость речи: ' + self.raR2 + '\n' + '\n' + \
                            'Для третьей стены:' + '\n' + \
                            'R = ' + str(round(self.Rr3, 5)) + ' (' + str(round(self.Rr3p, 2)) + '%)' + '\n' + \
                            'S = ' + str(round(self.Sr3, 5)) + ' (' + str(round(self.Sr3p, 2)) + '%)' + '\n' + \
                            'W = ' + str(round(self.Wr3, 5)) + ' (' + str(round(self.Wr3p, 2)) + '%)' + '\n' + \
                            'Разборчивость речи: ' + self.raR3 + '\n' + '\n' + \
                            'Для четвертой стены:' + '\n' + \
                            'R = ' + str(round(self.Rr4, 5)) + ' (' + str(round(self.Rr4p, 2)) + '%)' + '\n' + \
                            'S = ' + str(round(self.Sr4, 5)) + ' (' + str(round(self.Sr4p, 2)) + '%)' + '\n' + \
                            'W = ' + str(round(self.Wr4, 5)) + ' (' + str(round(self.Wr4p, 2)) + '%)' + '\n' + \
                            'Разборчивость речи: ' + self.raR4 + '\n' + '\n' + \
                            'Для пола:' + '\n' + \
                            'R = ' + str(round(self.Rr5, 5)) + ' (' + str(round(self.Rr5p, 2)) + '%)' + '\n' + \
                            'S = ' + str(round(self.Sr5, 5)) + ' (' + str(round(self.Sr5p, 2)) + '%)' + '\n' + \
                            'W = ' + str(round(self.Wr5, 5)) + ' (' + str(round(self.Wr5p, 2)) + '%)' + '\n' + \
                            'Разборчивость речи: ' + self.raR5 + '\n' + '\n' + \
                            'Для потолка:' + '\n' + \
                            'R = ' + str(round(self.Rr6, 5)) + ' (' + str(round(self.Rr6p, 2)) + '%)' + '\n' + \
                            'S = ' + str(round(self.Sr6, 5)) + ' (' + str(round(self.Sr6p, 2)) + '%)' + '\n' + \
                            'W = ' + str(round(self.Wr6, 5)) + ' (' + str(round(self.Wr6p, 2)) + '%)' + '\n' + \
                            'Разборчивость речи: ' + self.raR6 + '\n'
                print(txtreport)

                report = QMessageBox()
                report.setWindowTitle("Отчет")
                report.setText(txtreport)
                report.setStandardButtons(QMessageBox.Ok | QMessageBox.Save)

                report.exec_()

            else:
                print(
                    "А здесь выскочит окно, что не введены какие-то данные и по указателям ошибок выведется вся информация")
        else:
            print("Здесь выскочит окно, что не введены какие-то данные и по указателям ошибок выведется вся информация")

    def t1_Dbe_click(self):
        if self.t1_Dbe.isChecked():
            self.t1_DWl.setEnabled(True)
            self.t1_DWb.setEnabled(True)
            self.t1_DMl.setEnabled(True)
            self.t1_DMb.setEnabled(True)
        else:
            self.t1_DWl.setEnabled(False)
            self.t1_DWb.setEnabled(False)
            self.t1_DMl.setEnabled(False)
            self.t1_DMb.setEnabled(False)

    def t1_Wbe_click(self):
        if self.t1_Wbe.isChecked():
            self.t1_WWl.setEnabled(True)
            self.t1_WWb.setEnabled(True)
            self.t1_WMl.setEnabled(True)
            self.t1_WMb.setEnabled(True)
        else:
            self.t1_WWl.setEnabled(False)
            self.t1_WWb.setEnabled(False)
            self.t1_WMl.setEnabled(False)
            self.t1_WMb.setEnabled(False)

    def t2_Dbe_click(self):
        if self.t2_Dbe.isChecked():
            self.t2_DWl.setEnabled(True)
            self.t2_DWb.setEnabled(True)
            self.t2_DMl.setEnabled(True)
            self.t2_DMb.setEnabled(True)
        else:
            self.t2_DWl.setEnabled(False)
            self.t2_DWb.setEnabled(False)
            self.t2_DMl.setEnabled(False)
            self.t2_DMb.setEnabled(False)

    def t2_Wbe_click(self):
        if self.t2_Wbe.isChecked():
            self.t2_WWl.setEnabled(True)
            self.t2_WWb.setEnabled(True)
            self.t2_WMl.setEnabled(True)
            self.t2_WMb.setEnabled(True)
        else:
            self.t2_WWl.setEnabled(False)
            self.t2_WWb.setEnabled(False)
            self.t2_WMl.setEnabled(False)
            self.t2_WMb.setEnabled(False)

    def t3_Dbe_click(self):
        if self.t3_Dbe.isChecked():
            self.t3_DWl.setEnabled(True)
            self.t3_DWb.setEnabled(True)
            self.t3_DMl.setEnabled(True)
            self.t3_DMb.setEnabled(True)
        else:
            self.t3_DWl.setEnabled(False)
            self.t3_DWb.setEnabled(False)
            self.t3_DMl.setEnabled(False)
            self.t3_DMb.setEnabled(False)

    def t3_Wbe_click(self):
        if self.t3_Wbe.isChecked():
            self.t3_WWl.setEnabled(True)
            self.t3_WWb.setEnabled(True)
            self.t3_WMl.setEnabled(True)
            self.t3_WMb.setEnabled(True)
        else:
            self.t3_WWl.setEnabled(False)
            self.t3_WWb.setEnabled(False)
            self.t3_WMl.setEnabled(False)
            self.t3_WMb.setEnabled(False)

    def t4_Dbe_click(self):
        if self.t4_Dbe.isChecked():
            self.t4_DWl.setEnabled(True)
            self.t4_DWb.setEnabled(True)
            self.t4_DMl.setEnabled(True)
            self.t4_DMb.setEnabled(True)
        else:
            self.t4_DWl.setEnabled(False)
            self.t4_DWb.setEnabled(False)
            self.t4_DMl.setEnabled(False)
            self.t4_DMb.setEnabled(False)

    def t4_Wbe_click(self):
        if self.t4_Wbe.isChecked():
            self.t4_WWl.setEnabled(True)
            self.t4_WWb.setEnabled(True)
            self.t4_WMl.setEnabled(True)
            self.t4_WMb.setEnabled(True)
        else:
            self.t4_WWl.setEnabled(False)
            self.t4_WWb.setEnabled(False)
            self.t4_WMl.setEnabled(False)
            self.t4_WMb.setEnabled(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
