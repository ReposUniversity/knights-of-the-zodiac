from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, json

# Configuração do ChromeOptions para ignorar erros de certificado SSL
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")  # Opcional: para abrir em modo anônimo

# Configuração do WebDriver com as opções
driver = webdriver.Chrome(options=chrome_options)

def extract_video_data():
    base = "https://43.251.84.25:8080/TVSeries/EnglishTVSeries/Law%20and%20Order/Season%20"
    video_links = []
    for i in range(1, 20):
        value = i < 10 and "0" + str(i) or str(i)
        driver.get(base + value + "/")

        # Esperar a página carregar
        time.sleep(5)

        

        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Encontrados {len(links)} links na página.")

        for link in links:
            title = link.text
            link = link.get_attribute("href")
            print(f"Link: {link} - Título: {title}")

            video_links.append({"title": title, "url": link, "videoUrl": link})
    
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
