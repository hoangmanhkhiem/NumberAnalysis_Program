from PyQt5 import QtGui, QtWidgets,QtCore
import sys,webbrowser
import home
import homenoisuy,lagrange,newtoncachdeu,newton,about
import menutichphan,calchinhthang,calcsimpson
import calcgauss
import calctieptuyen, calcchiadoi, calcdaycung,calclap
import menudaoham,calcdaoham
import menunghiempt,menunghiemhpt
import numpy as np
import calcjacobi,calcgausskhu
import hdsd
from math import factorial
from sympy import symbols, sympify, lambdify,Symbol,expand
from tkinter import *
from tkinter import messagebox
import login

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow1 = QtWidgets.QMainWindow()


#Thông báo đầu phần mèm
def Alert():
    messagebox.showinfo("Hoàng Mạnh Khiêm VipPro","Hello lại là Khiêm đây!")
    messagebox.showwarning("Hoàng Mạnh Khiêm VipPro","Nhớ đọc hướng dẫn trước khi sử dụng nhé!")
    
def LOGIN():
    global ai
    ai = login.Ui_MainWindow()
    ai.setupUi(MainWindow)
    ai.login.clicked.connect(log)
    ai.again.clicked.connect(reset)
    MainWindow.show()
    
def log():
        if ai.taikhoan.text() == "khiemvippro" and ai.password.text()== "18042004":
            messagebox.showinfo("Hoàng Mạnh Khiêm VipPro","Đăng nhập thành công")
            mainUi()
        else:
            messagebox.showwarning("Hoàng Mạnh Khiêm VipPro","Sai tài khoản hoặc mật khẩu\nVui lòng nhập lại hoặc liên hệ Admin")
    
def reset():
        ai.taikhoan.setText("")
        ai.password.setText("")
        

#Hàm trỏ đường dẫn
def mainUi():
    global ui
    ui = home.Ui_menu()
    ui.setupUi(MainWindow)
    ui.ppnoisuy.clicked.connect(NOISUY.PP_noisuy)
    ui.about.clicked.connect(ABOUT.About)
    ui.ppnghiemcuapt.clicked.connect(NGHIEMPT.PP_NGHIEMPT)
    ui.ppnghiemhpt.clicked.connect(NGHIEMHPT.NGHIEM_HPT)
    ui.pptichphan.clicked.connect(TICHPHAN.PP_tichphan)
    ui.ppdaoham.clicked.connect(DAOHAM.PP_daoham)
    ui.hdsd.clicked.connect(HDSD._hdsd)
    ui.exit.clicked.connect(EXIT.Exit)
    ui.Other.clicked.connect(OTHER.pp1)

    MainWindow.show()
 

#Hàm xử lí dữ liệu  
class Xulidata(object):
    def Xuli(a):
        a
        y = Symbol("y")
        b = "y+" + a
        f = sympify(b)
        def ft(f):
            pt = lambdify(y, f)
            return pt(0)
        return ft(f)    


#Updatingg
class OTHER(object):
    def pp1(self):
        print("")



