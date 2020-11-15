from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user="202106015"
password="acumk6001**"
print("Sayfayı Açmak İçin 1e Basınız")
sec1 = int(input())
if(sec1 == 1):
    browser = webdriver.Chrome(executable_path=r"C:\Users\umutk\Desktop\Ubs-Bot\ubs-bot-py\chromedriver.exe")
    browser.get('http://ubs.yalova.edu.tr/AIS/Student/OnlineClass/Index?sapid=f42ee5559b93438d')
