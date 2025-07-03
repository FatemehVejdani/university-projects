import sys 
from PyQt5 import uic , QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem

# --- Initialize the main Qt application ---
app = QtWidgets.QApplication(sys.argv)

# --- Load UI files (designed in Qt Designer) ---
login_L = uic.loadUi("login.ui")               # Login window
win =  uic.loadUi("admin2.ui")                 # Admin main window
add_p = uic.loadUi("add.ui")                   # Add new user/product window
passwordchange = uic.loadUi("passwordchange.ui")  # Password change window
customerfnew = uic.loadUi("customerfnew.ui")   # Customer main window


# --- Handle login logic based on username/password ---
def login():
    username = login_L.le_username.text()
    password = login_L.le_password.text()
    
    # Admin credentials (example)
    if username == 'admin' and password == '123':
        win.show()
        login_L.close()
    
    # Customer credentials (hardcoded)
    if username == 'fatemehvejdani' and password == '456':
        customerfnew.show()
        login_L.close()


# --- Switch to password change window from customer view ---
def passwordchange_1():
    passwordchange.show()
    customerfnew.close()

# --- Switch to add page from admin view ---
def add():
    add_p.show()
    win.close()

# --- Close add page and return to admin window ---
def add_close():
    win.show()
    add_p.close()


# --- Dummy data for admin view (tree widget setup) ---
ls = [("fatemehvejdani", "fatemeh", "vejdani", "456", "456", "10000")]
for item in ls:
    n = QTreeWidgetItem()
    n.setText(0, item[0])
    n.setText(1, item[1])
    n.setText(2, item[2])
    n.setText(3, item[3])
    n.setText(4, item[4])
    n.setText(5, item[5])
    win.tree_list.addTopLevelItem(n)


# --- Logout handlers ---
def customerf_logout():
    login_L.show()
    customerfnew.close()

def admin_logout():
    login_L.show()
    win.close()

# --- Handle password change validation ---
def passwordchange_ok():
    passwordold = passwordchange.le_passwordold.text()
    passwordnew = passwordchange.le_passwordnew.text()
    
    if passwordold != '456':
        erroroldpassword.show()
    elif passwordnew == '456':
        errornewpassword.show()
    else:
        customerfnew.show()
        passwordchange.close()

# --- Cancel password change ---
def passwordchange_close():
    customerfnew.show()
    passwordchange.close()


# --- GUI component bindings (signals to slots) ---
labels = ["username", "name", "family", "password", "account name", "holding"]
win.tree_list.setHeaderLabels(labels)

add_p.btn_close.clicked.connect(add_close)
win.ac_add.triggered.connect(add)
win.ac_logout.triggered.connect(admin_logout)
customerfnew.btn_logout.clicked.connect(customerf_logout)
login_L.btn_login.clicked.connect(login)
customerfnew.btn_passwordchange.clicked.connect(passwordchange_1)
passwordchange.btn_ok.clicked.connect(passwordchange_ok)
passwordchange.btn_close.clicked.connect(passwordchange_close)


# --- Start the login page as entry point ---
login_L.show()
app.exec_()
