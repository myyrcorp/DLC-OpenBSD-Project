#!/bin/bash

# Script d'installation du système DLC pour Ubuntu/Kali
echo "--- Initialisation de l'installation du DLC ---"

# 1. Mise à jour du système
sudo apt update && sudo apt upgrade -y

# 2. Installation des dépendances Serveur (LAMP Stack)
echo "Installation d'Apache, MySQL et PHP..."
sudo apt install -y apache2 mariadb-server php libapache2-mod-php php-mysql

# 3. Installation des dépendances Python pour l'Agent et l'Aggregator
echo "Installation de Python et du connecteur MySQL..."
sudo apt install -y python3 python3-pip
pip3 install mysql-connector-python

# 4. Configuration de la Base de Données
echo "Configuration de MariaDB..."
sudo systemctl start mariadb
# Importation du schéma SQL que vous avez créé dans src/
if [ -f "../src/database.sql" ]; then
    sudo mariadb < ../src/database.sql
    echo "Base de données dlc_logs créée avec succès."
else
    echo "Attention : src/database.sql non trouvé."
fi

# 5. Configuration des permissions pour l'interface Web
echo "Configuration d'Apache..."
sudo cp -r ../src/web/* /var/www/html/
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 755 /var/www/html/

echo "--- Installation terminée ! ---"
echo "Accédez à l'interface sur http://localhost/"
