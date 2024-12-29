from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Função para aguardar um tempo
def sleep(seconds):
    time.sleep(seconds)

# Função para acessar a página e extrair os links e títulos
def extract_video_data():
    print("Iniciando o navegador...")

    # Inicializando o driver do Safari
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)

    driver.get("https://archive.org/search?query=subject%3A%22Dic%22+subject%3A%22Cartoon+Network%22+%22Knights+Of+The+Zodiac%22")

    print("Acessando a URL...")
    sleep(20)  # Espera a página carregar completamente

    print("Extraindo dados dos vídeos...")
    # Scroll até o final da página para carregar mais vídeos
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)

    # Extrai os links dos vídeos e títulos
    video_links = []
    items = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label]')
    for item in items:
        title = item.get_attribute('aria-label')
        url = item.get_attribute('href')
        if title and url:
            video_links.append({"title": title, "url": url})

    print(f"Dados extraídos com sucesso: {len(video_links)} vídeos encontrados.")
    driver.quit()  # Fecha o navegador

    return video_links

# Função para acessar cada URL de vídeo, pegar o link do vídeo e organizar os dados
def fetch_video_urls(video_links):
    print("Iniciando o navegador para acessar os URLs dos vídeos...")

    # Inicializando o driver do Safari
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)

    video_data = []

    for video in video_links:
        title = video['title']
        url = video['url']

        print(f"Acessando URL do vídeo: {url}")
        driver.get(url)
        sleep(5)  # Espera o vídeo carregar

        print("Esperando o vídeo ser carregado...")
        # Espera o elemento de vídeo aparecer na página
        video_element = driver.find_element(By.CSS_SELECTOR, 'video')

        print("Extraindo o link do vídeo...")
        video_url = video_element.get_attribute('src')

        video_data.append({"title": title, "url": url, "videoUrl": video_url})
        print(f"Dados do vídeo extraídos: {title}")

    print("Fechando o navegador...")
    driver.quit()  # Fecha o navegador

    print("Todos os dados dos vídeos foram extraídos com sucesso.")
    return video_data

# Função principal para pegar os dados e salvar no arquivo JSON
def scrape_data():
    print("Iniciando a extração dos dados...")
    video_links = extract_video_data()  # Extrai os links e títulos
    video_data = fetch_video_urls(video_links)  # Extrai os links de vídeo

    print("Salvando os dados em um arquivo JSON...")
    # Salva os dados em um arquivo JSON
    with open('videoData.json', 'w') as f:
        json.dump(video_data, f, indent=2)
    print("Dados salvos em videoData.json")

# Chama a função principal para iniciar o scraping
scrape_data()
