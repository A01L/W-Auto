#include lib's
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import tkinter as tk
import os.path

#create window on tkinter
frame = tk.Tk()
frame.title("WhatsApp Automatic")
frame.geometry('300x100')

#function for start loop
def sending():

    #config files
    nml = open('numbers.txt')
    text = open('message.txt', 'r', encoding='UTF-8')
    msg = text.read()

    #control
    lbl.config(text = "Операция завершена!")
    Button.config(text = "Запускать еще")
    options = webdriver.ChromeOptions()
    options.add_argument('--profiling-flush=n')
    options.add_argument('--enable-aggressive-domstorage-flushing')

    #param
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 30)

    #worker
    for nml in nml:
        url = f"https://web.whatsapp.com/send?phone={nml}&text={msg}"
        driver.get(url)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        sleep(5)

# Label Creation
lbl = tk.Label(frame, text = "Список номеров: numbers.txt \n Файл сообщения: message.txt")
lbl.pack()

#Check config files [numbers.txt, message.txt]
if os.path.isfile('numbers.txt'):
    if os.path.isfile('message.txt'):
        # Button Creation
        Button = tk.Button(frame,
                                text = "Запускать", 
                                command = sending,
                                bg="black",
                                fg="white"
                                )
        Button.pack(fill=tk.X, side=tk.BOTTOM)
    else:
        lbl.config(text = "Файл сообщении не найден [message.txt]!")
else:
    lbl.config(text = "Файл номеров не найден [numbers.txt]!")

#loop for Tkinter
frame.mainloop()