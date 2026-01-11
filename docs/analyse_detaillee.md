Nous vous présentons ici  le dossier d'analyse du Système DLC

1. Analyse des Cas d'Utilisation (Use Cases)
L'analyse se concentre sur deux types d'utilisateurs (acteurs) et sur le comportement autonome du système.

Administrateur Système / DevOps :

Consulter les logs centralisés via l'interface Web.

Filtrer les événements par machine, par période ou par niveau de gravité (INFO, WARN, ERROR).

Surveiller l'état de santé des nœuds distants.

Agent de Collecte (Système) :

Lire les fichiers journaux locaux en temps réel.

Transmettre les données au serveur central.

Gérer la mise en tampon (buffering) locale en cas de coupure réseau.

Serveur Central (Log Aggregator) :

Réceptionner et valider les flux de logs entrants.

Indexer les données dans la base de données MySQL pour une recherche optimisée.

2. Contraintes Fonctionnelles Approfondies
Pour que le projet soit validé académiquement, il doit respecter les règles suivantes :

Intégrité temporelle : Chaque log doit conserver son horodatage (timestamp) d'origine provenant du nœud source.

Identification unique : Le système doit pouvoir distinguer l'origine de chaque log (nom d'hôte ou IP du nœud).

Gestion des priorités : Les logs de type "ERROR" doivent être facilement identifiables pour permettre une réaction immédiate.

3. Analyse de la Tolérance aux Pannes
Le système doit répondre au modèle de fiabilité suivant :

Détection : L'agent détecte que le serveur central est injoignable.

Conservation : Les logs sont écrits dans un fichier temporaire sur le disque local de l'agent.

Restauration : Une fois la connexion rétablie, l'agent envoie les logs stockés en respectant l'ordre chronologique (FIFO - First In, First Out).

4. Modèle de Données (Aperçu)
La base de données MySQL contiendra au minimum une table logs structurée ainsi :

id : Clé primaire.

host_name : Source du log.

level : Gravité (INFO, WARN, ERROR).

message : Contenu du journal.

created_at : Date et heure de l'événement.
