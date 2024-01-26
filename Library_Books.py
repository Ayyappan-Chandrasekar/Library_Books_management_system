from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import mysql.connector as mc


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.fbox = QFormLayout()
        self.Email = QLabel("Email ID")
        self.Email_lb = QLineEdit()
        self.password = QLabel("Password")
        self.password_lb = QLineEdit()
        # self.lb3=QLabel("Google")
        # self.lb3.setAlignment(Qt.AlignCenter)
        # self.sgog=QLineEdit()

        # Set password field to show asterisks for password input
        self.password_lb.setEchoMode(QLineEdit.Password)

        self.Login_btn = QPushButton("Login")
        self.Login_btn.clicked.connect(self.login)
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_fields)
        self.close_btn = QPushButton("close")
        self.close_btn.clicked.connect(self.get_close)

        self.fbox.addRow(self.Email, self.Email_lb)
        self.fbox.addRow(self.password, self.password_lb)
        # self.fbox.addRow(self.lb3)
        self.fbox.addRow(self.Login_btn, self.clear_btn)
        self.fbox.setAlignment(Qt.AlignCenter)
        # self.fbox.addRow(self.clr_btn)
        self.fbox.addRow(self.close_btn)

        self.setLayout(self.fbox)
        self.setGeometry(600, 150, 300, 150)
        self.setWindowTitle("Welcome Log-in")
        self.show()

    def get_close(self):
        self.close()

    def clear_fields(self):
        self.Email_lb.clear()
        self.password_lb.clear()

    def login(self):
        Email_ID = self.Email_lb.text()
        Password = self.password_lb.text()

        # Perform authentication logic (replace with your authentication logic)
        if Email_ID == "ayyappan" and Password == "password":
            self.close()  # Close the login window
            self.Library_Buy()
            QMessageBox.information(self, "Login Successful", "Success")
            # print("Login successful!")
        else:
            # self.close()  # Close the login window
            # self.Library_Buy()
            QMessageBox.warning(self, "Login Failed", "Invalid Username or password, Please try again.")
            # print("Login failed!")

    def Library_Buy(self):
        self.main_window = Libary()
        self.main_window.show()


