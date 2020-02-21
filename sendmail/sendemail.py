from selenium import webdriver
from pathlib import Path
import pyinputplus as pyip
import sys, os, time
# sends an email to a user specific email address

#clear the command line
os.system('cls' if os.name == 'nt' else 'clear')

# get the users email address    
username = pyip.inputEmail(prompt='Enter your email address: ', limit=3, default='n/a')

# if user doesnt enter a valid email then exit program
if username == 'n/a':
    print('Sorry, you must enter a valid email')
    sys.exit()
    
# get the users password
password = pyip.inputPassword(prompt='Enter you password: ')

# get the email address of the recipient
email_dest = pyip.inputEmail(prompt='Enter an email address destination: ', limit=3, default='n/a')

# if user doesnt enter a valid email then exit program
if email_dest == 'n/a':
    print('Sorry, you must enter a valid email')
    sys.exit()

# get a subject for the email#
subject = pyip.inputStr("Enter a subject: ")

#get the user message
os.system('cls' if os.name == 'nt' else 'clear')
print("Enter the message <press enter twice to finish the message>: ")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
message = '\n'.join(lines)

# set the url
url = 'https://mail.google.com/mail/u/0/#inbox'

# create the driver and began interaction
driver = webdriver.Chrome(r'.\resources\chromedriver.exe')
#driver.implicitly_wait=True
driver.get(url)

xpath = '//*[@id="password"]/div[1]/div/div[1]/input'

# enter the username
driver.find_element_by_id('identifierId').send_keys(username)

# press next
driver.find_element_by_id('identifierNext').click()

#pause to give the browser time to load
time.sleep(3)

# enter the password
driver.find_element_by_name('password').send_keys(password)

# sign in
driver.find_element_by_id('passwordNext').click()

time.sleep(15)
x = '//*[@id=":3n"]/div/div'
#driver.find_element_by_name('q').send_keys("This is a test")
# start a new email
driver.find_element_by_xpath(x).click()
#driver.find_element_by_id(':3l').click()

# enter recipient email
driver.find_element_by_id(':9c').send_keys(email_dest)

# enter a subject
driver.find_element_by_id(':8u').send_keys(subject)

# enter email message
driver.find_element_by_id(':9z').send_keys(message)

# submit email
driver.find_element_by_id(':8k').click()

    