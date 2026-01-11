1. Présentation du projet
Le projet Distributed Logs Collector (DLC) vise à centraliser les journaux d'activité (logs) générés par diverses machines au sein d'une infrastructure informatique distribuée. L'objectif est de transformer ces données brutes en un outil d'aide à la décision et de diagnostic rapide.

2. Spécifications Fonctionnelles
Le système doit remplir les fonctions suivantes :

Collecte automatique : Récupération des logs systèmes et applicatifs sur chaque nœud distant.

Transmission résiliente : Envoi sécurisé des données avec un mécanisme de stockage local temporaire en cas de coupure réseau.

Centralisation et Indexation : Stockage organisé sur un serveur central permettant des recherches rapides.

Interface Web : Visualisation des logs avec filtres par gravité (INFO, WARN, ERROR), par machine et par date.

3. Spécifications Techniques
Système d'exploitation : OpenBSD pour sa sécurité et sa stabilité.

Base de données : MySQL pour l'indexation des logs.

Interface Web : Stack PHP/Apache (WampServer pour le développement).

Outils de développement : VS Code.

4. Contraintes et Qualités (Besoins non fonctionnels)
Sécurité : Chiffrement des transferts de logs et accès restreint à l'interface de consultation.

Scalabilité : Capacité à supporter une augmentation du nombre de serveurs clients sans perte de performance.

Fiabilité : Garantie de l'intégrité des logs, sans altération lors du transfert.

5. Calendrier de réalisation
Le projet se déroule sur 8 semaines :

S1 : Analyse et rédaction du cahier des charges.

S2-S4 : Conception de l'architecture et développement des agents de collecte.

S5-S6 : Développement du serveur central (Aggregator) et de l'interface Web.

S7 : Tests complets et simulations de pannes.

S8 : Finalisation de la documentation et préparation de la soutenance.
