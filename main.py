# coding=utf-8
import os
import pause
from pywinauto.application import Application
from selenium import webdriver
import pywinauto, cv2
import time
import subprocess
import pyautogui
import pygetwindow as gw
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from datetime import datetime as date


# opens and checks for the webex app
webexcheck = subprocess.check_output('tasklist', shell=True)

print ("Made by:" + Fore.MAGENTA + " github.com/GeorgeTzan :)")
print(" \n " + Fore.RED + "DO NOT USE WHEN GAMING!!" )

def checkwebex():
    for i in webexcheck:
        webexcheck

    while 1 > 0:
        checkwebex()


try:
    if b"ptoneclk.exe" in webexcheck:
        webexapp = gw.getWindowsWithTitle('Cisco Webex Meetings')[0]
        webexapp.maximize()
        webexapp.minimize()
        webexapp.close()

    else:
        app = Application(backend="uia").start(r'C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe')
        pause.seconds(2)
        webexapp = gw.getWindowsWithTitle('Cisco Webex Meetings')[0]
        pause.seconds(1)
        webexapp.minimize()
        webexapp.close()
except Exception as e:
    print (e)
    print ("poggers")

check = time.localtime()
current_timecheck = time.strftime("%H:%M:%S", check)
day = date.today().strftime("%A")

# class hours
firstPeriodStart = '08:14:30'
firstPeriodEnd = '08:59:00'
SecondPeriodStart = '09:09:00'
SecondPeriodEnd = '09:54:00'
ThirdPeriodStart = '10:04:00'
ThirdPeriodEnd = '10:49:00'
FourthPeriodStart = '10:59:00'
FourthPeriodEnd = '11:39:00'
FifthPeriodStart = '11:44:00'
FifthPeriodEnd = '12:24:00'
SixthPeriodStart = '12:29:00'
SixthPeriodEnd = '13:09:00'
SeventhPeriodStart = '13:09:10'
SeventhPeriodEnd = '13:49:00'

# breaks
breakpreSchoolStart = '05:00:00'
breakpreSchoolEnd = '08:13:50'

breakTimeStart = '09:00:00'
breakTimeEnd = '09:09:50'  # prwth wra ^
breakTime2Start = '09:54:00'
breakTime2End = '10:04:30'  # deuteri wra ^
breakTime3Start = '10:49:00'
breakTime3End = '10:59:50'  # trith wra ^
breakTime4Start = '11:39:00'
breakTime4End = '11:44:55'  # tetarth wra ^
breakTime5Start = '12:24:05'
breakTime5End = '12:29:05'  # pempth wra ^
#breakTime6Start = '13:09:00'
#breakTime6End = '13:00:00'  # ekth wra ^


# mouse movement & clicks
def clicks():
    chromeWebexENG = pyautogui.locateOnScreen(r"C:\AutoWebex\Images\chromeCheckBox.PNG")
    pyautogui.moveTo(chromeWebexENG)
    pyautogui.click()
        
    chromeWebexRun = pyautogui.locateOnScreen(r"C:\AutoWebex\Images\runWebexChromeENG.PNG")
    pyautogui.moveTo(chromeWebexRun)
    pyautogui.click()

    try:
        os.system("taskkill /f /im chrome.exe")

    except:
        pass
    os.system("taskkill /f /im chromedriver.exe")
    webex = pywinauto.Desktop(backend="uia").window(title="Cisco Webex Meetings")
    webex.wait('visible')

    ciscoConnect = pyautogui.locateOnScreen(r'C:\AutoWebex\Images\joinMeeting.PNG')
    pyautogui.moveTo(ciscoConnect)
    pyautogui.click()




# mouse movement and clicks to leave class
def disconnect():
    try:
        webexatm = gw.getWindowsWithTitle('Cisco Webex Meetings')[0]
        webexatm.maximize()
    except:
        pass
    #1.97657394
    try:
        ciscoDisconnect = pyautogui.locateOnScreen(r'C:\AutoWebex\Images\disconnect.PNG')
        pyautogui.moveTo(ciscoDisconnect)
        pyautogui.click()

        ciscoConfDisc = pyautogui.locateOnScreen(r'C:\AutoWebex\Images\confirmDisconnect.PNG')
        pyautogui.moveTo(ciscoConfDisc)
        pyautogui.click()
    except:
        print ("Webex not found")


# Class links
basikathemata = 'https://minedu-secondary2.webex.com/meet/mich1'
pwlhseis = 'https://minedu-secondary2.webex.com/meet/vraxenidis'
agglika = 'https://minedu-secondary2.webex.com/meet/mkalogiann'
istotopoi = 'https://minedu-secondary2.webex.com/meet/sathanasiou'
python = "https://minedu-secondary2.webex.com/meet/mich1"
mathematika = 'https://minedu-secondary2.webex.com/meet/kxenitidis'
glwssa = 'https://minedu-secondary2.webex.com/meet/despkarydi'
leitourgika = 'https://minedu-secondary2.webex.com/meet/nsivakis'
ylikonduktia = 'https://minedu-secondary2.webex.com/meet/nsivakis'
chemistry = 'https://minedu-secondary2.webex.com/meet/mgkosiou'
fysikh = 'https://minedu-secondary2.webex.com/meet/ggerakaki'
religion = 'https://minedu-secondary2.webex.com/meet/panandread'
gym = 'https://minedu-secondary2.webex.com/meet/xakoustou'
eisagwgh = 'https://minedu-secondary2.webex.com/meet/mich1'

