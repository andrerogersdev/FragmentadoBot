import os
import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

Edge_profile = 'user-data-dir=C:\\Users\\Allya\\AppData\\Local\\MicrosoftEdge\\User\\WhatsPerfil'
opt = webdriver.EdgeOptions()
opt.add_argument(Edge_profile) 
opt.add_argument("--window-size=1366,768")
opt.add_argument('--mute-audio')
#opt.add_argument('--headless')
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=opt)

driver.get('https://web.whatsapp.com')
sleep(1)

def clicar(tipo,valor,valordovalor):
    while True:
        try:
            a = driver.find_element("xpath",f"//{tipo}[contains(@{valor},'{valordovalor}')]")
            a.click()
        except:
            print("não encontrado, esperando 1 segundo.")
            sleep(1)
        else:
            print("clicado com sucesso!")
            break
while True:
    pasta_fotos = "C:\\Users\\Allya\\OneDrive\\Documentos\\programacao\\Trocar_Foto_auto\\eu"
    arquivos = os.listdir(pasta_fotos)
    clicar("div","aria-label","foto do perfil")
    print("clicado no bonequinho")
    sleep(2)
    while True:
        for arquivo in arquivos:
            sleep(2)
            clicar("img","class","_ao3e")
            print("clicado na camera")
            sleep(1)
            clicar("div","aria-label","Carregar foto")
            print("clicado em colocar foto")
            sleep(1)
            caminho_completo = os.path.join(pasta_fotos, arquivo)
            sleep(1)
            pyautogui.write(caminho_completo)
            sleep(1)
            pyautogui.press('enter')
            sleep(1)
            for c in range(0,4):
                clicar("span","data-icon","minus")
                sleep(0.1)
            sleep(2)
            clicar("span","data-icon","checkmark-large")
            sleep(5)
    
        


    