#Class giải nghiệm của phương trình
class NGHIEMPT(object):
    def PP_NGHIEMPT(self):
        global ui
        ui = menunghiempt.Ui_menunoghiempt()
        ui.setupUi(MainWindow)
        
        #Click
        ui.ppchiadoi.clicked.connect(NGHIEMPT.PP_CHIADOI)
        ui.pplap.clicked.connect(NGHIEMPT.PP_LAP)
        ui.pptieptuyen.clicked.connect(NGHIEMPT.PP_TIEPTUYEN)
        ui.ppdaycung.clicked.connect(NGHIEMPT.PP_DAYCUNG)
        ui.back.clicked.connect(mainUi)
        
        MainWindow.show()
   
    
    def PP_CHIADOI(self):
        global ui
        ui = calcchiadoi.Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NGHIEMPT.PP_NGHIEMPT)
        ui.tinh.clicked.connect(NGHIEMPT.calc_chiadoi)
        
        MainWindow.show()
        
    def calc_chiadoi(self):
        
        #Function
        x = symbols('x')
        def Input():
            func = ui.imputhamso.toPlainText()
            if func == "":
                return None
            F = sympify(func)
            return F
        
        def INPUT():
            global F
            F = Input()
            
        def f(x1):
            pt = lambdify(x,F)
            return pt(x1)
        
        def BisectionMethod_Count(a,b,e):
            global dem_0
            e = e + 1
            while e:
                dem_0 = (a+b)/2
                if f(dem_0)*f(a) > 0:
                    a = dem_0
                else:
                    b = dem_0
                e = e - 1
            return dem_0
        
        
        def BisectionMethod(a, b, e):
            count_chia = 0
            global dem_1
            while abs(b - a) > e:
                if count_chia >= 25:
                    return None
                count_chia = count_chia + 1
                dem_1 = (a + b) / 2
                if f(dem_1) * f(a) > 0:
                    a = dem_1
                else:
                    b = dem_1
            return dem_1
            
        #Xử lí đầu vào
        INPUT()
        a = ui.canduoi.toPlainText()
        b = ui.cantren.toPlainText()
        ep = ui.valuebombobox.toPlainText()
        
        #Xác thực đầu vào
        if F == None or a == "" or b == "" or ep == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            #Chuyển đổi dữ liệu
            a = Xulidata.Xuli(a)
            b = Xulidata.Xuli(b)
            
            #Xử lí đầu ra
            if ui.comboBox.currentText() == "Nhập giá trị sai số":
                ep = float(ep)
                y_ = BisectionMethod(a,b,ep)
                if y_ == None:
                    messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Không thể tìm thấy nghiệm")
                y_ = str(y_)
                ui.output.setText(y_) 
            else:
                ep = int(ep)
                if ep >= 25:
                    ui.output.setText("ERROR")
                    messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Số lần lặp vượt quá cho phép của admin")
                else:
                    y_ = BisectionMethod_Count(a,b,ep)
                    if y_ == None:
                        messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Không thể tìm thấy nghiệm")
                    y_ = str(y_)
                    ui.output.setText(y_) 
                
        
    def PP_LAP(self):
        global ui
        ui = calclap.Ui_calclappp()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NGHIEMPT.PP_NGHIEMPT)
        ui.tinh.clicked.connect(NGHIEMPT.calc_lap)
        
        MainWindow.show()
        
    def calc_lap(self):
        
        #Function
        x = symbols('x')
        def Input():
            func = ui.imputhamso.toPlainText()
            if func == "":
                return None
            F = sympify(func)
            return F
        
        def INPUT():
            global F
            F = Input()
            
        def f(x1):
            x = symbols("x")
            pt = lambdify(x,F)
            return pt(x1)


        def IterationMethod(x0,e):
            bodem = 0
            x_0 = x0
            y = f(x_0)
            while abs(x_0-y) >= e:
                x_0 = y
                y = f(x_0)
                if x_0 == y:
                    return None
                bodem = bodem + 1
                if bodem == 25:
                    return None
            return y
        
        def IterationMethod_count(x0,n):
            x_0 = x0
            n = n - 1
            y = f(x_0)
            while n:
                x_0 = y
                y = f(x_0)
                n = n - 1
            return y
            
        #Xử lí đầu vào
        INPUT()
        a = ui.giatrilap.toPlainText()
        ep = ui.valuebombobox.toPlainText()
        
        #Xác thực đầu vàonb 
        if a == "" or ep == "" or F == None:
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            #Chuyển đổi dữ liệu
            a = Xulidata.Xuli(a)
            
            #Xử lí đầu ra
            if ui.comboBox.currentText() == "Nhập giá trị sai số":
                ep = float(ep)
                y_ = IterationMethod(a,ep)
                if y_ == None:
                    messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Không thể tìm thấy nghiệm")
                y_ = str(y_)
                ui.output.setText(y_)
            else:
                ep = int(ep)
                if ep >= 25:
                    ui.output.setText("ERROR")
                    messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Số lần lặp vượt quá cho phép của admin")
                else:    
                    y_ = IterationMethod_count(a,ep)
                    if y_ == None:
                        messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Không thể tìm thấy nghiệm")
                    y_ = str(y_)
                    ui.output.setText(y_)
   
            
    def PP_TIEPTUYEN():
        global ui
        ui =calctieptuyen.Ui_calctuieptuyenn()
        ui.setupUi(MainWindow)
            
        #Click
        ui.back.clicked.connect(NGHIEMPT.PP_NGHIEMPT)
        ui.tinh.clicked.connect(NGHIEMPT.calc_tieptuyen)
            
        MainWindow.show()
            
    def calc_tieptuyen(self):
        
        #Funtion
        x = symbols('x')
        def Input():
            func = ui.imputhamso.toPlainText()
            if func == "":
                return None
            F = sympify(func)
            return F

        def INPUT():
            global F
            F = Input()
            
        def f(x1):
            pt = lambdify(x,F)
            return pt(x1)
        
        def Tangent_Method(a, b, e):
            bodem = 0
            global x_0
            if f(a) > 0:
                f_u = a
            else:
                f_u = b
            x_0 = f_u - f(f_u) * e / (f(f_u+e) - f(f_u))
            while abs(x_0-f_u) > e:
                if bodem == 25:
                    return None
                bodem = bodem + 1
                f_u = x_0
                x_0 = f_u - f(f_u) * e / (f(f_u + e) - f(f_u))
            return x_0
                
        #Xử lí đầu vào
        INPUT()
        a = ui.canduoi.toPlainText()
        b = ui.cantren.toPlainText()
        ep = ui.valuebombobox_2.toPlainText()
        
        #Xác thực đầu vào
        if F == None or a == "" or b == "" or ep == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            #Chuyển đổi dữ liệu
            a = Xulidata.Xuli(a)
            b = Xulidata.Xuli(b)
            ep = float(ep)
                
            #Xử lí đầu ra
            y_ = Tangent_Method(a, b, ep)
            if y_ == None:
                messagebox.showwarning("Hoàng Mạnh Khiêm VipPro","Không thể tìm thấy nghiệm")
            y_ = str(y_)
            ui.output.setText(y_)   
   
    
    def PP_DAYCUNG():
        global ui
        ui = calcdaycung.Ui_calcdaycungg()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NGHIEMPT.PP_NGHIEMPT)
        ui.tinh.clicked.connect(NGHIEMPT.calc_daycung)
        
    def calc_daycung():
        
        #Function
        x = symbols('x')
        def Input():
            func = ui.imputhamso.toPlainText()
            if func == "":
                return None
            F = sympify(func)
            return F
        
        def INPUT():
            global F
            F = Input()
            
        def f(x1):
            pt = lambdify(x,F)
            return pt(x1)


        def Bowstring_Method(a,b,e):
            dem_cung = 0
            f_a = f(a)
            f_b = f(b)
            dx = f_a*(b-a)/(f_a-f_b)
            x_0 = 0
            while abs(dx) > e:
                if dem_cung >= 25:
                    return None
                dem_cung = dem_cung + 1
                x_0 = a + dx
                f_a = f(x_0)
                if f_a * f_b <= 0:
                    a = x_0
                else:
                    b = x_0
                    f_a = f(a)
                    f_b = f(b)
                    dx = f_a*(b-a)/(f_a-f_b)
            return x_0
            
        #Xử lí đầu vào
        INPUT()
        a = ui.canduoi.toPlainText()
        b = ui.cantren.toPlainText()
        ep = ui.valuebombobox.toPlainText()
        
        #Xác thực đầu vào
        if F == None or a == "" or b == "" or ep == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            #Chuyển đổi dữ liệu
            a = Xulidata.Xuli(a)
            b = Xulidata.Xuli(b)
            ep = float(ep)
            
            #Xử lí đầu ra
            y_ = Bowstring_Method(a, b, ep)
            if y_ == None:
                messagebox.showwarning("Hoàng Mạnh Khiêm VipPro", "Không thể tìm thấy nghiệm")
            y_ = str(y_)
            ui.output.setText(y_)    
   
   
