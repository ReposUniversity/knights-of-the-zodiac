import subprocess
import re

# Função para pegar o IP da TV usando ping com o nome da TV
def find_airplay_device(tv_name):
    # Executa o comando ping no nome da TV (exemplo: quarto.local)
    command = f"ping -c 1 {tv_name}"
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Verifica se o ping foi bem-sucedido
        if result.returncode == 0:
            # Extrai o IP do resultado do ping
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', result.stdout.decode())
            if ip_match:
                return ip_match.group(1)
    except Exception as e:
        print(f"Erro ao executar o ping: {e}")
    return None

# Função para rodar o comando ffmpeg com o IP da TV
def send_video_to_airplay(ip, video_url):
    ffmpeg_command = [
        'ffmpeg', 
        '-i', video_url, 
        '-f', 'avi', 
        '-vcodec', 'h264', 
        '-acodec', 'aac', 
        '-f', 'mpegts', 
        f'udp://{ip}:5000'
    ]
    subprocess.run(ffmpeg_command)

# Nome da TV (exemplo: quarto.local)
tv_name = 'quarto.local'

# Encontre o IP do dispositivo AirPlay
ip = find_airplay_device(tv_name)
print(f"Dispositivo AirPlay encontrado: {ip}")

# if ip:
#     video_url = 'https://archive.org/serve/knightsofthezodiac12/Knights%20Of%20The%20Zodiac%201-2.mp4'  # Substitua pela URL do vídeo
#     send_video_to_airplay(ip, video_url)
# else:
#     print("Nenhum dispositivo AirPlay encontrado.")
