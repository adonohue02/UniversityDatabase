import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tacosrock1"
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE University_Library")
mycursor.execute("CREATE DATABASE University_Library")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tacosrock1",
    database="University_Library"
)

mycursor = mydb.cursor()
#Create Lib_member
mycursor.execute(
    "CREATE TABLE Lib_Member (mobile_no varchar(11) NOT NULL,F_name varchar(255) NOT NULL, L_name varchar(255) NOT "
    "NULL,validity varchar(255) NOT NULL,DOB varchar(10) NOT NULL,address varchar(255) NOT NULL,primary key (mobile_no, F_name, L_name)) "
    )
#Insert into Lib_member
mycursor.execute("insert into Lib_member  values('8456541234', 'Jack','frank', 'valid', '11-21-1998', '51 connor ct');")
mycursor.execute("insert into Lib_member  values('0983845869', 'frank','eddison', 'valid', '11-21-1998',"
                 "'41 toe street');")
mycursor.execute("insert into Lib_member  values('1284950394', 'jeff','egg', 'valid', '11-21-1998','78 jefferson dr');")
mycursor.execute("insert into Lib_member  values('3478274958', 'Allisa','bergandi', 'valid', '11-21-1998','20 lacross "
                 "ave');")
mycursor.execute("insert into Lib_member  values('4145842293', 'shawn','white', 'valid', '11-21-1998','45 sherbert "
                 "lane');")
mycursor.execute("insert into Lib_member  values('9148573329', 'jessica','connors', 'valid', '11-21-1998',"
                 "'14 new lane');")
mycursor.execute("insert into Lib_member  values('6461129349', 'aidan','showman', 'valid', '11-21-1998','3 pella ct');")
mycursor.execute("insert into Lib_member  values('9174561547', 'jackson','black', 'valid', '11-21-1998','17 mouacdie "
                 "dr');")
mycursor.execute("insert into Lib_member  values('8456541234', 'fernando','fredrickson', 'valid', '11-21-1998',"
                 "'23 edward ave');")
mycursor.execute("insert into Lib_member values('71322949586', 'ashlyn','swonson', 'valid', '11-21-1998','4 bedrock "
                 "lane');")
mydb.commit()
#Create Issues
mycursor.execute(
    "CREATE TABLE Issues (Issue_id varchar(40) NOT NULL,issue_type  varchar(255) NOT NULL,return_date varchar(11) NOT "
    "NULL, mobile_no varchar(11) NOT NULL,F_name varchar(255) NOT NULL, L_name varchar(255), primary key(issue_id, mobile_no, f_name, l_name))")
#Insert into Issues
mycursor.execute("insert into Issues values('0001','ripped pages','11-12-2019','8456541234', 'Jack','frank');")
mycursor.execute("insert into Issues values('0002','no front cover','10-15-2019','0983845869', 'frank','eddison');")
mycursor.execute("insert into Issues values('0003','missing book id','12-6-2019','1284950394', 'jeff','egg');")
mycursor.execute("insert into Issues values('0004','lost book','08-19-2019','3478274958', 'Allisa','bergandi');")
mycursor.execute("insert into Issues values('0005','falling apart','05-13-2019','4145842293', 'shawn','white');")
mycursor.execute("insert into Issues values('0006','wrong book','01-12-2019','9148573329', 'jessica','connors');")
mycursor.execute("insert into Issues values('0007','left book at library','04-01-2019','6461129349', 'aidan','showman');")
mycursor.execute("insert into Issues values('0008','water damage','04-23-2019','9174561547', 'jackson','black');")
mycursor.execute("insert into Issues values('0009','fell in fire','08-12-2019','8456541234', 'fernando','fredrickson');")
mycursor.execute("insert into Issues values('0010','stolen book','11-07-2019','71322949586', 'ashlyn','swonson');")
mydb.commit()
#Create Librarian
mycursor.execute(
    "CREATE TABLE Librarian (LIB_id varchar(40) NOT NULL,name  varchar(255) NOT NULL,primary key (lib_id))")
#insert into Librarian
mycursor.execute("insert into librarian values ('0000', 'Jack')")
mycursor.execute("insert into librarian values ('0001', 'mark')")
mycursor.execute("insert into librarian values ('0010', 'Shawn')")
mycursor.execute("insert into librarian values ('0011', 'Pan')")
mycursor.execute("insert into librarian values ('0100', 'Angila')")
mycursor.execute("insert into librarian values ('0101', 'Oscar')")
mycursor.execute("insert into librarian values ('0110', 'Dwight')")
mycursor.execute("insert into librarian values ('0111', 'Micheal')")
mycursor.execute("insert into librarian values ('1000', 'Jane')")
mycursor.execute("insert into librarian values ('1001', 'Frank')")
mydb.commit()
#create table book
mycursor.execute(
    "CREATE TABLE Book (book_id varchar(40) NOT NULL,title  varchar(255) NOT NULL,Publisher varchar(255) NOT NULL,"
    "publish_date varchar(12) NOT NULL,lib_id varchar(12) NOT NULL,primary key (book_id, lib_id),foreign key (lib_id) "
    "references librarian (lib_id))")
