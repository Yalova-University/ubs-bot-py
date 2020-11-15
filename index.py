from selenium import webdriver
import pymysql.cursors
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
conn  = pymysql.connect(host='localhost',
user='root',
password='',
db='ubs',
autocommit=True,
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
user="202106015"
password="acumk6001**"
print("Sayfayı Açmak İçin 1e Basınız")

sec1 = int(input())
if(sec1 == 1):
    browser = webdriver.Chrome(executable_path=r"C:\Users\umutk\Desktop\Ubs-Bot\ubs-bot-py\chromedriver.exe")
    browser.get('http://ubs.yalova.edu.tr/AIS/Student/OnlineClass/Index?sapid=f42ee5559b93438d')
    
    elem = browser.find_element_by_name('username')
    elem.clear()
    elem.send_keys("202106015")
    elem = browser.find_element_by_name('password')
    elem.clear()
    elem.send_keys("acumk6001**")
    print("Verileri Çekmek İçin 2 ye Basınız")
    sec2 = int(input())
    if(sec2 == 2):
        element = browser.find_elements_by_xpath("//*[@id='body-container']/div/div/div/div/div/div/div/ul/li/div")
        for item in element:
            e = item.text
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO dersler(dersler_icerik) VALUES (%e)")


            finally:
                conn.close()

             