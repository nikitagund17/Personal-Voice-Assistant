
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import cv2
from mod_train import  model_train


# 2nd Page Registration and Module train

class Ui_MainWindow(object):

    


    def setupUi(self, MainWindow):



        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FronEnd_img/reg.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1586, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -68, 1581, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("FronEnd_img/reg.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(620, 90, 281, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 750, 161, 31))
        
        self.pushButton.clicked.connect(self.start)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 750, 161, 31))
        self.pushButton_2.clicked.connect(self.ss)
        self.pushButton_2.clicked.connect(MainWindow.close)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 750, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.call)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1157, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Enter your ID to register"))
        self.pushButton.setText(_translate("MainWindow", "Verify"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.pushButton_3.setText(_translate("MainWindow", "Train_modul"))
    def start(self):
        
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
        cam.set(3, 640) # set video FrameWidth
        cam.set(4, 480) # set video FrameHeight


        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #Haar Cascade classifier is an effective object detection approach

        face_id =self.lineEdit.text()
        #Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

        print("Taking samples, look at camera ....... ")
        count = 0 # Initializing sampling face count

        while True:

            ret, img = cam.read() #read the frames using the above created object
            converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another
            faces = detector.detectMultiScale(converted_image, 1.3, 5)

            for (x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #used to draw a rectangle on any image
                count += 1

                
                cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])
                # To capture & Save images into the datasets folder

                cv2.imshow('image', img) #Used to display an image in a window

            k = cv2.waitKey(100) & 0xff # Waits for a pressed key
            if k == 27: # Press 'ESC' to stop
                break
            elif count >= 20: # Take 50 sample (More sample --> More accuracy)
                break

        print("Samples taken now closing the program....")
        cam.release()
        cv2.destroyAllWindows()
    def call(self):
        
        model_train()

    def ss(self):
       
        self.window=QtWidgets.QMainWindow()
        self.ui=login()
        self.ui.setupUi(self.window)
        self.window.show()

# 3rd Login Window 

class login(object):
    
    def __init__(self):
        super().__init__()


    def setupUi(self, MainWindow):

        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FronEnd_img/login.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1586, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -68, 1581, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("FronEnd_img/deepLearning.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1040, 40, 471, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("FronEnd_img/face-scan-min22-unscreen.gif"))
        self.label_2.setObjectName("label_2")
        movie=QMovie('FronEnd_img/face-scan-min22-unscreen.gif') 
        self.label_2.setMovie(movie)
        movie.start()
        movie1=QMovie('FronEnd_img/deepLearning.webp')
        self.label.setMovie(movie1)
        movie1.start()
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1200, 370, 161, 61))

        self.pushButton_2.clicked.connect(self.call)
        self.pushButton_2.clicked.connect(MainWindow.close)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
    def sk(self):
        self.window2=QtWidgets.QMainWindow()
        self.ui=login()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def call(self):
        from Facerecognition import rec
        rec()


# 1st page Login ANd Register

class face_detect(object):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        Login_window.setObjectName("FronEnd_img/Login_window")
        Login_window.resize(1586, 860)
        self.centralwidget = QtWidgets.QWidget(Login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -68, 1581, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("FronEnd_img/deepLearning.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 80, 471, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("FronEnd_img/face-scan-min22-unscreen.gif"))
        self.label_2.setObjectName("label_2")
        movie=QMovie('FronEnd_img/face-scan-min22-unscreen.gif') 
        self.label_2.setMovie(movie)
        movie.start()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1200, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.openWindow)        
        self.pushButton.clicked.connect(Login_window.close)

        movie1=QMovie('FronEnd_img/deepLearning.webp')
        self.label.setMovie(movie1)
        movie1.start()

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1350, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.log_win)
        self.pushButton_2.clicked.connect(Login_window.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.pushButton_2.setText(_translate("MainWindow", "GoLogin"))

    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()  

    def log_win(self):
        
        self.window=QtWidgets.QMainWindow()
        self.ui=login()
        self.ui.setupUi(self.window)
        self.window.show()  
  
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_window = QtWidgets.QMainWindow()
    ui = face_detect()
    ui.setupUi(Login_window)
    Login_window.show()
    

    
    sys.exit(app.exec_())
    
