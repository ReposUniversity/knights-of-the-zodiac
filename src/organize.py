import json

# Função para ler o arquivo JSON
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

# Função para salvar o arquivo JSON
def save_json_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Arquivo reorganizado salvo como {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função principal para ordenar os episódios
def sort_episodes():
    # Lê o arquivo JSON
    episodes = read_json_file('videoData.json')
    if not episodes:
        return

    # Ordena os episódios pelo número do episódio extraído do título
    episodes.sort(key=lambda x: int(''.join(filter(str.isdigit, x['title']))))

    # Salva o arquivo JSON reorganizado
    save_json_file('sorted_videoData.json', episodes)

# Chama a função principal
sort_episodes()
