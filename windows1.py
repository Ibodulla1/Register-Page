from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QFont

usernames = []
emails = []

def reading():
    with open("Register_Data.txt") as r:
        data = r.read().split('\n')

        for i in data:
            if i != '':
                i = i.split('|')
                usernames.append(i[3])
                emails.append(i[4])



class Register_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.check = False

        self.setGeometry(600,250,600,500)
        self.setWindowTitle("REGISTER")

        self.First_Name = QLabel("First Name: ")
        self.First_Name.setFont(QFont("Times",15))
        self.First_Name_Edit = QLineEdit()
        self.First_Name_Edit.setFont(QFont("Times",12))
        self.First_Name_Edit.setPlaceholderText("Enter Your First name...")


        self.Last_Name = QLabel("Last Name: ")
        self.Last_Name.setFont(QFont("Times",15))
        self.Last_Name_Edit = QLineEdit()
        self.Last_Name_Edit.setFont(QFont("Times",12))
        self.Last_Name_Edit.setPlaceholderText("Enter Your Last name...")

        self.Phone_Num = QLabel("Phone Number: ")
        self.For_Phone_Num = QLabel("")
        self.Phone_Num.setFont(QFont("Times",15))
        self.Phone_Num_Edit = QLineEdit()
        self.Phone_Num_Edit.setFont(QFont("Times",12))
        self.Phone_Num_Edit.setPlaceholderText("+998...")

        self.Username = QLabel("Username: ")
        self.Username.setFont(QFont("Times",15))
        self.Username_Edit = QLineEdit()
        self.Username_Edit.setFont(QFont("Times",12))
        self.Username_Edit.setPlaceholderText("Enter Your Username...")

        self.Email = QLabel("Email: ")
        self.For_Email = QLabel("")
        self.Email.setFont(QFont("Times",15))
        self.Email_Edit = QLineEdit()
        self.Email_Edit.setFont(QFont("Times",12))
        self.Email_Edit.setPlaceholderText("Enter Your Email...")

        self.Send_Button = QPushButton("REGISTER")
        self.Send_Button.setFont(QFont("Arial",15))
        self.Send_Button.setStyleSheet("background-color : blue; color:white")
        self.Send_Button.clicked.connect(self.Send_Close)




        self.Q_V_Layout_Register = QVBoxLayout()

        self.Q_V_Layout_Register.addWidget(self.First_Name)
        self.Q_V_Layout_Register.addWidget(self.First_Name_Edit)
        self.Q_V_Layout_Register.addWidget(self.Last_Name)
        self.Q_V_Layout_Register.addWidget(self.Last_Name_Edit)
        self.Q_V_Layout_Register.addWidget(self.Phone_Num)
        self.Q_V_Layout_Register.addWidget(self.Phone_Num_Edit)
        self.Q_V_Layout_Register.addWidget(self.For_Phone_Num)
        self.Q_V_Layout_Register.addWidget(self.Username)
        self.Q_V_Layout_Register.addWidget(self.Username_Edit)
        self.Q_V_Layout_Register.addWidget(self.Email)
        self.Q_V_Layout_Register.addWidget(self.Email_Edit)
        self.Q_V_Layout_Register.addWidget(self.For_Email)
        self.Q_V_Layout_Register.addWidget(self.Send_Button)

        self.setLayout(self.Q_V_Layout_Register)


    def Send_Close(self):
            if self.First_Name_Edit.text() != '' and self.Last_Name_Edit.text() != '' and self.Phone_Num_Edit.text().isdigit() and '@' in self.Email_Edit.text():

                with open("Register_Data.txt", "a") as r:

                    r.write(f"{self.First_Name_Edit.text()}|{self.Last_Name_Edit.text()}|{self.Phone_Num_Edit.text()}|{self.Username_Edit.text()}|{self.Email_Edit.text()}\n")

                self.First_Name_Edit.clear()
                self.Last_Name_Edit.clear()
                self.Phone_Num_Edit.clear()
                self.Username_Edit.clear()
                self.Email_Edit.clear()

                self.check = True

                Message_Box = QMessageBox()
                Message_Box.setText("You Have Successfully Registered")
                Message_Box.setStyleSheet("background-color : green; color:white")
                Message_Box.adjustSize()
                Message_Box.show()
                Message_Box.exec_()

                self.close()    













