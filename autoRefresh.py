from selenium import webdriver
import time
import os

# Caminho do seu driver do navegador (Microsoft EdgeDriver)
driver_path = 'C:\\Users\\bruno.pisciotta\\Desktop\\edgedriver_win64\\msedgedriver.exe'

# Adicionar o caminho do driver ao PATH
os.environ['PATH'] += ';' + os.path.dirname(driver_path)

# URL da página que você deseja atualizar
url = 'https://github.com/bruno-pisciotta281/bruno-pisciotta281/blob/main/README.md'

# Configurações do navegador
options = webdriver.EdgeOptions()
options.add_argument('--headless')  # Isso permite que o navegador funcione em segundo plano (sem interface gráfica)

# Inicializar o driver do navegador
driver = webdriver.Edge(options=options)

# Função para realizar o refresh
def realizar_refresh():
    driver.get(url)
    print(f"Realizando refresh em {url}")
    time.sleep(1)  # Aguarda 3 segundos (ajuste conforme necessário)
    driver.refresh()
    print("Refresh concluído")

# Loop para realizar refresh continuamente
try:
    while True:
        realizar_refresh()
except KeyboardInterrupt:
    print("Interrupção pelo usuário. Fechando o navegador.")
    driver.quit()
