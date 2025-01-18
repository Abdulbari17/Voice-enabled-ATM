import speech_recognition as sr 
import pyttsx3 
import sqlite3 
import my_module 
generalList = [] 
data = {} 
email = "" 
pin = "" 
amountValue = 0 
cardOption = "" 
engine=pyttsx3.init() 
voices=engine.getProperty('voices') 
engine.setProperty('voice','voices[0].id') 
conn = sqlite3.connect('datab.db') 
cursor = conn.cursor() 
cursor.execute('''CREATE TABLE IF NOT EXISTS datab 
(Fname char(20), Lname char(20), Uname char(20), 
Emailid char(20), Pin n(5), Balance n(5));''') 
def speak(text): 
    engine.say(text) 
    engine.runAndWait() 
def capture(): 
    """Capture audio"""
    rec = sr.Recognizer() 
with sr.Microphone() as source: 
    rec.adjust_for_ambient_noise(source, duration=0.5) 
    rec.dynamic_energy_threshold = True 
    audio = rec.listen(source,phrase_time_limit=10) 
try: 
    text = rec.recognize_google(audio,language='en-in') 
    return text 
except: 
    text=input() 
return text 
def generallist(): 
    generalOption = capture() 
if generalOption == 3: 
print(generalList) 
rootHome() 
else: 
print("error") 
speak('error') 
def logOut(): 
speak('Thank You for banking with us, have a nice day')
print("Thank You for banking with us, have a nice day.") 
conn = sqlite3.connect('datab.db') 
cursor = conn.cursor() 
cursor.execute('''CREATE TABLE IF NOT EXISTS datab 
(Fname char(20), Lname char(20), Uname char(20), 
Emailid char(20), Pin n(5), Balance n(5));''') 
speak('Welcome enter 1 for login enter 2 for register') 
print("Welcome to ") 
print("1. Login") 
print("2. Register") 
rootHome() 
def moneyOut1(): 
global email 
global pin 
message = "" 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
if int(b) < 10000: 
print("Insufficient Balance") 
speak('Insufficient balance') 
elif int(b) > 10000: 
val=int(b) - 10000 
print("Your #10000 withdrawal was successful.") 
speak('Your 10000 withdrawal was successful') 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
else: 
message = "Transaction error" 
speak(message) 
def moneyOut2():
global email 
global pin 
message = "" 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
if int(b) < 5000: 
print("Insufficient Balance") 
speak('Insufficient balance') 
elif int(b) > 5000: 
val=int(b) - 5000 
print("Your #5000 withdrawal was successful.") 
speak("Your #5000 withdrawal was successful.") 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
else: 
message = "Transaction error" 
speak(message) 
def moneyOut3(): 
global email 
global pin 
message = "" 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
if int(b) < 2000: 
print("Insufficient Balance") 
speak('Insufficient balance') 
elif int(b) > 2000: 
val=int(b) - 2000 
print("Your #2000 withdrawal was successful.") 
speak('Your #2000 withdrawal was successful.') 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
else: 
message = "Transaction error" 
speak(message) 
def moneyOut4(): 
global email
global pin 
message = "" 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
if int(b) < 1000: 
print("Insufficient Balance") 
speak('Insufficient balance') 
elif int(b) > 1000: 
val=int(b) - 1000 
print("Your #1000 withdrawal was successful.") 
speak('Your #1000 withdrawal was successful.') 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
else: 
message = "Transaction error" 
speak(message) 
def moneyOut5(): 
global email 
global pin 
message = "" 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
if int(b) < 500: 
print("Insufficient Balance")
speak('Insufficient balance') 
elif int(b) > 500: 
val=int(b) - 500 
print("Your #500 withdrawal was successful.") 
speak('Your #500 withdrawal was successful.') 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
else: 
message = "Transaction error" 
speak(message) 
def moneyOutothers(): 
global email 
global pin 
global amountValue 
message = "" 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
if b < amountValue: 
print("Insufficient Balance") 
speak('Insufficient balance') 
elif b > amountValue:
val=int(b) - amountValue 
print("Your #" + str(amountValue) + " withdrawal was successful.") 
speak('Your'+str(amountValue)+ 'withdrawal was successful') 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
else: 
message = "Transaction error" 
speak(message) 
def withdraw(): 
speak('enter how much you want to withdraw') 
print("How much do you want to withdraw?") 
print("1. 10,000") 
speak('enter 1 for 10000') 
print("2. 5,000") 
speak('enter 2 for 5000') 
print("3. 2,000") 
speak('enter 3 for 2000') 
print("4. 1,000") 
speak('enter 4 for 1000') 
print("5. 500") 
speak('enter 5 for 500') 
print("6. others")
speak('enter 6 for others') 
print("7. Back") 
speak('enter 7 to go back') 
print("Select option: ") 
withdrawOption = capture() 
if withdrawOption == "1" or withdrawOption == 1: 
moneyOut1() 
print("Do you want to perform another transaction?") 
speak('Do you want to perform another transaction?') 
print("1. Yes") 
speak('enter 1 if yes') 
print("2. No") 
speak('enter 2 if no') 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption =="Tu" or 
anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
elif withdrawOption == "2" or withdrawOption =="Tu" or 
withdrawOption ==2:
moneyOut2() 
print("Do you want to perform another transaction?") 
speak('Do you want to perform another transaction?') 
print("1. Yes") 
speak('enter 1 if yes') 
print("2. No") 
speak('enter 2 if no') 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption =="Tu" or 
anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
elif withdrawOption == "3" or withdrawOption =="tree" or 
withdrawOption ==3: 
moneyOut3() 
print("Do you want to perform another transaction?") 
speak('Do you want to perform another transaction?') 
print("1. Yes")
speak('enter 1 if yes') 
print("2. No") 
speak('enter 2 if no') 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
elif withdrawOption == "4" or withdrawOption ==4: 
moneyOut4() 
print("Do you want to perform another transaction?") 
speak('Do you want to perform another transaction?') 
print("1. Yes") 
speak('enter 1 if yes') 
print("2. No") 
speak('enter 2 if no') 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user()
elif anotherOption == "2" or anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
elif withdrawOption == "5" or withdrawOption ==5: 
moneyOut5() 
print("Do you want to perform another transaction?") 
speak('Do you want to perform another transaction?') 
print("1. Yes") 
speak('enter 1 if yes') 
print("2. No") 
speak('enter 2 if no') 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection")
speak('Invalid selection')
elif withdrawOption == "6" or withdrawOption ==6: 
global amountValue 
amountValue = int(input()) 
moneyOutothers() 
print("Do you want to perform another transaction?") 
speak('Do you want to perform another transaction?') 
print("1. Yes") 
speak('enter 1 if yes') 
print("2. No") 
speak('enter 2 if no') 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
elif withdrawOption == "7" or withdrawOption ==7: 
user() 
else: 
print("Invalid selection") 
speak("Invalid selection")
def histroy(): 
global email 
global pin 
message = " " 
message = "Still working on it" 
print(message) 
speak(message) 
speak('Do you want to perform another transaction?') 
print("Do you want to perform another transaction?") 
speak('Enter 1 for yes') 
print("1. Yes") 
speak('enter 2 for no') 
print("2. No") 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection')
def balance(): 
global email 
global pin 
message = "" 
val=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
print("Your current balance is #" + str(val) + ".") 
speak('Your current balance is '+str(val)) 
speak('Do you want to perform another transaction?') 
print("Do you want to perform another transaction?") 
speak('Enter 1 for yes') 
print("1. Yes") 
speak('enter 2 for no') 
print("2. No") 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user() 
elif anotherOption == "2" or anotherOption =="Tu" or 
anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection')
def proceed(): 
global email 
global pin 
#word = "" 
speak('enter receivers mail address') 
print("Enter the receiver's email address: ") 
remail = capture() 
speak('enter amount you want to transfer') 
print("Enter the amount you want to transfer: ") 
amount = capture() 
a=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(email,)).fetchone() 
b=a[0] 
c=conn.execute("SELECT Balance FROM datab WHERE Emailid=?",(remail,)).fetchone() 
d=c[0] 
f=conn.execute("SELECT FNAME FROM datab WHERE Emailid=?",(remail,)).fetchone() 
l=conn.execute("SELECT LNAME FROM datab WHERE Emailid=?",(remail,)).fetchone() 
if int(b)>0 and int(b)>int(amount): 
val=int(b)-int(amount) 
val2=int(d)+int(amount) 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val,email)) 
conn.commit() 
conn.execute("UPDATE datab SET Balance=? WHERE Emailid=?",(val2,remail)) 
conn.commit() 
f=f[0] 
l=l[0] 
mess = "#" + amount + " transfered successfully to " + f + 
" " + l + "." 
else: 
speak('Insufficient balance') 
print("Insufficient balance") 
# else: 
# word = "Insufficient fund" 
# for details in generalList: 
# if(details["Email"] == email): 
# 
# 
details["Balance"] = details["Balance"] + int(amount) 
print("#" + amount + " was transfered successfully to " 
+ email + ".") 
# else: 
# 
message="Invalid account details" 
# for details in generalList: 
# if details["Pin"] == pin: 
# 
# 
#  
# 
# 
details["Balance"] = details["Balance"] - int(amount) 
if details["Balance"] < 0: 
print("Insufficient fund") 
else: 
print("Your current balance is #" + 
str(details["Balance"]) + ".") 
speak('Do you want to perform another transaction?') 
print("Do you want to perform another transaction?") 
speak('Enter 1 for yes') 
print("1. Yes") 
speak('enter 2 for no') 
print("2. No") 
print("Select option: ") 
anotherOption = capture() 
if anotherOption == "1" or anotherOption ==1: 
user()
elif anotherOption == "2" or anotherOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
def trans(): 
speak('enter 1 to proceed enter 2 to go back') 
print("1. Proceed") 
print("2. Back") 
print("Select option: ") 
transOption = capture() 
if transOption == "1" or transOption==1: 
proceed() 
elif transOption == "2" or transOption ==2: 
user() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
def user(): 
global email 
a=conn.execute("SELECT Fname FROM datab where Emailid=?",(email,)).fetchone() 
f=a[0]
b=conn.execute("SELECT Lname FROM datab where Emailid=?",(email,)).fetchone() 
l=b[0] 
print("Welcome " + f + l + ".") 
speak('Welcome ' + f + l ) 
speak('enter 1 for withdraw') 
print("1. Withdraw") 
speak('enter 2 for balance') 
print("2. Balance") 
speak('enter 3 for Transfer') 
print("3. Transfer") 
speak('enter 4 for balance statement') 
print("4. Histroy") 
speak('enter 5 for logout') 
print("5. Log Out") 
print("Select option: ") 
userOption = capture() 
if userOption == "1" or userOption ==1: 
withdraw() 
elif userOption == "2" or userOption ==2: 
balance() 
elif userOption == "3" or userOption ==3: 
trans() 
elif userOption == "4" or userOption ==4: 
histroy() 
elif userOption == "5" or userOption ==5:
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
speak('Invalid selection') 
print("Invalid selection") 
def login(): 
global email 
global pin 
message = "" 
speak('enter your email') 
print("Enter your Email: ") 
email = capture() 
speak('enter your pin') 
print("Enter your Pin: ") 
pin = capture() 
var=cursor.execute("SELECT Pin FROM datab WHERE Emailid=?",(email,),).fetchone() 
var1=var[0] 
print(var1) 
if(int(var1)==int(pin)): 
user() 
else: 
message = "Invalid login details" 
print(message) 
speak(message)
# def access(): 
# if generalList[0]["Email"] == "email" and 
generalList[0]["Pin"] == "pin": 
#  
user() 
# else: 
# 
print("Invalid login details") 
def reg(): 
global data 
data = {} 
print("Enter first name:") 
speak('Enter first name') 
data["First Name"] = capture() 
print(data["First Name"]) 
print("Enter Last Name:") 
speak('Enter last name') 
data["Last Name"] = capture() 
print(data["Last Name"]) 
print("Enter your user name: ") 
speak('Enter user name') 
data["User Name"] = capture() 
print(data["User Name"]) 
print("Enter your email address: ") 
speak('Enter email') 
data["Email"] = capture()
print(data["Email"]) 
print("Enter your pin:") 
speak('Enter pin') 
data["Pin"] = capture() 
print(data["Pin"]) 
print("Enter your balance:") 
speak('Enter balance') 
data["Balance"] = int(capture()) 
print(data["Balance"]) 
data["History"] = [] 
cursor.execute(""" 
INSERT INTO datab 
(Fname,Lname,Uname,Emailid,Pin,Balance) 
VALUES (?,?,?,?,?,?) 
""", (data["First Name"],data["Last Name"],data["User Name"],data["Email"],data["Pin"],data["Balance"])) 
conn.commit() 
var1="User Name" in data 
cursor1=conn.execute("SELECT * FROM datab ORDER BY rowid DESC limit 1") 
for i in cursor1: 
print(i) 
# for details in generalList: 
# if(details["Email"] == data["Email"]): 
#  
print("Used email address, input a new one.") 
# else:
generalList.append(data) 
speak('welcome to your first transaction') 
print("Welcome "+ data["First Name"] + " " + data["Last Name"] +".") 
speak('if you wish to transact enter 1 otherwise enter 2') 
print("Do you wish to transact? ") 
print("1. Yes") 
print("2. No") 
print("Select option: ") 
regOption = capture() 
if regOption == "1" or regOption ==1: 
login() 
elif regOption == "2" or regOption ==2: 
logOut() 
conn.commit() 
cursor.close() 
conn.close() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
def rootHome(): 
homeOption =my_module.capture() 
if homeOption == "1" or homeOption ==1: 
login() 
elif homeOption ==2 or homeOption =="2": 
reg() 
elif homeOption ==3 or homeOption =="3": 
generallist() 
else: 
print("Invalid selection") 
speak('Invalid selection') 
print("Welcome to ") 
speak("welcome") 
speak("enter 1 for login enter 2 for register") 
print("1. Login") 
print("2. Register") 
cursor1=conn.execute("SELECT * FROM datab") 
for i in cursor1: 
print(i) 
rootHome() 
