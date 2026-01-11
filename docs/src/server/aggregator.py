import socket
import mysql.connector

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'user': 'votre_utilisateur',
    'password': 'votre_password',
    'database': 'dlc_logs'
}

def save_log(hostname, ip, level, message, source):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # 1. Vérifier/Ajouter le host
        cursor.execute("INSERT IGNORE INTO remote_hosts (hostname, ip_address) VALUES (%s, %s)", (hostname, ip))
        cursor.execute("SELECT id FROM remote_hosts WHERE hostname = %s", (hostname,))
        host_id = cursor.fetchone()[0]
        
        # 2. Insérer le log
        query = "INSERT INTO logs_archive (host_id, log_level, message, log_source) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (host_id, level, message, source))
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erreur DB: {e}")

# Serveur Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen(5)
print("Aggregator DLC en attente sur le port 5000...")

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode('utf-8')
    if data:
        # Format attendu: HOSTNAME|LEVEL|SOURCE|MESSAGE
        parts = data.split('|')
        if len(parts) >= 4:
            save_log(parts[0], addr[0], parts[1], parts[3], parts[2])
    client.close()
