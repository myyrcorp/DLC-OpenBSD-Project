#!/bin/bash

# Démarrer le serveur d'agrégation en arrière-plan
echo "Démarrage de l'Aggregator..."
python3 ../src/server/aggregator.py &

sleep 2

# Démarrer l'agent de collecte local pour test
echo "Démarrage de l'Agent local..."
python3 ../src/agent/collector.py
