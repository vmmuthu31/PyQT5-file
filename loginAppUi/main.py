from PyQt5 import QtWidgets, QtCore
from loginUi import Ui_Form
import sys

class LoginApp(QtWidgets.QWidget, Ui_Form):
    def changeForm(self):
        if self.pushButton_7.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.pushButton_7.setText("<")
        else:
            self.widget_2.show()
            self.widget_3.hide()
            self.pushButton_7.setText(">")

    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.widget_3.hide()
        self.pushButton_7.clicked.connect(self.changeForm)

#connecting with the databases

def addNew():
    name=nameVar.get()
    email=emailVar.get()
    password=passVar.get()
    organiz=OrganizVar.get()
    encname=jwt.encode({"some": "payload"}, name, algorithm="HS256")
    encemail=jwt.encode({"some": "payload"}, email, algorithm="HS256")
    encpassword=jwt.encode({"some": "payload"}, password, algorithm="HS256")
    encorganiz=jwt.encode({"some": "payload"}, organiz, algorithm="HS256")
    conn = sqlite3.connect('Users.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS User (Name TEXT NOT NULL,Email TEXT PRIMARY KEY,Password Text NOT NULL,organiz TEXT NOT NULL)')
    count=cursor.execute('INSERT INTO User (Name,Email,Password,organiz) VALUES(?,?,?,?)',(encname,encemail,encpassword,encorganiz))
    if(cursor.rowcount>0):
        print ("Registration Successfully")
    else:
        print ("Signup Error")
    conn.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec_())
