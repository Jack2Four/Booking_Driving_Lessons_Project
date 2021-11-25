##############################
#           Imports          #
##############################
from guizero import App, Window, Text, PushButton, TextBox, info, Box, ButtonGroup, Combo, Picture, Waffle
import sqlite3 as sql
from sqlite3 import Error
import sqlite3
import os
import os.path
from datetime import datetime
import time
count = 0

###############################################
#           Procedures and Functions          #
###############################################

def newpage():
    window4.hide()
    window5.show()

def backbutton():
    window4.hide()
    window3.show()

def done_button():
    # done button procedure for checking whether or not the person is in the database or not.
    global row
    global temp3
    # validation for if null
    if textbox2.value =="":
        info("Error!", "You must enter a Username!")
    elif textbox3.value == "":
        info("Error!", "You must enter a Password!")
    else:
        # sql for selecting the username and password the user entered and search for it in the database
        query = ("SELECT * from User_Table WHERE Username = "+ "'"+ str(textbox2.value) + "'"+ " AND Password = "+ "'" + str(textbox3.value) + "'")
        print(query)
        # gets that row 
        row = query_database("DrivingLessons.db", query)
        # checks if the legnth of thr row is nothing if it is, nothing was found.
        if len(row) == 0:
            info("Error!", "Your details are not in our database! Try again.")
        else:
            # the sql which lets you through to the notes page if you login details are fine.
            temp3 = str(row[0][0])
            open_window3()
            close_window()
            app.hide()

# signup checking that once the information from signing up has been uploaded to the database that it is actually updated.
def signup_verification():
    global row
    global temp3
    # sql for selecting where username and password are to get the row
    query = ("SELECT * from User_Table WHERE Username = "+ "'"+ str(txtbox2.value) + "'"+ " AND Password = "+ "'" + str(txtbox7.value) + "'")
    print(query)
    row = query_database("DrivingLessons.db", query)
    # does the exact same as in the function done_dutton() by checking it found a row
    if len(row) == 0:
        info("Error!", "Your details are not in our database! Try again.")
    else:
        # opens the notes page and closes down windows no longer in use.
        temp3 = str(row[0][0])
        open_window3()
        close_window()
        app.hide()

def done_button_clicked_signup():
    # validation on signing up
    if txtbox2.value == "":
        info("Error!", "You must enter a Username!")
    elif len(txtbox2.value) <= 3:
        info("Error!", "Username must be larger than 3 characters!")
    elif len(txtbox2.value) >= 12:
        info("Error!", "Username too large must be below 12 characters!")
    elif txtbox3.value == "":
        info("Error!", "You must enter a Firstname!")
    elif txtbox4.value == "":
        info("Error!", "You must enter a Surname!")
    elif txtbox5.value == "":
        info("Error!", "You must enter a Email!")
    elif "@" and "." not in txtbox5.value:
        info("Error!", "'Email' must have @ and a '.'!")
    elif txtbox6.value == "":
        info("Error!", "You must enter a Date of Birth!")
    elif "/" not in txtbox6.value:
        info("Error!", "'Date of birth must be in this format DD/MM/YYYY!")
    elif txtbox7.value == "":
        info("Error!", "You must enter a Password!")
    elif len(txtbox7.value) <= 3:
        info("Error!", "Password must be larger than 3 characters!")
    elif len(txtbox7.value) >= 12:
        info("Error!", "Password too large must be below 12 characters!")
    elif txtbox7.value == txtbox8.value:
        #insert the data into the database
        mysql2 = ("INSERT INTO User_Table(Username, Password, Forename, Surname, Email, DateOfBirth) VALUES ('"+ str(txtbox2.value) + "','" + str(txtbox7.value) + "','" + str(txtbox3.value) + "','" + str(txtbox4.value) + "','" + str(txtbox5.value) + "','" + str(txtbox6.value)+ "')")
        print(mysql2)
        Noidea2 = execute_sql("DrivingLessons.db", mysql2)
        signup_verification()
        window2.hide()
        window3.show()
    else:
        info("Sorry!","You need to enter your in password the same time twice!")

def LogoutButtonClicked():
    window3.hide()
    app.show()