class Login_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.check = False

        self.setGeometry(600,300,600,400)
        self.setWindowTitle("LOGIN")
        self.setStyleSheet("background-color: black")

        self.Username_Label = QLabel("Enter Your Username: ")
        self.Username_Label.setFont(QFont("Times",25))
        self.Username_Label.setStyleSheet("color:lightgreen")

        self.Username_Edit = QLineEdit()
        self.Username_Edit.setFont(QFont("Times",20))
        self.Username_Edit.setStyleSheet("background-color:white")
        self.Username_Edit.setPlaceholderText("username...")



        self.Email_Label = QLabel("Enter Your Email: ")
        self.Email_Label.setFont(QFont("Times",25))
        self.Email_Label.setStyleSheet("color:lightgreen")

        self.Email_Edit = QLineEdit()
        self.Email_Edit.setFont(QFont("Times",20))
        self.Email_Edit.setStyleSheet("background-color:white")
        self.Email_Edit.setPlaceholderText("email...")

        self.Login_Button = QPushButton("LOGIN")
        self.Login_Button.setFont(QFont("Arial",25))
        self.Login_Button.setStyleSheet("background-color:green; color:white")
        self.Login_Button.clicked.connect(self.login_button)


        self.V_Box = QVBoxLayout()
        
        self.V_Box.addWidget(self.Username_Label)
        self.V_Box.addWidget(self.Username_Edit)

        self.V_Box.addWidget(self.Email_Label)
        self.V_Box.addWidget(self.Email_Edit)
        self.V_Box.addWidget(self.Login_Button)

        self.setLayout(self.V_Box)


    def login_button(self):
        reading()
        Message_Box = QMessageBox()
        Message_Box.setWindowTitle("LOGIN")

        if self.Email_Edit.text() == '' and self.Username_Edit.text() == '':

            Message_Box.setText("You Have Not Entered Anything")
            Message_Box.setStyleSheet("background-color: red; color: white")
            Message_Box.show()
            Message_Box.exec_()

        elif self.Email_Edit.text() in emails and self.Username_Edit.text() in usernames:
                Message_Box.setText("You Have Successfully Logged In")
                Message_Box.setStyleSheet("background-color: darkgreen; color: white")
                Message_Box.show()
                Message_Box.exec_()
                self.close()
                

        elif self.Email_Edit.text() not in emails:
            self.Email_Edit.setText("")
            Message_Box.setText("No Such Email was Found")
            Message_Box.setStyleSheet("background-color: red; color: white")
            Message_Box.show()
            Message_Box.exec_()

        elif self.Username_Edit.text() not in usernames:
            self.Username_Edit.setText("")
            Message_Box.setText("No Such Username was Found")
            Message_Box.setStyleSheet("background-color: red; color: white")
            Message_Box.show()
            Message_Box.exec_()

        

            

            
            
                






















class Register(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Main_W = QWidget()

        self.Register_BTN = QPushButton("REGISTER")
        self.Register_BTN.setStyleSheet("background-color:Green")
        self.Register_BTN.setFont(QFont("Arial",25))
        self.Register_BTN.clicked.connect(self.Register_Page)


        self.Login_BTN = QPushButton("LOGIN")
        self.Login_BTN.setStyleSheet("background-color:red")
        self.Login_BTN.setFont(QFont("Arial",25))
        self.Login_BTN.clicked.connect(self.Login_Page)

        self.Close_BTN = QPushButton("CLOSE")
        self.Close_BTN.setStyleSheet("background-color:black;color:white")
        self.Close_BTN.setFont(QFont("Arial",25))
        self.Close_BTN.clicked.connect(self.close)



        self.Q_V_layout = QVBoxLayout()

        self.Q_V_layout.addWidget(self.Register_BTN)
        self.Q_V_layout.addWidget(self.Login_BTN)
        self.Q_V_layout.addWidget(self.Close_BTN)

        self.Main_W.setLayout(self.Q_V_layout)

        self.setCentralWidget(self.Main_W)


    def Register_Page(self):
        self.Register_Obj = Register_Window()
        self.Register_Obj.show()
        

    def Login_Page(self):
        self.Login_Obj = Login_Window()

        self.Login_Obj.show()    







if __name__ == "__main__":
    app = QApplication([])
    Page = Register()
    Page.show()
    Page.setWindowTitle("REGISTER AND LOGIN")
    Page.setWindowIcon(QIcon("C:\\Users\\Ibodulla Jumaniyozov\\Downloads\\register.jpg"))
    Page.setGeometry(600,200,600,600)
    app.exec_()