class Libary(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Log_in Success')
        self.setGeometry(600, 150, 300, 120)

        label = QLabel('Log_in Success Welcome Library Books')

        self.Buy_btn = QPushButton("Buy")
        self.Buy_btn.clicked.connect(self.Buy_open)
        self.Buy_btn.clicked.connect(self.close)
        self.Return_btn = QPushButton("Return")
        self.Return_btn.clicked.connect(self.Return_ID)
        self.Return_btn.clicked.connect(self.close)
        # self.Return_btn.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.Buy_btn)
        layout.addWidget(self.Return_btn)

        self.setLayout(layout)

        self.close()  # Close the login window

    def Buy_open(self):
        self.Buy_window = Buy()
        self.Buy_window.show()

    def Return_ID(self):
        self.Return_window = Return_Books()
        self.Return_window.show()


class Buy(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.fbox = QFormLayout()
        self.ID_lb1 = QLabel("ID")
        self.ID = QLineEdit()
        self.lb1 = QLabel("Name")
        self.sname = QLineEdit()
        self.lb2 = QLabel("Address")
        self.addr = QTextEdit()
        self.lb3 = QLabel("Date")
        self.dob = QDateEdit()
        self.lb4 = QLabel("City")
        self.city = QComboBox()
        self.city.addItem("Chennai")
        l = ["Pondicherry", "Mumbai", "Bangalaore", "Andhra Pradesh", "Kerala", "Assam", "Bihar", "Chhattisgarh", "Goa",
             "Gujarat"]
        self.city.addItems(l)
        self.hbox = QHBoxLayout()
        self.Lan = QLabel("Book_Language")
        self.TAMIL = QRadioButton()
        self.TAMIL.setText("TAMIL")
        self.ENGLISH = QRadioButton()
        self.ENGLISH.setText("ENGLISH")

        # self.lb6 = QLabel("Book Title")
        self.Book_title = QLabel("Book Title")
        self.Book_l = QComboBox()
        self.Book_l.addItem("Wiley")
        t = ["Springer", "OUP", "Academy", "Pearson", "Elsiver", "Computer Science", "Mutual Funts", "Cenima", "Tech", ]
        self.Book_l.addItems(t)

        # self.course = QListWidget()
        self.Buy_N_btn = QPushButton("Buy")
        self.Buy_N_btn.clicked.connect(self.Buy_success)
        self.Buy_N_btn.clicked.connect(self.Library_Buy)
        self.Buy_N_btn.clicked.connect(self.clear_fields)
        # self.Buy_N_btn.clicked.connect(self.close)
        self.can_btn = QPushButton("close")
        self.can_btn.clicked.connect(self.get_close)

        self.hbox = QHBoxLayout()
        self.fbox.addRow(self.ID_lb1, self.ID)
        self.fbox.addRow(self.lb1, self.sname)
        self.fbox.addRow(self.lb2, self.addr)
        self.fbox.addRow(self.lb3, self.dob)
        self.fbox.addRow(self.lb4, self.city)
        self.fbox.addRow(self.Lan, self.hbox)
        self.hbox.addWidget(self.TAMIL)
        self.hbox.addWidget(self.ENGLISH)
        self.fbox.addRow(self.Book_title, self.Book_l)
        # self.fbox.addRow(self.lb6, self.course)
        self.fbox.addRow(self.Buy_N_btn, self.can_btn)

        self.setLayout(self.fbox)
        self.setGeometry(600, 150, 600, 600)
        self.setWindowTitle("Buying to Library")
        self.show()

    def Library_Buy(self):
        self.main_window = Libary()
        self.main_window.show()

    def Buy_close(self):
        self.close()

    def get_close(self):
        self.close()

    def clear_fields(self):
        self.ID.clear()
        self.sname.clear()
        self.addr.clear()


    def Buy_success(self):

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="marvel@studio",
                database="Library")
            mycursor = mydb.cursor()

            s1 = self.ID.text()
            s2 = self.sname.text()
            s3 = self.addr.toPlainText()
            s4 = self.dob.date().toPyDate()
            s5 = self.city.currentText()
            s6 = ""
            if self.TAMIL.isChecked() == True:
                s6 = self.TAMIL.text()
            else:
                s6 = self.ENGLISH.text()

            s7 = self.Book_l.currentText()
            # s7 = item.text()
            print(s1)
            print(s2)
            print(s3)
            print(s4)
            print(s5)
            print(s6)
            print(s7)
            sql = "INSERT INTO Buy_Library (id, name, address, date, city, book_Language, book_title) VALUES (%s, %s,%s,%s,%s,%s,%s)"
            val = (s1, s2, s3, s4, s5, s6, s7)

            mycursor.execute(sql, val)

            mydb.commit()

        except Exception as e:
            print(e)

        QMessageBox.information(self, "Login Successful", "Success")


class Return_Books(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 800, 400)

        self.ID = QLabel('Enter ID:')
        self.ID_Edit = QLineEdit()
        self.btn_search = QPushButton('Search')
        self.btn_search.clicked.connect(self.displayData)
        self.btn_Return = QPushButton('Return')
        self.btn_Return.clicked.connect(self.Book_Return)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "Name", "Address", "Date", "City", "Book_Language", "Book_title"])

        self.fbox = QFormLayout()
        self.fbox.addRow(self.ID, self.ID_Edit)

        # self.fbox.addRow(self.ID_Edit)
        self.fbox.addRow(self.btn_search, self.btn_Return)
        self.fbox.setAlignment(Qt.AlignCenter)
        # layout.addWidget(self.btn_Return)
        self.fbox.addRow(self.table_widget)

        container = QWidget()
        container.setLayout(self.fbox)

        self.setCentralWidget(container)

    def displayData(self):
        try:
            self.mydb = mc.connect(
                host='localhost',
                user='root',
                password='marvel@studio',
                database='Library'
            )
            self.mycursor = self.mydb.cursor()

            ID = self.ID_Edit.text()
            query = "SELECT * FROM Buy_Library where id=%s"
            val = (ID,)
            self.mycursor.execute(query, val)

            data = self.mycursor.fetchone()

            # Clear existing data in the table
            self.table_widget.setRowCount(7)

            if data:
                row_num = 0
                self.table_widget.insertRow(row_num)
                for column_num, value in enumerate(data):
                    self.table_widget.setItem(row_num, column_num, QTableWidgetItem(str(value)))
            else:
                print("No data found for ID:", id)
                QMessageBox.information(self, "ID check", "Please Enter Valid ID".format(ID))

        except Exception as e:
            print(e)

    def Book_Return(self):
        try:
            self.mydb = mc.connect(
                host='localhost',
                user='root',
                password='marvel@studio',
                database='Library'
            )
            self.mycursor = self.mydb.cursor()

            ID = self.ID_Edit.text()
            query = "delete FROM Buy_Library WHERE id = %s"
            val = (ID,)
            self.mycursor.execute(query, val)
            self.mydb.commit()

            if ID:
                QMessageBox.information(self, "Data Deleted", "Student data with ID {} has been deleted.".format(ID))
            else:
                QMessageBox.information(self, "Valid ID", "Please check data ID or Enter valid ID.".format(ID))
            # self.clear_table()

        except Exception as e:
            print(e)


# def main():
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = LoginWindow()
    Login.show()
    sys.exit(app.exec())