#Class giải đa thức nội suy    
class NOISUY(object):
    def PP_noisuy(self):
        global ui
        ui = homenoisuy.Ui_menunoisuy_2()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(mainUi)
        ui.pplagrange.clicked.connect(NOISUY.pplagrange)
        ui.ppnewton.clicked.connect(NOISUY.ppnewton)
        ui.ppnewtoncachdeu.clicked.connect(NOISUY.ppnewtoncachdeu)

    
        MainWindow.show()

    #Phương pháp Lagrange
    def pplagrange(self):
        global ui
        ui = lagrange.Ui_calclagra()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NOISUY.PP_noisuy)
        ui.tinh.clicked.connect(NOISUY.calc_lagrange)
           
    def calc_lagrange(self):
        
        #Function
        def hoocnerNhan(x):
            a = [1, -x[0]]
            for i in range(1, len(x)):
                a.append(0)
                temp = a.copy()
                for j in range(1, len(a)):
                    a[j] = temp[j] - temp[j - 1] * x[i]
                a[0] = 1
            return a

        def hoocnerChia(a, value):
            b = [a[0]]
            for i in range(1, len(a)):
                b.append(a[i] + b[i - 1] * value)
            return b

        def noiSuyLagrange(x, y):
            a = np.zeros(len(x))
            phi = hoocnerNhan(x)
            for i in range(len(x)):
                omega = hoocnerChia(phi, x[i])
                omega.pop()
                k = y[i] / hoocnerChia(omega, x[i]).pop()
                for j in range(len(a)):
                    a[j] += k * omega[j]
            return a.tolist()
        
        #Xử lí đầu vào
        x = ui.mocnoisuy.toPlainText()
        y = ui.giatrimocnoisuy.toPlainText()
        x0 = ui.giatrinoisuy.toPlainText()
        
        #Xác thực đầu vào
        if x == "" or y == "" or x0 == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            
            #Chuyển đổi dữ liệu
            x = x.split()
            x = list(map(float, x))
            y = y.split()
            y = list(map(float, y))
            x0 = float(x0)
            
            if len(x) != len(y):
                ui.output.setText("ERROR!")
                messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Số lương mốc nội suy và giá trị mốc không bằng nhau")
            else:
                #Xử lí đầu ra
                a = noiSuyLagrange(x, y)
                y_ = hoocnerChia(a, x0).pop()
                y_ = str(y_)
                ui.output.setText(y_)

    #Phương pháp Newton cách đều
    def ppnewtoncachdeu(self):
        global ui
        ui = newtoncachdeu.Ui_calcnewtoncachdeu()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NOISUY.PP_noisuy)
        ui.tinh.clicked.connect(NOISUY.calc_newtoncachdeu)
        
    def calc_newtoncachdeu(self):
        
        #Function
        def hoocnerChia(a, value):
            b = [a[0]]
            for i in range(1, len(a)):
                b.append(a[i] + b[i - 1] * value)
            return b


        def hoocnerNhanBoSung(coeffTich, t):
            if len(coeffTich) == 0:
                coeffTich.append(1)
                coeffTich.append(-t)
            else:
                coeffTich.append(0)
                temp = coeffTich.copy()
                for i in range(1, len(coeffTich)):
                    coeffTich[i] = coeffTich[i] - t * temp[i - 1]
            return coeffTich


        # Nội suy Newton tiến
        def saiPhanTien(delta, yk):
            temp = delta.copy()
            delta.append(0)
            delta[0] = yk
            for i in range(1, len(delta)):
                delta[i] = delta[i - 1] - temp[i - 1]
            return delta


        def ns_NewtonTien(x, y):
            a = [y[0]]
            delta = [y[0]]
            coeffTich = []
            giaiThua_k = 1
            for i in range(1, len(x)):
                delta = saiPhanTien(delta, y[i])
                coeffTich = hoocnerNhanBoSung(coeffTich, i - 1)
                giaiThua_k *= i
                c = delta[len(delta) - 1] / giaiThua_k
                a_1 = a.copy()
                a.append(0)
                for j in range(1, len(a)):
                    a[j] = a_1[j - 1] + c * coeffTich[j]
                a[0] = c
            return a
        
        #Xử lí đầu vào
        x = ui.mocnoisuy_2.toPlainText()
        y = ui.mocnoisuy_3.toPlainText()
        x0 = ui.mocnoisuy_4.toPlainText()
        
        
        #Xác thực đầu vào
        if x == "" or y == "" or x0 == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            
            #Chuyển đổi dữ liệu
            x = x.split()
            x = list(map(float, x))
            y = y.split()
            y = list(map(float, y))
            x0 = float(x0)
            if len(x) != len(y):
                ui.output.setText("ERROR!")
                messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Số lương mốc nội suy và giá trị mốc không bằng nhau")
            else:
                ktkc = x[1]-x[0]
                x_kt = x[0]
                check = 0
                for i in range(1,len(x),1):
                    if x[i] == x[i-1]+ktkc:
                        continue
                    else:
                        check = 1
                if check == 1:
                    ui.output.setText("ERROR!")
                    messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Không xử lí được hãy dùng PP NewTon tổng quát")
                else:
                    a = ns_NewtonTien(x, y)
                    h = x[1] - x[0]
                    t = (x0 - x[0]) / h
                    y_ = hoocnerChia(a, t).pop()
                
                    #Xử lí đầu ra
                    y_ = str(y_)
                    ui.output.setText(y_)
        
                    
    # Phương pháp Newton tổng quát  
    def ppnewton(self):
        global ui
        ui = newton.Ui_calcnedwton()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NOISUY.PP_noisuy)
        ui.tinh.clicked.connect(NOISUY.calc_newton)
        
    def calc_newton(self):
        
        #Function
        # kết nạp mốc x[i] vào Bảng tỷ hiệu
        def BuildBTH(BTH, x, y, i):
            TH_row_i = np.zeros(len(x))
            TH_row_i[0] = y[i]
            for j in range(1, i + 1):
                TH_row_i[j] = (TH_row_i[j - 1] - BTH[j - 1]) / (x[i] - x[i - j])
            return TH_row_i

        # kết nạp mốc x[i] vào Bảng tính tích
        def BuildBTT(BTT, x, i):
            TT_row_i = np.zeros(len(x))
            TT_row_i[i + 1] = 1  # sử dụng lược đồ Hoocne
            for j in range(i, 0, -1):
                TT_row_i[j] = BTT[j - 1] - x[i] * BTT[j]
            TT_row_i[0] = -x[i] * BTT[0]
            return TT_row_i

        # kết nạp mốc x[i] vào đa thức
        def fx(BTH, BTT, i, f):
            for j in range(0, i + 1):
                f[j] += BTH[i] * BTT[j]
            return f

        # Xây dựng đa thức nội suy Newton tiến
        def Newton_interpolation_Forward(BTH, BTT, f, x, y, n):
            for i in range(1, n + 1):
                BTH = BuildBTH(BTH, x, y, i)
                BTT = BuildBTT(BTT, x, i - 1)
                f = fx(BTH, BTT, i, f)
            return f, BTH, BTT

        # ước tính f(x0)
        def fx0(f, n, x0):
            value = f[n]
            for i in range(n - 1, -1, -1):  # sử dụng lược đồ Hoocne
                value = value * x0 + f[i]
            return value
        
        
        def _Newton(x):
            n = len(x) - 1
            BTH, BTT, f = np.zeros(n + 1), np.zeros(n + 1), np.zeros(n + 1)
            BTH[0], BTT[0], f[0] = y[0], 1, y[0]
            f, BTH, BTT = Newton_interpolation_Forward(BTH, BTT, f, x, y, n)
            y_ = fx0(f, n, x0)
            return y_
        
        #Xử lí đầu vào
        x = ui.mocnoisuy.toPlainText()
        y = ui.giatrimocnoisuy.toPlainText()
        x0 = ui.diemnoisuy.toPlainText()
        
        #Xác thực đầu vào
        if x == "" or y == "" or x0 == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            
            #Chuyển đổi dữ liệu
            x = x.split()
            x = list(map(float, x))
            y = y.split()
            y = list(map(float, y))
            x0 = float(x0)
            
            
            if len(x) != len(y):
                ui.output.setText("ERROR!")
                messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Số lương mốc nội suy và giá trị mốc không bằng nhau")
            else:
                #Xử lí dữ liệu đầu ra
                y_ = _Newton(x)
                y_ = str(y_)
                
                ui.output.setText(y_)
 
 
