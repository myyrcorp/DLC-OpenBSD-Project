import socket
import time
import os

# Configuration
SERVER_IP = '127.0.0.1'  # Remplacez par l'IP de votre serveur central
SERVER_PORT = 5000
HOSTNAME = socket.gethostname()
BUFFER_FILE = '/tmp/dlc_buffer.log'

def send_to_server(message):
    """Tente d'envoyer un message au serveur central."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2) # Timeout court pour détecter rapidement une panne
        sock.connect((SERVER_IP, SERVER_PORT))
        sock.sendall(message.encode('utf-8'))
        sock.close()
        return True
    except:
        return False

def process_buffer():
    """Vérifie si des logs sont en attente dans le buffer et tente de les envoyer."""
    if os.path.exists(BUFFER_FILE):
        print("Tentative de vidage du buffer local...")
        with open(BUFFER_FILE, 'r') as f:
            lines = f.readlines()
        
        remaining_lines = []
        for line in lines:
            if send_to_server(line.strip()):
                continue
            else:
                remaining_lines.append(line)
        
        # Mise à jour du buffer avec ce qui n'a pas pu être envoyé
        if not remaining_lines:
            os.remove(BUFFER_FILE)
        else:
            with open(BUFFER_FILE, 'w') as f:
                f.writelines(remaining_lines)

def collect_log(level, source, message):
    """Prépare et envoie le log ou le stocke localement en cas d'échec."""
    log_data = f"{HOSTNAME}|{level}|{source}|{message}"
    
    if send_to_server(log_data):
        print(f"Log envoyé : {message}")
        process_buffer() # Si la connexion est revenue, on traite le buffer
    else:
        print(f"Échec connexion. Log stocké localement dans {BUFFER_FILE}")
        with open(BUFFER_FILE, 'a') as f:
            f.write(log_data + '\n')

# Exemple d'utilisation (simulation de surveillance de fichier)
if __name__ == "__main__":
    print(f"Agent DLC démarré sur {HOSTNAME}...")
    # Simulation : Envoi d'un log de test
    collect_log('INFO', '/var/log/syslog', 'Démarrage du service de collecte')
    
    # Dans un cas réel, vous utiliseriez une boucle qui lit /var/log/syslog
