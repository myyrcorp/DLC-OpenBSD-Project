1. Architecture Logicielle (Modèle Distribué)
Le système repose sur une architecture Producteur–Consommateur répartie sur plusieurs nœuds :

Producteurs (Agents DLC) : Installés sur les serveurs OpenBSD clients. Ils surveillent les fichiers /var/log et transmettent les données via des sockets sécurisées.

Consommateur (Aggregator) : Un service centralisé qui écoute les connexions entrantes, traite les chaînes de caractères reçues et les insère en base de données.

Couche de Stockage : Une base MySQL optimisée pour l'écriture rapide et l'indexation temporelle.

2. Schéma des Communications (Logique API)
Bien que le système utilise principalement des protocoles de transport de données, la logique d'échange suit une structure d'API simplifiée pour garantir la compatibilité :

Format d'envoi (JSON ou CSV) :

hostname : Identifiant du nœud.

timestamp : Date précise de l'événement.

severity : Niveau de gravité (0=INFO, 1=WARN, 2=ERROR).

payload : Message brut du log.

Mécanisme de "Handshake" : L'agent vérifie la disponibilité du serveur avant l'envoi pour décider s'il doit utiliser le tampon local (buffer).

3. Conception de la Base de Données (UML/Schéma)
Le schéma relationnel est conçu pour supporter des volumes importants sans perte de performance :

Table remote_hosts : Stocke la liste des machines autorisées.

Table logs_archive : Table principale partitionnée par date pour accélérer les recherches sur l'interface Web.

4. Architecture de l'Interface Web
L'interface de consultation est conçue en PHP (WampServer) selon le modèle MVC (Modèle-Vue-Contrôleur) :

Modèle : Requêtes SQL optimisées pour les filtres par période.

Vue : Dashboard responsive pour visualiser les alertes "ERROR" en rouge.

Contrôleur : Gestion de l'authentification et de la validation des formulaires de recherche.
