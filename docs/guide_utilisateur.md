Guide Utilisateur : Distributed Logs Collector (DLC)
Ce guide détaille les procédures d'installation, de configuration et d'exploitation du système de collecte de logs centralisé.

1. Prérequis Système
Serveur Central : Ubuntu 22.04+ ou Kali Linux avec Apache, MySQL (MariaDB) et PHP installés.

Nœuds Clients (Agents) : Toute distribution Linux (Ubuntu/Kali) disposant de Python 3.

Réseau : Les nœuds doivent pouvoir communiquer avec le serveur central via le port TCP défini (par défaut : 5000).

2. Installation du Serveur Central (Aggregator)
Base de données : Importez le schéma SQL fourni dans src/database.sql pour créer les tables logs et hosts.

Service d'écoute : Lancez le script de réception situé dans src/server/aggregator.py :
  Le code bash est: python3 src/server/aggregator.py

  Le serveur attend désormais les connexions entrantes des agents.

Interface Web : Déplacez le contenu de src/web/ vers votre répertoire web (ex: /var/www/html/dlc/) et configurez le fichier config.php avec vos identifiants MySQL.

3. Installation et Lancement de l'Agent
Sur chaque machine dont vous souhaitez collecter les logs :

Configurez l'adresse IP du serveur central dans le script src/agent/collector.py.

Lancez l'agent en tant que super-utilisateur pour permettre la lecture des fichiers système :
  Le code Bash est: sudo python3 src/agent/collector.py --path /var/log/syslog

  L'agent commence alors à surveiller le fichier et transmet chaque nouvelle ligne au serveur.

4. Utilisation de l'Interface de Consultation
Accédez à l'interface via votre navigateur : http://ip-du-serveur/dlc/.

Tableau de bord : Visualisez en temps réel l'arrivée des logs.

Filtrage :

Par Machine : Sélectionnez le nom d'hôte dans la liste déroulante.

Par Gravité : Filtrez pour n'afficher que les alertes de type ERROR ou WARN.

Par Période : Utilisez le sélecteur de date pour retrouver des incidents passés.

5. Maintenance et Dépannage
Vérification du tampon (Buffer) : Si le serveur est hors ligne, vérifiez le fichier local /tmp/dlc_buffer.log sur l'agent pour confirmer que les logs sont bien conservés en attente de retransmission.

Logs du système DLC : Consultez le fichier /var/log/dlc.log pour diagnostiquer les erreurs de connexion entre l'agent et le serveur.