def BookButtonClicked():
    if buttongroup3.value == "Peter Griffin":
        driverid = 1
    elif buttongroup3.value == "Stan Smith":
        driverid = 2
    elif buttongroup3.value == "Walter White":
        driverid = 3


    if buttongroup2.value == "Yes, I need one":
        CarNeeded = True
    else:
        CarNeeded = False
    now = datetime.now()
    now = now.strftime("%d/%m/%Y, %H:%M")
    print(now)
    userid = str(row[0][0])
    print(row)
    #insert the data into the database
    mysql2 = ("INSERT INTO BookingsTable(CarTransmition, BookingCar, BookingDate, BookingTime, BookedDate, LessonType, UserID, DriverID) VALUES ('"+ str(buttongroup1.value) + "','" + str(CarNeeded) + "','" + str(combo.value) + "','" + str(combo2.value) + "','" + str(now) + "','" + str(buttongroup4.value) + "','" + str(userid) + "','" + str(driverid) + "')")
    print(mysql2)
    Noidea3 = execute_sql("DrivingLessons.db", mysql2)
    info("Success!", "You have successfully booked a lesson!\n These are your details: \n The Lesson will be "+ str(combo.value)+ " at "+ str(combo2.value)+ ".")

def CalenderButtonClicked():
    window3.hide()
    window4.show()

def ShowMyButtonClicked():
    global row
    global count
    dog = row[0][0]
    query = "SELECT * FROM BookingsTable WHERE UserID ="+ str(dog)
    row = query_database("DrivingLessons.db", query)
    print(query)
    print(row)
    # checks if the legnth of thr row is nothing if it is, nothing was found.
    text = Text(window4, text=" ")
    if len(row) == 0:
        info("Sorry!", "You do not have any lessons booked!")
        window4.hide()
        window3.show()
    else:
        if count == 0:
            for i in range(0, len(row)):
                print(i)
                tempory1 = row[i][3]
                tempory2 = row[i][4]
                tempory3 = row[i][5]
                testbox = Box(window4, align="top", border=True)
                blanktext1 = Text(testbox, text=" ")
                text100 = Text(testbox, text=" You have a lesson on: "+ str(tempory1))
                text101 = Text(testbox, text=" The lesson is at: "+ str(tempory2))
                text102 = Text(testbox, text=" You booked this lesson: "+ str(tempory3))
                blanktext1 = Text(testbox, text=" ")
                count = count + 1
        else:
            info("Sorry!","You have already clicked this button dumbass.")



############################################
#        Makes it pop up new windows       #
############################################

# these are mainly used for opening and closing the windows of the GUI
def open_app():
    app.show()

def open_window():
    window.show()
    close_app()

def open_window2():
    window2.show()
    close_app()

def open_window3():
    window3.show()

def close_window():
    window.hide()
    app.show()

def close_window2():
    window2.hide()
    app.show()

def close_window3():
    window3.hide()
    
def close_app():
    app.hide()

###############################################
#                Database Setup               #
#                                             #
#           Delete Existing Database          #
###############################################
# This function deletes a database.
# It's just a file so all it does it 
#  delete the file
def delete_db(database_file):
    if os.path.exists(database_file):
        os.remove(database_file)
#############################################
#           Create Database Tables          #
#############################################
def init_db(database_file, database_sql):   
    # open the sqlite database file
    conn = sqlite3.connect(database_file)

    # connect to it and get a cursor
    # this is like a placeholder in the database
    cursor = conn.cursor()                  
    
    # open the script file containing SQL
    script = open(database_sql, 'r')

    # read the contents of the script 
    # into a string called sql
    sql = script.read()                     
    
    # execute the SQL 
    cursor.executescript(sql)               
    
    # commit the changes to make them permanent
    conn.commit()                           
    
    # close the connection to the database
    conn.close()  
#############################################
#           Insert into Tables          #
#############################################
def insert_data(database_file, sql):
    # open the sqlite database file
    conn = sqlite3.connect(database_file)
    # this is like a placeholder in the database
    script = open(sql, 'r')
    sql = script.read()
    cursor = conn.cursor()
    # execute the SQL 
    cursor.executescript(sql)
    conn.commit()    
    conn.close()
########################################
#          Query the Database          #
########################################

# this peice of code connected to the database file i have in my files
# it then creates a variable to hold all the data and uses cursor function
# it then excecutes the sql code its give and returns all the rows that it found
def query_database(database, query):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows
########################################
#          Insert to Database          #
########################################
# instead of querying the database with sql that would ask SELECT questions and give andswers this bit of ode can be used to excecute and sql given
def execute_sql(database, sql_statement):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(sql_statement)
    conn.commit()
    return cur.lastrowid

#############################################
#              MAIN PROGRAMME               #
#############################################
# creation of the app window
app = App(title="Login/Signup", layout="auto")
app.set_full_screen()
# creates widgets making them look goodo
textblank = Text(app, text=" ")
text = Text(app, text="To book a driving lesson,", size=15)
text2 = Text(app, text="Login or Create an account:", size=15)
textblank = Text(app, text=" ")
box = Box(app, align="top", width="fill")
# contains commands in the buttons so that when it is clicked a command function will happen this is event driven coding.
open_button = PushButton(box, text="Login", command=open_window, width=20)
open_button = PushButton(box, text="Sign Up", command=open_window2, width=20)

