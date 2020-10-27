import requests
import os
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Login:    
    #saves each line from form in a list
    def read_schedule(self):
        try:
            #os.chdir("..")
            script_dir = os.path.abspath(os.curdir) #<-- absolute dir the script is in
            rel_path = "login_and_schedule.txt"
            abs_file_path = os.path.join(script_dir, rel_path)
            file = open(abs_file_path)
            self.user_info = [None]*2
            self.schedule_info = [[0] for i in range(6)]     #multi dimensional array for multiple logins in a day(limit 2)
            self.timeArr = [[] for i in range(6)]
            self.currDay = datetime.today().weekday()  #returns index/weekday num

            for indx, val in enumerate(file):
                if indx == 0 or val == "\n":
                    continue
                if indx < 4:
                    self.user_info[indx-1] = val.replace(" ","").strip()
                    continue
                self.schedule_info[indx-4][0] = val.replace(" ","").strip()     #subtract 4 from indx to account for usrnm, pwrd, etc
        except:
            print("Failed to open login and schedule file")


    """Note: cant be a counter timer cause if program is shut off it will throw it out of wack.
    use the weekday names to set the timer"""
    def trim_schedule(self):
        #trims username and password fields
        for indx,x in enumerate(self.user_info[0]):
            if(x == ':'):
                self.user_info[0] = (self.user_info[0][indx+1:]).strip()
                break

        for indx, x in enumerate(self.user_info[1]):
            if(x==':'):
                self.user_info[1] = (self.user_info[1][indx+1:]).strip()
                break

        #trims schedule from text file
        for x in range(6):
            for indx, i in enumerate(self.schedule_info[x]):
                if i.find(':') != -1:
                    self.schedule_info[x][indx] = i[(i.find(':'))+1:]   #trims the first colon after the weekday
                    if i.find(',')!= -1:
                        self.schedule_info[x][indx] = i[i.find(':')+1: i.find(',')]
                        j = i[i.find(',')+1:]
                        self.schedule_info[x].append(j)
                        break
                    continue

    #converts the string schedule to a an array of type datetime
    def strArr_to_timeArr(self):
        for indx, x in enumerate(range(6)):
            for i in self.schedule_info[x]:
                if i == '':
                    continue
                date = datetime.strptime(i[:i.find('-')], "%H:%M")  #string to military hour and minute
                date = date.strftime("%I:%M %p")                    #military hour and min to formatted normal time
                self.timeArr[indx].append(datetime.strptime(date, "%I:%M %p"))

                date = datetime.strptime(i[i.find('-')+1 :], "%H:%M")
                date = date.strftime("%I:%M %p")
                self.timeArr[indx].append(datetime.strptime(date, "%I:%M %p"))

    #This function is called to take the difference between each clock_in/clock_out
    #with the number returned a timer will be set up to either clock in or clock out
    #We will have to call this after every clock in or clock out
    #set this function as recursive?
    def execution_timer(self):
        if len(self.timeArr[self.currDay]) == 0:
            self.countdown = datetime(datetime.now().year, datetime.now().month, datetime.now().day+1) - datetime.now()
            print("No shift today.\nBot is sleeping...")
            time.sleep(self.countdown.seconds)
            self.currDay += 1
            return

        for shift in self.timeArr[self.currDay]:           #navigates to current day of week     CHANGE 1  tO currDay
            #check for no shift on current day
            
            if shift.time() < datetime.now().time():
                continue
            else:
                self.countdown = datetime.combine(datetime.today(), shift.time()) - datetime.combine(datetime.today(), datetime.now().time())
                print(self.countdown.seconds)
                print("Time left before next clock-in/clock-out", self.countdown)
                print("Bot is sleeping....")
                time.sleep(self.countdown.seconds)                     #sleeps program until execution
                self.sign_in()
                print("Bot has clocked-in/clocked-out")
                break
        #endshift = time.sleep(datetime.hour(24) - datetime.now().time())
        #print("End of shift. Program will now sleep for ", endshift)
        #print(type(endsx))
        self.currDay += 1



    #logs in with list and clocks in depending on schedule
    def sign_in(self):
        driver = webdriver.Firefox()
        driver. get('https://ccp.mywconline.com/')
        driver.find_element_by_name('username').send_keys(self.user_info[0])
        driver.find_element_by_name('password').send_keys(self.user_info[1])
        driver.find_element_by_name('scheduleid').click()
        driver.find_element_by_name('login').click()
        driver.find_element_by_class_name('tooltip3b').click()
        try:
            driver.find_element_by_name('submit').click()
            print("Clocked-in/Clocked-out")
        except:
            print("Failed")

        time.sleep(10)
        driver.close()

if __name__=='__main__':
    login = Login()
    login.read_schedule()
    login.trim_schedule()
    login.strArr_to_timeArr()
    while True:
        login.execution_timer()

#add exit program feature/ctrl + c
