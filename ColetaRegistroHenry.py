# Importando Blibliotecas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import shutil
import os
from datetime import datetime
import sys


# Configurações
catraca_url = "ip de acesso a catraca"


# Configuração do ChromeDriver
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)
#chrome_options.add_argument("--start-minimized")
#chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-web-security")





# Inicializando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Acessar a página da catraca
    driver.get(catraca_url)

    WebDriverWait(driver, 10)

    #Localizando o campo usuario
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lblLogin")))
    username_fields = driver.find_element(By.ID, "lblLogin")

    # Preencher o campo de usuario
    username_fields.send_keys("usuario")

    WebDriverWait(driver, 10)

    # Preencher o campo de senha
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lblPass")))
    username_fields = driver.find_element(By.ID, "lblPass")
    username_fields.send_keys("senha")

    WebDriverWait(driver, 10)

    # Clicar no botão de envio
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick="subComp(1,7,0);"]')))
    submit_button = driver.find_element(By.CSS_SELECTOR, 'a[onclick="subComp(1,7,0);"]')
    submit_button.send_keys(Keys.ENTER)

    # Navegar até a aba de dados    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[onclick="subComp(0, 8, 0);"]')))
    registros_fields = driver.find_element(By.CSS_SELECTOR, 'a[onclick="subComp(0, 8, 0);"]')
    registros_fields.click()

    # Obter a data atual
    data_atual = datetime.now()
    hora_inicial = "00:00"
    hora_final = "23:59"
    data_inicial = data_atual.strftime("%d/%m/%y")+" "+hora_inicial
    data_final = data_atual.strftime("%d/%m/%y")+" "+hora_final

    
    #Preenchendo os campos de data inicial e final
    lblDataI = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lblDataI")))
    lblDataI.clear()
    lblDataI.send_keys(data_inicial)
    time.sleep(2)
    lblDataF = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lblDataF")))
    lblDataF.clear()
    lblDataF.send_keys(data_final)
    time.sleep(2)

    #Fazendo o dowload dos registros com base na data
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[onclick="subCompD(5, 8, 2);"]')))
    download_registro = driver.find_element(By.CSS_SELECTOR, 'a[onclick="subCompD(5, 8, 2);"]').click()

    

    # Aguardar alguns segundos para garantir que o download seja concluído
    time.sleep(6)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[onclick="subComp(2, 7, 0);"]')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[onclick="subComp(2, 7, 0);"]')))
    sair = driver.find_element(By.CSS_SELECTOR, 'a[onclick="subComp(2, 7, 0);"]')
    sair.click()
   

except TimeoutException:
    print("Elementos de autenticação não encontrados ou página de registros não carregada. Verifique se os IDs estão corretos e se a página está carregando corretamente.")

finally:
    # Fechar o navegador
    driver.quit()

# Formatar a data no formato desejado para o nome do arquivo
nome_arquivo = data_atual.strftime("Bilhetes %Y-%m-%d") + ".txt"  # Por exemplo, "Bilhetes 2024-05-09.txt"

#Move o arquivo baixado para pasta de acesso do Sênior

# Especifique o caminho do arquivo baixado e o destino para mover o arquivo
caminho_origem = "origem/eventos_00101220640042018.txt"
caminho_destino = "Destino"

# Verifica se o diretório de destino existe, se não, cria o diretório
if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)

# Move o arquivo para o destino com o novo nome
shutil.move(caminho_origem, os.path.join(caminho_destino, nome_arquivo))

print("Arquivo movido com sucesso!")

time.sleep(2)
sys.exit()