#Class giải tích phân                                 
class TICHPHAN(object):
    def PP_tichphan(self):
        global ui
        ui = menutichphan.Ui_menunoisuy_2()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(mainUi)        
        ui.pphinhthang.clicked.connect(TICHPHAN.Hinhthang)
        ui.ppsimpson.clicked.connect(TICHPHAN.Simpson)
        
        MainWindow.show()
        
    def Hinhthang(self):
        global ui
        ui = calchinhthang.Ui_calchinhthang()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(TICHPHAN.PP_tichphan)
        ui.tinh.clicked.connect(TICHPHAN.calc_hinhthang)
        
    def calc_hinhthang(self):
        
        #Function
        x = symbols('x')
        def Input():
            func = ui.imputhamso.toPlainText()
            if func == "":
                return None
            F = sympify(func)
            return F
        
        def INPUT():
            global F
            F = Input()
            
        def f(x1):
                pt = lambdify(x,F)
                return pt(x1)
            
        X1 = []
        Y1 = []
        def TTPHinhThang(a,b,n):
            ans = 0
            h = (b-a)/n
            for i in range (n+1):
                X1.append(a + i * h)
                Y1.append(f(a + i * h))
            for i in range(n+1):
                if i == 0 or i == n:
                    ans += Y1[i]
                else:
                    ans += 2 * Y1[i]
            return h / 2 * ans
        
            
        #Xử lí đầu vào
        INPUT()
        a = ui.canduoi.toPlainText()
        b = ui.cantren.toPlainText()
        ep = ui.value_n.toPlainText()
        
        #Xác thực dữ liệu
        if a == "" or b == "" or F == None or ep == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            
            #Chuyển đổi dữ liệu
            a = Xulidata.Xuli(a)
            b = Xulidata.Xuli(b)
            ep = ui.value_n.toPlainText()
            ep = int(ep)
            
            
            #Xử lí đầu ra
            ans = TTPHinhThang(a, b, ep)
            ans = str(ans)
            ui.output.setText(ans)
        
    def Simpson(self):
        global ui
        ui = calcsimpson.Ui_calcsimpson()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(TICHPHAN.PP_tichphan)
        ui.tinh.clicked.connect(TICHPHAN.calc_simpson)
        
    def calc_simpson(self):
        
        #Fuction
        x = symbols('x')
        def Input():
            func = ui.imputhamso.toPlainText()
            if func == "":
                return None
            F = sympify(func)
            return F
        
        def INPUT():
            global F
            F = Input()
            
        X2 = []
        Y2 = []
        
        def f(x1):
            pt = lambdify(x,F)
            return pt(x1)
        
        def TTPSimpson(a,b,m):
            ans = 0
            h = (b - a) / m
            for i in range (m+1):
                X2.append(a+ i * h)
                Y2.append(f(a + i * h))
            for i in range(m+1):
                if i == 0 or i == m:
                    ans += Y2[i]
                elif i % 2 == 1:
                    ans += 4 * Y2[i]
                else:
                    ans += 2 * Y2[i]
            return h / 3 * ans
            
        #Xử lí đầu vào
        INPUT()
        a = ui.canduoi.toPlainText()
        b = ui.cantren.toPlainText()
        ep = ui.value_n.toPlainText()
        
        #Xác thực dữ liệu
        if a == "" or b == "" or F == None or ep == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            
            #Chuyển đổi dữ liệu
            a = Xulidata.Xuli(a)
            b = Xulidata.Xuli(b)
            ep = int(ep)
            
            #Xử lí đầu ra
            ans = TTPSimpson(a, b, ep)
            ans = str(ans)
            ui.output.setText(ans)
      
      