print(day)

browser_location = "C:\AutoWebex\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--lang=en')

# loop wste na trexei gia panta // Loop so it runs forever
run = True
while run:
    # gets day & time
    check = time.localtime()
    current_timecheck = time.strftime("%H:%M:%S", check)
    day = date.today().strftime("%A")
    print(current_timecheck)
    if day == 'Monday' and firstPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(basikathemata)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 55, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Monday' and breakTime2Start <= current_timecheck <= breakTime2End:
        print("Διάλειμμα//break")
        pause.seconds(5)
        continue

    elif day == 'Monday' and ThirdPeriodStart <= current_timecheck <= ThirdPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(ylikonduktia)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 10, 50, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Monday' and breakTime3Start <= current_timecheck <= breakTime3End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Monday' and FourthPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(basikathemata)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 11, 40, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Monday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Monday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(agglika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 12, 45, 05, 00))
        disconnect()
        pause.seconds(3)
        continue
    
    elif day == 'Monday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Monday' and SixthPeriodStart <= current_timecheck <= SixthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(mathematika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 10, 00, 00))
        disconnect()
        pause.seconds(3)
        continue
    
    elif day == 'Monday' and SeventhPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(glwssa)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 50, 05, 00))
        disconnect()
        pause.seconds(3)
        run = False
        
    # Tuesday

    elif day == 'Tuesday' and firstPeriodStart <= current_timecheck <= firstPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(python)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 00, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Tuesday' and breakTimeStart <= current_timecheck <= breakTimeEnd:
        print("Διάλειμμα")
        pause.seconds(5)
        continue

    elif day == 'Tuesday' and SecondPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(pwlhseis)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 55, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Tuesday' and breakTime2Start <= current_timecheck <= breakTime2End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Tuesday' and ThirdPeriodStart <= current_timecheck <= ThirdPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(religion)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 10, 50, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Tuesday' and breakTime3Start <= current_timecheck <= breakTime3End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Tuesday' and FourthPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(chemistry)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 11, 40, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Tuesday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Tuesday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(leitourgika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 12, 25, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Tuesday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Tuesday' and SixthPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(istotopoi)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 50, 05, 00))
        disconnect()
        pause.seconds(2)
        run = False
        
    # Wednesday
    elif day == 'Wednesday' and firstPeriodStart <= current_timecheck <= firstPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(glwssa)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 00, 05, 00))
        disconnect()
        continue
    
    elif day == 'Wednesday' and breakTimeStart <= current_timecheck <= breakTimeEnd:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Wednesday' and SecondPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(leitourgika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 55, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Wednesday' and breakTime2Start <= current_timecheck <= breakTime2End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Wednesday' and ThirdPeriodStart <= current_timecheck <= ThirdPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(mathematika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 10, 50, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Wednesday' and breakTime3Start <= current_timecheck <= breakTime3End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Wednesday' and FourthPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(basikathemata)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 11, 40, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Wednesday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Wednesday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(fysikh)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 12, 25, 00, 00))
        disconnect()
        pause.seconds(1)
        continue
    
    elif day == 'Wednesday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Wednesday' and SixthPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(ylikonduktia)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 50, 00, 00))
        disconnect()
        pause.seconds(1)
        run = False

    # Thursday
    elif day == 'Thursday' and firstPeriodStart <= current_timecheck <= ThirdPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(python)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 10, 50, 00, 00))
        disconnect()
        continue
    
    elif day == 'Thursday' and breakTime3Start <= current_timecheck <= breakTime3Start:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Thursday' and FourthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(pwlhseis)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 12, 25, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Thursday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Thursday' and SixthPeriodStart <= current_timecheck <= SixthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get('https://minedu-secondary2.webex.com/meet/nsivakis')
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 10, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Thursday' and SeventhPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(agglika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 50, 05, 00))
        disconnect()
        pause.seconds(2)
        run = False
        
    # Friday
    elif day == 'Friday' and firstPeriodStart <= current_timecheck <= firstPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(glwssa)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 00, 05, 00))
        disconnect()
        continue
    
    elif day == 'Friday' and breakTimeStart <= current_timecheck <= breakTimeEnd:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Friday' and SecondPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(gym)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 9, 55, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Friday' and breakTime2Start <= current_timecheck <= breakTime2End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Friday' and ThirdPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(istotopoi)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 11, 40, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Friday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Friday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(leitourgika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 12, 25, 05, 00))
        disconnect()
        pause.seconds(2)
        continue
    
    elif day == 'Friday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    
    elif day == 'Friday' and SixthPeriodStart <= current_timecheck <= SixthPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(eisagwgh)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 09, 55, 00))
        disconnect()
        pause.seconds(1)
        continue
    
    elif day == 'Friday' and SeventhPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=browser_location, options=options)
        type(browser)
        browser.get(mathematika)
        clicks()
        pause.until(date(check.tm_year, check.tm_mon, check.tm_mday, 13, 50, 05, 00))
        disconnect()
        pause.seconds(1)
        run = False
        
    elif day == 'Saturday' or day == 'Sunday' and firstPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        print("It's Weekend")
    else:
        print("School Break or no School today")
        pause.seconds(5)
        continue

