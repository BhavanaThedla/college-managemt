import mysql.connector as mysql
db = mysql.connect(host = "localhost",user = "root",password = "Indhu@408",database = "college")
command_handler = db.cursor(buffered = True)

def student_session(username):
    print("Login success")
    print("Welcome student")
    while 1:
        print("")
        print("Student's Menu:")
        print("1.Viewing Register")
        print("2.Logout")
        user_option = input(str("Option:"))
        if user_option =="1":
            print("Viewing Register")
            username=(str(username),)
            command_handler.execute("SELECT date,username,status FROM attendance WHERE username=%s",username)
            records=command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option =="2":
            print("You have been logged out")
            break
        else:
            print("No valid option was selected")



def teacher_session():
    print("Login Success")
    print("Welcome Teacher")
    while 1:
        print("Teachers Menu:")
        print("1.Mark student register")
        print("2.View student register")
        print("3.Logout")

        user_option = input(str("Option:"))
        if user_option == "1":
            print("")
            print("Mark Student Register")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date : DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                status = input(str("Status for " + str(record) + "P/A/L:"))
                query_vals = (str(record),date,status)
                command_handler.execute("INSERT INTO attendance (username,date,status) VALUES(%s,%s,%s)",query_vals)
                db.commit()
                print(record + " Marked as " +  status)
        elif user_option =="2":
            print("")
            print("Viewing the student register") 
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying Students Register")
            for record in records:
                print(record)
        elif user_option =="3":
            print("You have been logged out")
            break
        else:
            print("No valid option was selected")   



def admin_session():
    print("Login successs")
    print("Welcome Admin")
    while 1:
        print("Admin Menu:")
        print("1.Register a new Student")
        print("2.Register a new Teacher")
        print("3.Deleting Existing Student")
        print("4.Deleting Existing Teacher")
        print("5.Logout")

        user_option = input(str("Option:"))

        if user_option == "1":
            print("")
            print("Register a New Student")
            username = input(str("Student username:"))
            password = input(str("Student password:"))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES(%s,%s,'student')",query_vals)
            db.commit()
            print(username + " has been registered as a Student")

        elif user_option == "2":
            print("")
            print("Register a New Teacher")
            username = input(str("Teacher username:"))
            password = input(str("Teacher password:"))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES(%s,%s,'teacher')",query_vals)
            db.commit()
            print(username + " has been registered as a Teacher")

        elif user_option =="3":
            print("")
            print("Delete Existing Student Account")
            username = input(str(" Student Username:"))
            query_vals = username,"student"
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username + " has been deleted")
        
        elif user_option =="4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str(" Teacher Username:"))
            query_vals = username,"teacher"
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username + " has been deleted")
            
        elif user_option == "5":
            print("You have been logged out")
            break
        else:
            print("no valid option was selected")

def auth_student():
    print("")
    print("Student's Login")
    print("")
    username = input(str("Username:"))
    password = input(str("Password:"))
    query_vals = (username,password,"student")
    command_handler.execute("SELECT username FROM users WHERE username= %s AND password= %s AND privilege = %s",query_vals)
    #username = command_handler.fetchone()
    if command_handler.rowcount <= 0:
        print("login does not recognized")
    else:
        student_session(username)


def auth_teacher():
    print("")
    print("Teacher's Login")
    print("")
    username = input(str("Username:"))
    password = input(str("Password:"))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'",query_vals)
    if command_handler.rowcount<=0:
        print("login does not recognized")
    else:
        teacher_session()


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username:"))
    password = input(str("password:"))
    if username == "admin":
        if password =="password":
            admin_session()
        else:
            print("Invalid password")
    else:
        print("Login details not recognised")
    
def main():
    while 1:
        print("Welcome to the system")
        print("")
        print("1.Login as a Student")
        print("2.Login as a Teacher")
        print("3.Login as a Admin")
        user_option = input(str("Option:" ))
        if user_option == "1":
            auth_student()
        elif user_option =="2":
            auth_teacher()
        elif user_option =="3":
            auth_admin()
        else: 
            print("No valid option is selected")

main()