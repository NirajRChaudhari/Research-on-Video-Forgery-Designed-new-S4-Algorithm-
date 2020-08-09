from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import algorithm
import second_win
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.resize(838, 437)
        MainWindow.setMinimumSize(QtCore.QSize(838, 437))
        MainWindow.setMaximumSize(QtCore.QSize(838, 437))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet("border:0px;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upload_file = QtWidgets.QPushButton(self.groupBox_2)
        self.upload_file.setMinimumSize(QtCore.QSize(0, 42))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.upload_file.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.upload_file.setFont(font)
        self.upload_file.setAutoFillBackground(False)
        self.upload_file.setStyleSheet("color:#ff007f; ")
        self.upload_file.setObjectName("upload_file")
        self.horizontalLayout.addWidget(self.upload_file)
        self.display_filename = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_filename.sizePolicy().hasHeightForWidth())
        self.display_filename.setSizePolicy(sizePolicy)
        self.display_filename.setMinimumSize(QtCore.QSize(480, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.display_filename.setFont(font)
        self.display_filename.setStyleSheet("color:#ff007f; ")
        self.display_filename.setObjectName("display_filename")
        self.display_filename.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.display_filename)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        css = ''' QProgressBar
                {
                color: #ff007f;
                border-radius: 5px;
                text-align: center;
                }
                QProgressBar::chunk
                {
                background-color: #00aaff;
                width: 3.15px;
                margin: 0.5px;
                } '''
        self.progressBar.setStyleSheet(css)

        self.horizontalLayout_2.addWidget(self.progressBar)
        self.check_forgery = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_forgery.sizePolicy().hasHeightForWidth())
        self.check_forgery.setSizePolicy(sizePolicy)
        self.check_forgery.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.check_forgery.setFont(font)
        self.check_forgery.setStyleSheet("color:#00aaff; ")
        self.check_forgery.setObjectName("check_forgery")
        self.horizontalLayout_2.addWidget(self.check_forgery)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.check_forgery.setEnabled(False)
        self.display_filename.setEnabled(False)
        'Connect Signlas to Slots'
        self.upload_file.clicked.connect(self.action_upload_file)
        self.check_forgery.clicked.connect(self.action_check_forgery)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def action_check_forgery(self):
        self.check_forgery.setEnabled(False)
        self.check_forgery.setText("Processing .....")
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)

        self.Results= algorithm.main(self.fname[0],self)  #Main Function Call
        
        self.progressBar.setVisible(False)
        self.open_second_window()
        self.display_filename.setText("")
        self.check_forgery.setText("Check Forgery")

    def action_upload_file(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Select File for Forgery Checking',os.getcwd(),"Video files (*.avi *.mp4)")
        if(self.fname[0]==''):
            self.check_forgery.setEnabled(False)
            self.display_filename.setText("")
        else:
            self.display_filename.setText(os.path.basename(self.fname[0]))
            self.check_forgery.setEnabled(True)

    def open_second_window(self):
        self.second_ui=second_win.Ui_MainWindow()
        self.MainWindow2=QtWidgets.QMainWindow()
        self.second_ui.setupUi(self.MainWindow2,self.fname[0],self.Results)
        self.MainWindow2.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Copy-Move Forgery Detection System"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#ff007f;\">S4 Filters based</span><span style=\" font-size:24pt; font-weight:600; color:#ff00ff;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#00aaff;\">Copy-Move Forgery Detection System</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt; font-weight:600; color:#00aaff;\"><br /></p></body></html>"))
        self.upload_file.setText(_translate("MainWindow", "Upload File"))
        self.check_forgery.setText(_translate("MainWindow", "Check Forgery"))

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    first_ui=Ui_MainWindow()
    first_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 
