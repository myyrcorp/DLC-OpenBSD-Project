Ici, nous presenterons dossier de réalisation pour l'implémentation du DLC sous Linux.

1. Environnement de Développement
Bien que la base conceptuelle soit OpenBSD, la réalisation technique s'appuie sur des outils Linux standards pour garantir la portabilité :

Système d'exploitation : Ubuntu 22.04 LTS ou Kali Linux 2024.x.

Langages : Python ou C pour les agents de collecte (lecture des fichiers /var/log) et PHP 8.x pour le backend Web.

Base de données : MySQL (ou MariaDB) installée via le gestionnaire de paquets apt.

2. Architecture du Code Source (src/)
Le code est structuré pour séparer la logique de collecte de la logique d'affichage :

agent/ : Scripts Python utilisant la bibliothèque watchdog ou tail -f pour surveiller les journaux système.

server/ : Script d'écoute (Socket Server) qui reçoit les données et exécute les requêtes INSERT vers MySQL.

web/ : Fichiers PHP pour le tableau de bord de consultation.

3. Mécanisme de Retransmission (Logique Linux)
Sur Ubuntu/Kali, nous utilisons le système de fichiers pour la tolérance aux pannes :

L'agent tente une connexion TCP vers le serveur central.

Si la connexion échoue (serveur hors ligne), l'agent écrit le log dans /tmp/dlc_buffer.log.

Un processus en arrière-plan vérifie périodiquement la disponibilité du serveur et vide ce fichier une fois la connexion rétablie.

4. Plan de Tests et Validation
La validation s'effectue sur la Semaine 7 via les tests suivants :

Test de connectivité : Vérification de la réception d'un message "INFO" envoyé depuis un nœud distant.

Simulation de panne réseau : Coupure de l'interface réseau (sudo ifconfig eth0 down), génération de logs, puis rétablissement pour vérifier la retransmission automatique.

Test de performance : Injection de 1000 logs en une minute pour tester la réactivité de l'interface Web et l'indexation MySQL.

5. Déploiement Rapide
Les scripts de déploiement (dans /scripts) permettent d'automatiser l'installation des dépendances :

Voici un exemple de commande de déploiement agent sur Ubuntu
sudo apt update && sudo apt install python3-mysql.connector -y
