from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Função para aguardar um tempo
def sleep(seconds):
    time.sleep(seconds)

# Função para acessar a página e extrair os links de vídeo e títulos
def extract_video_data():
    print("Iniciando o navegador...")

    # Inicializando o driver do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Caso queira rodar sem a interface gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Usando o WebDriver Manager para gerenciar a versão do ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://archive.org/details/law-order-1990-s-01-e-09-indifference-720p-web-dl-x-265-im-e_202401/Law+%26+Order+(1990)+-+S01E01+-+Prescription+for+Death+(720p+WEB-DL+x265+ImE).mp4")
    print("Acessando a URL...")
    sleep(5)  # Espera a página carregar completamente

    print("Extraindo dados dos vídeos...")
    sleep(1)  # Espera 1 segundo para garantir que os links sejam carregados

    # Extrai os links dos vídeos e títulos
    video_links = []
    items = driver.find_elements(By.CSS_SELECTOR, '.js-play8-play-track')  # Seletor dos links dos vídeos

    for item in items:
        item.click()
        time.sleep(3)
        title = item.text.strip().split('\n')[1]
        video_element = driver.find_element(By.CSS_SELECTOR, 'video')
        video_url = video_element.get_attribute('src') 
        url = item.get_attribute('href')
        print(f"{title} - URL do vídeo: {video_url}")

        if video_url:
            video_links.append({"title": title, "url": url, "videoUrl": video_url})

    print(f"Dados extraídos com sucesso: {len(video_links)} vídeos encontrados.")
    driver.quit()  # Fecha o navegador

    return video_links

# Função principal para pegar os dados e salvar no arquivo JSON
def scrape_data():
    print("Iniciando a extração dos dados...")
    video_links = extract_video_data()  # Extrai os links e títulos

    print("Salvando os dados em um arquivo JSON...")
    # Salva os dados em um arquivo JSON
    with open('videoData.json', 'w') as f:
        json.dump(video_links, f, indent=2)
    print("Dados salvos em videoData.json")

# Chama a função principal para iniciar o scraping
scrape_data()
