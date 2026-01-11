-- Création de la base de données
CREATE DATABASE IF NOT EXISTS dlc_logs;
USE dlc_logs;

-- Table pour enregistrer les machines clientes (nœuds)
CREATE TABLE IF NOT EXISTS remote_hosts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL UNIQUE,
    ip_address VARCHAR(45) NOT NULL,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table principale pour le stockage des logs
CREATE TABLE IF NOT EXISTS logs_archive (
    id INT AUTO_INCREMENT PRIMARY KEY,
    host_id INT,
    log_level ENUM('INFO', 'WARN', 'ERROR') NOT NULL,
    message TEXT NOT NULL,
    log_source VARCHAR(255), -- ex: /var/log/syslog
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (host_id) REFERENCES remote_hosts(id)
);

-- Index pour accélérer les recherches par niveau et par date
CREATE INDEX idx_log_level ON logs_archive(log_level);
CREATE INDEX idx_created_at ON logs_archive(created_at);