#Class giải đạo hàm      
class DAOHAM(object):
    def PP_daoham(self):
        global ui
        ui = menudaoham.Ui_homedaoham()
        ui.setupUi(MainWindow)  
        
        #Click
        ui.back.clicked.connect(mainUi)
        ui.ppdaoham.clicked.connect(DAOHAM.daoham)
        
        
        MainWindow.show()
        
    def daoham(self):
        global ui
        ui = calcdaoham.Ui_calcdaoham()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(DAOHAM.PP_daoham)
        ui.tinh.clicked.connect(DAOHAM.calc)
        
    def calc(self):
        
        #Function
        def multiply_horner(A, i) -> list:
            """ Nhân một đa thức với (t-i) """ 
            A.append(0)
            for j in range(len(A)-1,0,-1):
                A[j] = A[j] - A[j - 1] * i
            return A

        def devide_horner(A, i, X) -> list:
            """ Chia một đa thức với (t-i) """
            for j in range(1, len(X)):
                X[j] = i*X[j-1] + A[j]
            return X

        def P_t(A, X) -> list:
            """ Tính P(t) """
            Pt = [0]*(n+1)
            for i in range(n+1):
                D = devide_horner(A, i, X)
                for j in range(n+1):
                    Pt[j] = Pt[j] + D[j]*((-1)**(n-i))/(factorial(i)*factorial(n-i))*y[i]
            return Pt

        def deri_approx(Pt):
            """ Tính gần đúng đạo hàm cấp 1 """
            ans = 0
            for i in range(n):
                ans = ans + (1/h)*Pt[i]*(n-i)*(t**(n-i-1))
            return ans
        
        #Xử lí đầu vào
        x = ui.mocnoisuy.toPlainText()
        y = ui.giatrimocnoisuy.toPlainText()
        x0 = ui.giatrinoisuy.toPlainText()
        
        #Xác thực dữ liệu
        if x == "" or y == "" or x0 == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Nhập thiếu dữ liệu đầu vào")
        else:
            
            #Chuyển đổi dữ liệu
            x = x.split()
            x = list(map(float, x))
            y = y.split()
            y = list(map(float, y))
            x0 = float(x0)
            
            if len(x) != len(y):
                ui.output.setText("ERROR!")
                messagebox.showerror("Hoàng Mạnh Khiêm VipPro", "Số lương mốc nội suy và giá trị mốc không bằng nhau")
            else:
                n = len(x)-1
                h = (x[n]-x[0])/n
                t = (x0 - x[0])/h
                A = [1]
                for i in range(0, n + 1):
                    A = multiply_horner(A, i)  # Mảng chứa tích các (t-i)
                X = [1] * (n + 1)  # Tạo mảng lưu giá trị phép chia A cho (t-i)
                
                #Xử lí đầu ra
                Pt = P_t(A, X)
                y_ = deri_approx(Pt)
                y_ = str(y_)
                ui.output.setText(y_) 


