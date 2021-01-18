# coding=utf-8
import os
import pause
from pywinauto.application import Application
from selenium import webdriver
import pywinauto
import time
import subprocess
import pyautogui
import pygetwindow as gw
from datetime import datetime as date

# anoigma kai check toy webex
webexcheck = subprocess.check_output('tasklist', shell=True)


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

    else:
        app = Application(backend="uia").start(r'C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe')
        pause.seconds(2)
        webexapp = gw.getWindowsWithTitle('Cisco Webex Meetings')[0]
        pause.seconds(1)
        webexapp.minimize()
except:
    pass
# wres mathimatwn
check = time.localtime()
current_timecheck = time.strftime("%H:%M:%S", check)
day = date.today().strftime("%A")
firstPeriodStart = '07:59:00'
firstPeriodEnd = '08:39:00'
SecondPeriodStart = '08:50:00'
SecondPeriodEnd = '09:29:00'
ThirdPeriodStart = '09:39:00'
ThirdPeriodEnd = '10:19:00'
FourthPeriodStart = '10:29:00'
FourthPeriodEnd = '11:09:00'
FifthPeriodStart = '11:19:00'
FifthPeriodEnd = '11:59:00'
SixthPeriodStart = '12:09:00'
SixthPeriodEnd = '12:49:00'
SeventhPeriodStart = '12:59:00'
SeventhPeriodEnd = '13:39:00'

#breaks
breakTimeStart = '08:39:00'
breakTimeEnd = '08:50:00' # prwth wra ^
breakTime2Start = '09:29:00'
breakTime2End = '09:38:30' # deuteri wra ^
breakTime3Start = '10:19:00'
breakTime3End = '10:29:55' # trith wra ^
breakTime4Start ='11:10:00'
breakTime4End = '11:19:55' # tetarth wra ^
breakTime5Start = '12:00:00'
breakTime5End = '12:10:00' # pempth wra ^
breakTime6Start = '12:50:00'
breakTime6End = '13:00:00' # ekth wra ^
# mouse movement & clicks
def clicks():
    pyautogui.moveTo(278, 180)
    pyautogui.click()
    pyautogui.moveTo(655, 240)
    pyautogui.click()
    try:
        os.system("taskkill /f /im chrome.exe")

    except:
        pass
    os.system("taskkill /f /im chromedriver.exe")
    webex = pywinauto.Desktop(backend="uia").window(title="Cisco Webex Meetings")
    webex.wait('visible')
    pyautogui.moveTo(820, 673)
    pyautogui.click()


# mouse movement and clicks to leave class
def disconnect():
    try:
        webexatm = gw.getWindowsWithTitle('Cisco Webex Meetings')
        webexatm.maximize()
    except:
        pass
    pyautogui.moveTo(926, 693)
    pyautogui.click()
    pyautogui.moveTo(558, 341)
    pyautogui.click()


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
print(current_timecheck)

# loop wste na trexei gia panta
run = True
while run:

    if day == 'Monday' and firstPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(basikathemata)
        clicks()
        pause.minutes(90)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Monday' and breakTime3Start <= current_timecheck <= breakTime3End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue

    elif day == 'Monday' and ThirdPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(pwlhseis)
        clicks()
        pause.minutes(90)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Monday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Monday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(agglika)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Monday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Monday' and SixthPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(istotopoi)
        clicks()
        pause.minutes(90)
        disconnect()
        pause.seconds(3)
        run = False
    # Tuesday

    elif day == 'Tuesday' and firstPeriodStart <= current_timecheck <= firstPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(python)
        # pause.until(date(2021, 8, 49, 2))
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Tuesday' and breakTimeStart <= current_timecheck <= breakTimeEnd:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue

    elif day == 'Tuesday' and SecondPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(mathematika)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Tuesday' and breakTime2Start <= current_timecheck <= breakTime2End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Tuesday' and ThirdPeriodStart <= current_timecheck <= ThirdPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(glwssa)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Tuesday' and breakTime3Start <= current_timecheck <= breakTime3End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Tuesday' and FourthPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(ylikonduktia)
        # pause.until(datetime(2020, 12, 9, 2))
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Tuesday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Tuesday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(agglika)
        clicks()
        pause.minutes(40)
        # pause.until(datetime(2020, 12, 59, 2))
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Tuesday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Tuesday' and SixthPeriodStart <= current_timecheck <= SixthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(leitourgika)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Tuesday' and breakTime6Start <= current_timecheck <= breakTime6End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Tuesday' and SeventhPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(pwlhseis)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        run = False
    # Wednesday
    elif day == 'Wednesday' and firstPeriodStart <= current_timecheck <= SecondPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(python)
        clicks()
        pause.minutes(90)
        disconnect()
        continue
    elif day == 'Wednesday' and breakTime2Start <= current_timecheck <= breakTime2End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Wednesday' and ThirdPeriodStart <= current_timecheck <= ThirdPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(chemistry)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Wednesday' and breakTime3Start <= current_timecheck <= breakTime3End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Wednesday' and FourthPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get('https://minedu-secondary2.webex.com/meet/nsivakis')
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Wednesday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Wednesday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(fysikh)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Wednesday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print ("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Wednesday' and SixthPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(istotopoi)
        clicks()
        pause.minutes(90)
        disconnect()
        pause.seconds(1)
        run = False

    # Thursday
    elif day == 'Thursday' and firstPeriodStart <= current_timecheck <= firstPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(religion)
        clicks()
        pause.minutes(40)
        disconnect()
        continue
    elif day == 'Thursday' and breakTimeStart <= current_timecheck <= breakTimeEnd:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Thursday' and SecondPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(python)
        clicks()
        pause.minutes(140)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Thursday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Thursday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(glwssa)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Thursday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Thursday' and SixthPeriodStart <= current_timecheck <= SixthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(mathematika)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Thursday' and breakTime6Start <= current_timecheck <= breakTime6End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Thursday' and SeventhPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(ylikonduktia)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(1)
        run = False
    # Friday
    elif day == 'Friday' and firstPeriodStart <= current_timecheck <= firstPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(gym)
        clicks()
        pause.minutes(40)
        # disconnect()
        continue
    elif day == 'Friday' and breakTimeStart <= current_timecheck <= breakTimeEnd:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Friday' and SecondPeriodStart <= current_timecheck <= FourthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(ylikonduktia)
        clicks()
        pause.minutes(140)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Friday' and breakTime4Start <= current_timecheck <= breakTime4End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Friday' and FifthPeriodStart <= current_timecheck <= FifthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(mathematika)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Friday' and breakTime5Start <= current_timecheck <= breakTime5End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Friday' and SixthPeriodStart <= current_timecheck <= SixthPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(glwssa)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(2)
        continue
    elif day == 'Friday' and breakTime6Start <= current_timecheck <= breakTime6End:
        print("Διάλειμμα")
        pause.seconds(5)
        continue
    elif day == 'Friday' and SeventhPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        browser = webdriver.Chrome(executable_path=r'C:\Users\epalelefth\PycharmProjects\AntiQueueBot\chromedriver.exe')
        type(browser)
        browser.get(eisagwgh)
        clicks()
        pause.minutes(40)
        disconnect()
        pause.seconds(1)
        run = False
    elif day == 'Saturday' or day == 'Sunday' and firstPeriodStart <= current_timecheck <= SeventhPeriodEnd:
        print("Einai savvatokuriako Blaka")
    #  break
    else:
        print("break or not currently school day")
        pause.seconds(5)
        continue