#########################
#         Login         #
#########################
# creates the window for the login page
window = Window(app, title="Login")
window.set_full_screen()
textblank = Text(window, text=" ")
box2 = Box(window, width="fill")
window.hide()
# creates widgets
text1 = Text(box2, text="Enter your login:", width="fill", height= "fill", size=15)
textblank = Text(box2,  width="fill", height= "fill", text=" ")
text2 = Text(box2, text="Username: ",  width="fill", height= "fill")
textbox2 = TextBox(box2, hide_text=False,width=30, height= "fill")
text3 = Text(box2, text="Password: ",   width="fill", height= "fill")
textbox3 = TextBox(box2, hide_text=True, width=30, height= "fill")
text4 = Text(box2, text=" ",   width="fill", height= "fill")
# 2 buttons to allow for easy use and direction
done_button = PushButton(window, text="Done", command=done_button, width=10)
close_button = PushButton(window, text="Back", command=close_window, width=10)

###########################
#         Sign Up         #
###########################
# creates the signup window
window2 = Window(app, title="Sign Up")
window2.set_full_screen()
window2.hide()
toptxt = Text(window2, text="                      ")
toptxt2 = Text(window2, text="    Please enter details:  ", size=15)
toptxt = Text(window2, text="                      ")
# i have made the layour a grid so it can look how i wanted it to.
box1 = Box(window2, layout="grid")
#firstname
blanktxt2 = Text(box1, text="               ", grid=[1,0])
txt2 = Text(box1, text="Username:", align = "left", grid=[0,0])
txtbox2 = TextBox(box1, hide_text=False, align="left", grid=[2,0], width=20)
#secondname
blanktxt3 = Text(box1, text="                       ", grid=[1,1])
txt3 = Text(box1, text="Forename:", align = "left", grid=[0,1])
txtbox3 = TextBox(box1, hide_text=False, width=20, height= "fill", grid=[2,1])
#email
blanktxt4 = Text(box1, text="                       ", grid=[1,2])
txt4 = Text(box1, text="Surname: ",   align = "left", grid=[0,2])
txtbox4 = TextBox(box1, hide_text=False, width=20, height= "fill", grid=[2,2])
#dateofbirth
blanktxt5 = Text(box1, text="                       ", grid=[1,3])
txt5 = Text(box1, text="Email: ",    align = "left", grid=[0,3])
txtbox5 = TextBox(box1, hide_text=False, width=20, height= "fill",grid=[2,3])
#username
blanktxt6 = Text(box1, text="                       ", grid=[1,4])
txt6 = Text(box1, text="Date of Birth: ",   align = "left", grid=[0,4])
txtbox6 = TextBox(box1, hide_text=False, width=20, height= "fill",grid=[2,4])
#password
blanktxt7 = Text(box1, text="                       ", grid=[1,5])
txt7 = Text(box1, text="Password: ",    align = "left", grid=[0,5])
txtbox7 = TextBox(box1, hide_text=True, width=20, height= "fill",grid=[2,5])
#confirming password
blanktxt8 = Text(box1, text="                       ", grid=[1,6])
txt8 = Text(box1, text="Verify Password: ",    align = "left", grid=[0,6])
txtbox8 = TextBox(box1, hide_text=True, width=20, height= "fill",grid=[2,6])
# buttons to navigate page
textblank = Text(window2, text=" ")
doneski_button = PushButton(window2, text="Done", command=done_button_clicked_signup, width=15)
close_button = PushButton(window2, text="Back", command=close_window2, width=15)