#Class giải nghiệm của hệ phương trình
class NGHIEMHPT(object):
    def NGHIEM_HPT(self):
        global ui
        ui = menunghiemhpt.Ui_menunoisuy_2()
        ui.setupUi(MainWindow)
        
        #Click
        ui.ppgauass.clicked.connect(NGHIEMHPT.PP_gauss)
        ui.ppjacobi.clicked.connect(NGHIEMHPT.PP_jacobi)
        ui.ppgauass_khu.clicked.connect(NGHIEMHPT.PP_gauss_khu)
        ui.back.clicked.connect(mainUi)

    def PP_gauss_khu(self):
        global ui
        ui = calcgausskhu.Ui_calcgauss()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NGHIEMHPT.NGHIEM_HPT)
        ui.tinh.clicked.connect(NGHIEMHPT.calckhugauss)

    def calckhugauss(self):
        f1 = ui.giatriheso.toPlainText()
        if f1 == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")
        else:
            data = f1.splitlines()
            A = []
            b = []
            countA = 0
            for s in data:
                    row = s.strip().split(' ')
                    row1 = [float(i) for i in row]
                    row2 = []
                    for i in range(len(row1)-1):
                        countA = countA + 1
                        row2.append(row1[i])
                    A.append(row2)
                    b.append(row1[len(row1)-1])
            if(len(b)==countA/len(A)):
                def gaussian_elimination(A, b):
                    n = len(A)

                    # Hợp nhất ma trận A và vector b
                    Ab = []
                    for i in range(n):
                        Ab.append(A[i] + [b[i]])

                    # Quá trình khử Gauss
                    for i in range(n):
                        # Tìm phần tử chính không bằng 0 trong cột i
                        max_row = i
                        for j in range(i + 1, n):
                            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                                max_row = j

                        # Đưa dòng có phần tử chính không bằng 0 lên đầu
                        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

                        # Kiểm tra phương trình vô nghiệm
                        if abs(Ab[i][i]) < 1e-15:
                            if abs(Ab[i][n]) < 1e-15:
                                return "Phương trình có vô số nghiệm"
                            else:
                                return "Phương trình vô nghiệm"

                        # Loại bỏ phần tử chính khỏi các dòng dưới đó
                        for j in range(i + 1, n):
                            ratio = Ab[j][i] / Ab[i][i]
                            for k in range(i, n + 1):
                                Ab[j][k] -= ratio * Ab[i][k]

                    # Truy ngược để tìm nghiệm
                    x = [0] * n
                    for i in range(n - 1, -1, -1):
                        x[i] = Ab[i][n] / Ab[i][i]
                        for j in range(i - 1, -1, -1):
                            Ab[j][n] -= Ab[j][i] * x[i]

                    return x
                
                x = gaussian_elimination(A,b)
                x = str(x)
                ui.output.setText(x)
            else:
                ui.output.setText("ERROR!")
                messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")


    
    def PP_jacobi(self):
        global ui
        ui = calcjacobi.Ui_calcgauss()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NGHIEMHPT.NGHIEM_HPT)
        ui.tinh.clicked.connect(NGHIEMHPT.calc_jacobi)   
            
        MainWindow.show()
    
    def calc_jacobi(self):
        # Gói A
        # kiểm tra điều kiện chéo trội của A
        def kt(A,n):
            m = []
            m = [sum(abs(j) for j in r) for r in A]
            if all(2 * abs(A[i][i]) > m[i] for i in range(n)):
                return 0
            else:
                m = [sum([abs(x[i]) for x in A]) for i in range(len(A[0]))]
                if all(2 * abs(A[j][j]) > m[j] for j in range(n)):
                    return 1
                else:
                    return -1


        # chuẩn vc của ma trận
        def chuanvc(a):
            a1 = []
            for r in a:
                m = (sum(abs(i) for i in r))
                a1.append(m)
            c = max(i for i in a1)
            return c


        # chuẩn 1 của ma trận
        def chuan1(a):
            a1 = [sum([abs(x[i]) for x in a]) for i in range(len(a[0]))]
            m = max(abs(i) for i in a1)
            return m


        # xác định loại chuẩn ma trận
        def chuan(a,n,A):
            if kt(A,n) == 0:
                return chuanvc(a)
            else:
                if kt(A,n) == 1:
                    return chuan1(a)
                else:
                    print("error!")


        #xác định loại chuẩn vecto
        def chuan_vecto(v,A):
            if kt(A,len(A)) == 0:
                return sum(abs(i) for i in v)
            if kt(A,len(A)) == 1:
                return max(abs(i) for i in v)
            if kt(A,len(A)) == -1:
                print("error!")


        # Hiệu hai vecto
        def sub(x, y):
            m = []
            for i in range(len(x)-2):
                m.append((x[i] - y[i]))
            return m


        # Gói C:
        # xác định ma trận B và vecto tự do
        B = []
        d = []


        def xacdinh_b(A,n):
            for i in range(n):
                B.append([])
                for j in range(n):
                    if i == j:
                        B[i].append(0)
                    else:
                        B[i].append(-(A[i][j]) / (A[i][i]))


        def xacdinh_d(A,n):
            for i in range(n):
                d.append(b[i] / A[i][i])


        # lặp đơn
        def lap_don(B, d, e):
            x0 = d

            # xây dựng hàm phi(x)
            def phi(B, x, d):
                m = []
                y = []
                for r in B:
                    p = sum(x[i] * r[i] for i in range(n))
                    m.append(p)
                for i in range(n):
                    y.append(m[i] + d[i])
                return y

            xk = phi(B, x0, d)
            for i in range(e):
                x0 = xk
                xk = phi(B, x0, d)
            return xk

        #Xây dựng hàm cho tính đến khi hợp lí
        def lap_don_ss(A,B, d, e):
            x0 = d

            # xây dựng hàm phi(x)
            def phi(B, x, d):
                m = []
                y = []
                for r in B:
                    p = sum(x[i] * r[i] for i in range(n))
                    m.append(p)
                for i in range(n):
                    y.append(m[i] + d[i])
                return y

            xk = phi(B, x0, d)
            dem = 0
            while chuan_vecto(sub(x0, xk),A) > e:
                x0 = xk
                xk = phi(B, x0, d)
                dem = dem + 1
            return xk,dem

        def chuanvect(a):
            return max(abs(i) for i in a)

        def chuanvec1(a):
            return sum(abs(i) for i in a)
        
        # main
        # Bước 1: Kiểm tra A
        f1 = ui.giatriheso.toPlainText()
        x = ui.giatritinhgauss.toPlainText()
        N = ui.lanlap.toPlainText()
        if f1 == "" or N == "" or x == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")
        else:
            data = f1.splitlines()
            x = x.split()
            x = list(map(float,x))
            n = sum(1 for _ in data)
            A = []
            b = []
            countA = 0
            for s in data:
                row = s.strip().split(' ')
                row1 = [float(i) for i in row]
                row2 = []
                for i in range(len(row1)-1):
                    countA = countA + 1
                    row2.append(row1[i])
                A.append(row2)
                b.append(row1[len(row1)-1])
            if(len(b)==countA/len(A) and len(x)==len(b) or x == "None"):
                if kt(A,len(A)) == -1:
                    ui.output.setText("None")
                    messagebox.showwarning("HoangManhKhiem VipPro","Ma trận A không phải ma trận chéo trội.")
                else:
                    if ui.comboBox.currentText() == "Tiên nghiệm":
                        N = int(N)
                        xacdinh_d(A,n)
                        xacdinh_b(A,n)
                        q = chuan(B,n,A)
                        #Tiên nghiệm
                        x1 = lap_don(B,d,1)
                        x1 = np.array(x1)
                        x= np.array(x)
                        X = chuanvect(x1-x)
                        epp = q**3*X/(1-q)
                        epp =str(epp)
                        Y = lap_don(B,d,N)
                        Y = str(Y)
                        OUT = "Nghiệm của hệ: " + Y + "\n" + "Sai số tiên nghiệm: " + epp
                        ui.output.setText(OUT)
                    elif ui.comboBox.currentText() == "Hậu nghiệm":
                        N = int(N)
                        xacdinh_d(A,n)
                        xacdinh_b(A,n)
                        q = chuan(B,n,A)
                        #Hậu nghiệm
                        print(q)
                        x1 = lap_don(B, d, N)
                        x2 = lap_don(B, d, N-1)
                        x1 = np.array(x1)
                        x2 = np.array(x2)
                        x3 = x1 - x2
                        x3 = chuanvec1(x3)
                        Y = lap_don(B, d, N)
                        Y = str(Y)
                        epp = q*x3 / (1 - q)
                        epp =str(epp)
                        OUT = "Nghiệm của hệ: " + Y + "\n" + "Sai số hậu nghiệm: " + epp
                        ui.output.setText(OUT)
                    else:
                            N = float(N)
                            if kt(A,len(A)) == 0:
                                out1 = "A là ma trận chéo trội hàng"
                                xacdinh_d(A,n)
                                xacdinh_b(A,n)
                                eps = N*(1-chuan(B,n,A))/(chuan(B,n,A))
                                qq = chuan(B,n,A)
                                qq = str(qq)
                                out2 = "chuan1 = " + qq
                            if kt(A,len(A)) == 1:
                                out1 = "A là ma trận chéo trội cột"
                                xacdinh_d(A,n)
                                xacdinh_b(A,n)
                                chuanT = max(abs(1 / A[i][i]) for i in range(n))
                                chuanD = max(abs(A[i][i]) for i in range(n))
                                chuan_B1 = max([sum([abs(x[j] / A[j][j]) for x in A]) for j in range(n)]) - 1
                                qq =chuan_B1
                                qq = str(qq)
                                out2 = "chuanvc = " + qq
                            nghiem = lap_don_ss(A,B, d, eps)
                            xkk = nghiem[0]
                            sbl = nghiem[1]
                            xkk = str(xkk)
                            sbl = str(sbl)
                            xxxxx = out1 + "\n" + out2 + "\n" + "Nghiệm của hệ:" + xkk + "\n" + "Số lần lặp: " + sbl
                            ui.output.setText(xxxxx)
                        
            else:
                ui.output.setText("ERROR!")
                messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")


    
    def PP_gauss(self):
        global ui
        ui = calcgauss.Ui_calcgauss()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(NGHIEMHPT.NGHIEM_HPT)
        ui.tinh.clicked.connect(NGHIEMHPT.calc_gauss)
        
        MainWindow.show()
    
    def calc_gauss(self):
        
        #Function
        def kt(A,n):
            m = []
            m = [sum(abs(j) for j in r) for r in A]
            if all(2 * abs(A[i][i]) > m[i] for i in range(n)):
                return 0
            else:
                m = [sum([abs(x[i]) for x in A]) for i in range(len(A[0]))]
                if all(2 * abs(A[j][j]) > m[j] for j in range(n)):
                    return 1
                else:
                    return -1

        def chuanvc(a):
            a1 = []
            for r in a:
                m = (sum(abs(i) for i in r))
                a1.append(m)
            c = max(i for i in a1)
            return c

        #xác định loại chuẩn vecto
        def chuan_vecto(v,A):
            if kt(A,len(A)) == 0:
                return sum(abs(i) for i in v)
            if kt(A,len(A)) == 1:
                return max(abs(i) for i in v)
            if kt(A,len(A)) == -1:
                print("error!")

        # chuẩn 1 của ma trận
        def chuan1(a):
            a1 = [sum([abs(x[i]) for x in a]) for i in range(len(a[0]))]
            m = max(abs(i) for i in a1)
            return m

        def chuanvect(a):
            return max(abs(i) for i in a)

        def gauss(A, b, x, n):
            L = np.tril(A)
            U = A - L
            for i in range(n):
                x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
            return x
        
        def gauss_ss(A, b, x, N):
            n = len(A)
            x = np.zeros(n)
            max_iterations = 100
            dem = 0
            for _ in range(max_iterations):
                x_new = np.zeros(n)
                dem = dem +1
                for i in range(n):
                    sum_val = 0
                    for j in range(n):
                        if j != i:
                            sum_val += A[i][j] * x[j]
                    x_new[i] = (b[i] - sum_val) / A[i][i]

                if np.linalg.norm(x - x_new) < N:
                    return x_new,dem

                x = x_new

            return "Phương pháp không hội tụ trong số lần lặp lại tối đa.","False"

        def xacdinhT(A):
            L = np.tril(A)
            U = A - L
            U = U * (-1)
            T = np.linalg.inv(L) @ U
            return T


        #Xử lí đầu vào
        f1 = ui.giatriheso.toPlainText()
        x = ui.giatritinhgauss.toPlainText()
        N = ui.lanlap.toPlainText()
        if x == "" or f1 == "" or N == "":
            ui.output.setText("ERROR!")
            messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")
        else:
            if ui.comboBox.currentText() == "Sai số":
                data = f1.splitlines()
                x = x.split()
                x = list(map(float,x))
                N = float(N)
                n = sum(1 for _ in data)
                A = []
                b = []
                countA = 0
                for s in data:
                    row = s.strip().split(' ')
                    row1 = [float(i) for i in row]
                    row2 = []
                    for i in range(len(row1)-1):
                        countA = countA + 1
                        row2.append(row1[i])
                    A.append(row2)
                    b.append(row1[len(row1)-1])
                if(len(b)==countA/len(A) and len(x)==len(b)):
                    if kt(A,len(A)) == -1:
                        ui.output.setText("None")
                        messagebox.showwarning("HoangManhKhiem VipPro","Ma trận A không phải ma trận chéo trội.")
                    else:
                        y = gauss_ss(A,b,x,N)
                        if y == "Phương pháp không hội tụ trong số lần lặp lại tối đa.":
                            ui.output.setText("Phương pháp không hội tụ trong số lần lặp lại tối đa.")
                            messagebox.showerror("HoangManhKhiem VipPro","Phương pháp không hội tụ trong số lần lặp lại tối đa.")
                        else:
                            x1 = gauss(A, b, x, 1)
                            t = chuanvect(x1-x) 
                            T = xacdinhT(A)
                            q = chuanvc(T)
                            epp = q**3*t/(1-q)
                            epp = str(epp)
                            out = "Nghiệm của hệ: " + str(y[0]) + "\n" + "sai số tiên nghiệm sử dụng chuẩn vc: " + epp + "\n" + "số lần lặp: " + str(y[1])
                            ui.output.setText(out)
                else:
                    ui.output.setText("ERROR!")
                    messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")
                
            else:
                data = f1.splitlines()
                x = x.split()
                x = list(map(float,x))
                N = int(N)
                n = sum(1 for _ in data)
                A = []
                b = []
                countA = 0
                for s in data:
                    row = s.strip().split(' ')
                    row1 = [float(i) for i in row]
                    row2 = []
                    for i in range(len(row1)-1):
                        countA = countA + 1
                        row2.append(row1[i])
                    A.append(row2)
                    b.append(row1[len(row1)-1])
                if(len(b)==countA/len(A) and len(x)==len(b)):
                    if kt(A,len(A)) == -1:
                        ui.output.setText("None")
                        messagebox.showwarning("HoangManhKhiem VipPro","Ma trận A không phải ma trận chéo trội.")
                    else:
                        y = gauss(A,b,x,N)
                        y = str(y)
                        x1 = gauss(A, b, x, 1)
                        t = chuanvect(x1-x) 
                        T = xacdinhT(A)
                        q = chuanvc(T)
                        epp = q**3*t/(1-q)
                        epp = str(epp)
                        out = "Nghiệm của hệ: " + y + "\n" + "sai số tiên nghiệm sử dụng chuẩn vc: " + epp
                        ui.output.setText(out)
                else:
                    ui.output.setText("ERROR!")
                    messagebox.showerror("HoangManhKhiem VipPro","Nhập thiếu dữ liệu")
    
        
        
#Class thông tin của người sáng lập        
class ABOUT(object):
    def About():
        global ui
        ui = about.Ui_aboutMain()
        ui.setupUi(MainWindow)
        
        #Click
        ui.back.clicked.connect(mainUi)
        ui.fb.clicked.connect(ABOUT.facebook)
        ui.github.clicked.connect(ABOUT.github)
        
        
        MainWindow.show()
        
    def github(self):
        url = "https://github.com/hoangmanhkhiem"
        webbrowser.open_new_tab(url)
        
    def facebook(self):
        url = "https://www.facebook.com/hoangmanhkhiem.IT"
        webbrowser.open_new_tab(url)


#Class setup hướng dẫn sử dụng
class HDSD(object):
    def _hdsd(self):
        global ui
        ui = hdsd.Ui_HDSDMAIN()
        ui.setupUi(MainWindow)
        
        ui.back.clicked.connect(mainUi)
        
        MainWindow.show()


#Class dừng app
class EXIT(object):
    def Exit(self):
        messagebox.showinfo("HoangManhKhiem VipPro","Cảm ơn đã sử dụng phần mềm này :))")
        MainWindow.close()
        
         
Alert()
LOGIN()
sys.exit(app.exec_())