#insert into book
mycursor.execute("insert into Book values('109586472','The hitch hiker guide to 3 universes','John Doe', '11-30-1985', '0000');")
mycursor.execute("insert into Book values('109857625','Cook the percect toast','Fredrick Aids', '12-14-1995', '0001');")
mycursor.execute("insert into Book values('109581123','How to pass cmpt 258','Dr. Agrawal', '09-07-1973', '0010');")
mycursor.execute("insert into Book values('109049576','how to make money','John Denver', '01-04-1971', '0011');")
mycursor.execute("insert into Book values('129384750','The size of earth','Frank Frankenson', '07-01-2004', '0100');")
mycursor.execute("insert into Book values('203948552','Learn Python 101','Howard Toaster', '04-26-1978', '0101');")
mycursor.execute("insert into Book values('304958123','Where the money at foo','Shiquan Davids', '03-15-1956', '0110');")
mycursor.execute("insert into Book values('109485622','Story of my life','Aidan Jakers', '10-29-1983', '0111');")
mycursor.execute("insert into Book values('148571028','Goodnight moon','Jack Nob', '03-14-1940', '1000');")
mycursor.execute("insert into Book values('574839102','My Side of the mountain','Jake Doctor', '06-11-2001', '1001');")
mydb.commit()
#create borrow
mycursor.execute(
    "CREATE TABLE Borrow (mobile_no varchar(255) NOT NULL,f_name  varchar(255) NOT NULL,l_name varchar(255) NOT NULL,book_id varchar(255) Not null)")
#insert into borrow
mycursor.execute("insert into Borrow  values('8456541234', 'Jack','frank', '109586472');")
mycursor.execute("insert into Borrow  values('8456541235', 'frank','eddison', '109857625');")
mycursor.execute("insert into Borrow  values('8456541236', 'jeff','egg', '109581123');")
mycursor.execute("insert into Borrow  values('8456541267', 'Allisa','bergandi','109049576');")
mycursor.execute("insert into Borrow  values('8456541235', 'shawn','white', '129384750');")
mycursor.execute("insert into Borrow  values('8456541269', 'jessica','connors','203948552');")
mycursor.execute("insert into Borrow  values('8456541234', 'aidan','showman','304958123');")
mycursor.execute("insert into Borrow  values('8436541234', 'jackson','black', '109586472');")
mycursor.execute("insert into Borrow  values('8456541234', 'fernando','fredrickson','148571028');")
mycursor.execute("insert into Borrow values('8456875234', 'ashlyn','swonson','574839102');")
mydb.commit()

#
def opt1():
    f_name = str(input("Enter first name:"))
    l_name = str(input("Enter last name:"))
    sqlQuery = "SELECT distinct \
        issue_id \
        FROM issues \
        natural join lib_member\
        where f_name = %s and l_name = %s"
    val = (f_name, l_name)

    #print("sql query = " + sqlQuery)
    mycursor.execute(sqlQuery, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Issue id:", x[0])




def opt2():
    book_id = str(input("Enter the book id to change the title of the book:"))
    title = str(input("Enter new title of the book:"))
    sqlQuery = "UPDATE book SET book.title = %s WHERE book.book_id = %s "
    # sqlQuery = "SELECT * FROM department WHERE dept_name =  '" + dept_name +"'"
    val = (title, book_id)
    try:
        mycursor.execute(sqlQuery, val)
        myresult = mycursor.fetchmany()
        print("Title has been changed")
        mydb.commit()
    except mysql.connector.Error as error:
        mydb.commit()
        print("Title already exists in database.")






def opt3():
    mobile_no = str(input("Enter new members mobile number :"))
    sqlQuery = "SELECT lib_member.mobile_no FROM lib_member WHERE lib_member.mobile_no= '" + mobile_no + "'"
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sqlQuery)
        myresult = mycursor.fetchone()
        print(myresult)
    except mysql.connector.Error as error:
        print("Department doesn't exist")
        exit(0)

    f_name = str(input("Enter the new members first name:"))
    l_name = str(input("Enter the new members last name:"))
    validity = str(input("Enter the new members validity:"))
    DOB = str(input("Enter the new members Date of Birth:"))
    address = str(input("Enter the new members address:"))
    try:
        sqlQuery = "INSERT INTO lib_member (mobile_no, f_name,l_name, validity, DOB, address) VALUES (%s, %s,%s,%s,%s,%s)"
        val = (mobile_no, f_name, l_name, validity, DOB, address)
        mycursor.execute(sqlQuery, val)
        print("Member added to database ")
        mydb.commit()
    except mysql.connector.Error as error:
        print("Member already exists in the database.")


def opt4():
    mobile_no = str(input("Enter Member mobile number:"))
    sqlQuery = "Delete from lib_member where lib_member.mobile_no = %s"
    val = (mobile_no,)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sqlQuery, val)
        myresult = mycursor.fetchall()
    except mysql.connector.Error as error:
        mydb.commit()
        print("Member deleted.")


while True:
    print("1. Enter the first and last name of a member and i will provide you with the issue id \n")
    print("2. Enter a book id and modify the title  \n ")
    print("3. Insert a record about a new member.\n")
    print("4. Delete a record about a member\n")
    print("5. Exit\n")
    i = int(input("Enter Your choice :"))
    if i == 5:
        break
    elif i == 1:
        opt1()
    elif i == 2:
        opt2()
    elif i == 3:
        opt3()
    elif i == 4:
        opt4()