##########################################
#         Booking Driving Lessons        #
##########################################
# the notes page is created.
window3 = Window(window, title="Booking Driving Lessons")
window3.set_full_screen()
window3.hide()
# create a box to house the controls, we want the box to span the entire width of the app
blanktext1 = Text(window3,align="top", text="   ")
Texty = Text(window3, align="top",text="Welcome!", size=15)
blanktext1 = Text(window3,align="top", text="   ")
Texty2 = Text(window3, align="top",text="Please book your driving lesson", size=15)
blanktext1 = Text(window3,align="top", text="   ")
Bookingbox1 = Box(window3, layout = "grid", border= True)
Bookingbox2 = Box(Bookingbox1, border=False, grid=[0,0], width = "fill", height="fill")
TextA = Text(Bookingbox2, text = "  What will you be driving?", size=14)
blanktext1 = Text(Bookingbox2, text="   ")
buttongroup1 = ButtonGroup(Bookingbox2, options=["Manual","Automatic"])
blanktext1 = Text(Bookingbox2, text="   ")
blanktext1 = Text(Bookingbox2, text="   ")
Bookingbox3 = Box(Bookingbox1, border=False, grid=[1,0], width = "fill", height="fill")
TextB = Text(Bookingbox3, text = "   Book your Difficulty:    ", size=14)
blanktext1 = Text(Bookingbox3, text="   ")
buttongroup4 = ButtonGroup(Bookingbox3, options=["Easy","Medium", "Hard"])
blanktext1 = Text(Bookingbox3, text="   ")
Bookingbox4 = Box(Bookingbox1, border=False, grid=[0,1], width = "fill", height="fill")
TextC = Text(Bookingbox4, text = " Do you need to borrow ", size=14)
blanktext1 = Text(Bookingbox4, text="  a car? ",  size=14)
blanktext1 = Text(Bookingbox4, text="   ")
buttongroup2 = ButtonGroup(Bookingbox4, options=["Yes, I need one","No, I have one"])
blanktext1 = Text(Bookingbox4, text="   ")
blanktext1 = Text(Bookingbox4, text="   ")

Bookingbox5 = Box(Bookingbox1, border=False, grid=[1,1], width = "fill", height="fill")
TextD = Text(Bookingbox5, text = "Who do you want to teach you?", size=14)
Bookingbox6 = Box(Bookingbox5, border=False, layout = "grid")
Picture1 = Picture(Bookingbox6, image="Peter.png", grid=[0,0])
Picture2 = Picture(Bookingbox6, image="StanSmith.png", grid=[1,0])
Picture3 = Picture(Bookingbox6, image="WalterWhite.png", grid=[2,0])
buttongroup3 = ButtonGroup(Bookingbox5, options=["Peter Griffin","Stan Smith", "Walter White"], horizontal=True)
blanktext1 = Text(Bookingbox5, text="   ")
Bookingbox7 = Box(Bookingbox1, border=False, grid=[0,2], width = "fill", height="fill")

TextE = Text(Bookingbox7, text = "   Lesson Dates Avaliable: ", size=14)
combo = Combo(Bookingbox7, options=["05/10/2021", "06/10/2021", "07/10/2021","08/10/2021","09/10/2021","10/10/2021"])
blanktext1 = Text(Bookingbox7, text="   ")
Bookingbox8 = Box(Bookingbox1, border=False, grid=[1,2], width = "fill", height="fill")
TextF = Text(Bookingbox8, text = "          Lesson times avaliable:            ", size=14)
combo2 = Combo(Bookingbox8, options=["9:30-10:30 AM", "11:00-12:00 AM", "1:00-2:00 PM","2:00-3:00 PM","3:00-4:00 PM","4:00-5:00 PM"])
blanktext1 = Text(Bookingbox8, text="   ")
logoutbuttonwindow3 = PushButton(window3, text="Logout", command=LogoutButtonClicked, width=15)
BookButton = PushButton(window3, text="Book", command=BookButtonClicked, width=15)
CalenderButton = PushButton(window3, text="Already Booked", command=CalenderButtonClicked, width=15)
Window5Button = PushButton(window3, text="My new page", command=newpage)
###########################################
#        Calender of Booked Lessons       #
###########################################
window4 = Window(window, title="Already Booked")
window4.set_full_screen()
window4.hide()
# create a box to house the controls, we want the box to span the entire width of the app
blanktext1 = Text(window4,align="top", text="   ")
Texty2 = Text(window4, align="top",text="These are your previous bookings:", size=15)
blanktext1 = Text(window4,align="top", text="   ")
myBooked = PushButton(window4, text="Show My Bookings", command=ShowMyButtonClicked, width=15)
blanktext1 = Text(window4,align="top", text="   ")
button = PushButton(window4, text="Back", command=backbutton)
###########################################
#                New Page                 #
###########################################
window5 = Window(window, title="Gifs be like")
window5.set_full_screen()
window5.hide()
window5.bg = "light green"
my_waffle = Waffle(window5)
my_waffle[2,1].color = "green"

# Your waffle will remember what colour each pixel is
print(my_waffle[2,1].color)

# Even the ones auto-set at the start (which are white by default)
print(my_waffle[1,1].color)



########################################
#         Calling the Database         #
########################################
####

# this bit of code called the functions that delete the existing database named booking, and then create a brand new one using the sql in files and by calling these functions
delete_db("DrivingLessons.db")
init_db("DrivingLessons.db", "CreateDatabase2.sql")
insert_data("DrivingLessons.db", "InsertSQL2.sql")


# app display should always be shown or the gui will not work and wont display anything.
app.display()

