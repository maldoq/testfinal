Elenizado : Plateforme de Test
Ce projet consiste à tester et valider le bon fonctionnement d'un site web espagnol nommé Elenizado, conçu pour les interactions entre professeurs et étudiants autour de la langue espagnole. Ce README vous guidera pour lancer le projet et comprendre les tests réalisés.

📖 Introduction
Le site Elenizado permet aux étudiants de :

Consulter des articles récents sur la langue espagnole.
Commenter des publications et répondre à d'autres commentaires.
Découvrir les événements à venir liés à la langue espagnole.
Consulter les bibliographies de certains auteurs (professeurs).
Envoyer des requêtes pour contacter ces professeurs.
Les tests ont pour objectif de vérifier :

La navigation correcte sur le site.
Le bon fonctionnement des commentaires.
L’envoi des messages via le formulaire de contact.
⚙️ Installation et Lancement
Prérequis
Python (version ≥ 3.9)
Django (version ≥ 4.0)
Virtualenv pour la gestion des environnements virtuels.
Node.js (si des dépendances frontend sont nécessaires)
Étapes d'installation
Cloner le projet

bash
Copier le code
git clone https://github.com/votre-repo/elenizado.git
cd elenizado
Créer et activer un environnement virtuel

bash
Copier le code
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
Installer les dépendances

bash
Copier le code
pip install -r requirements.txt
Appliquer les migrations

bash
Copier le code
python manage.py migrate
Lancer le serveur

bash
Copier le code
python manage.py runserver
Accéder à l'application sur http://127.0.0.1:8000/.

🧪 Tests
Types de tests réalisés
Tests unitaires : Vérifient les composants individuels.
Tests d’intégration : Assurent la bonne interaction entre les modules.
Tests de performance : Évaluent la rapidité et l'efficacité du site avec Locust.
Analyse CI/CD : Détection des failles dans les pipelines d’intégration continue.
Exécution des tests
Configurer pytest

Un fichier pytest.ini est inclus dans la racine du projet.
Les tests se trouvent dans des dossiers nommés tests au sein de chaque application.
Lancer les tests

bash
Copier le code
pytest
Rapports

Les résultats sont générés en HTML pour une visualisation détaillée.
Les conventions PEP8 sont validées avec Flake8 :
bash
Copier le code
flake8
🔍 Plan de Test
Identification des besoins
Tester les liens des pages (accueil, détails des articles, etc.).
Valider l’envoi des commentaires et leur gestion.
Vérifier l’envoi des messages via le formulaire de contact.
Cas de test prioritaires
Inscription valide et invalide.
Connexion valide et invalide.
Ajout de blog (valide et invalide).
Fonctionnalité de like.
Commentaires (avec et sans authentification).
Exemple de tests unitaires
Voici un exemple de test pour vérifier l'accessibilité de la page d'accueil :

python
Copier le code
from django.test import TestCase, Client

class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_accessible(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
📊 Résultats
Tests manuels

Problèmes détectés : erreurs de navigation dues à des importations incorrectes dans models.py.
Le formulaire de contact génère une erreur en l’absence d’un email valide.
Tests logiciels

Rapport HTML généré pour les tests.
Le code ne respecte pas entièrement les normes PEP8. Une configuration de pre-commit est recommandée.
Tests de performance

Les rapports Locust sont disponibles dans le dossier performancetest.
🚀 Conclusion
Une révision du code est nécessaire pour corriger les erreurs de navigation et de gestion des formulaires.
Un système CI/CD est fortement recommandé pour maintenir la qualité du code et automatiser les tests.
Implémenter un outil comme pre-commit pour respecter les normes PEP8.
📂 Structure du Projet
plaintext
Copier le code
elenizado/
│
├── elenizado/            # Application principale
├── tests/                # Dossiers contenant les tests
├── static/               # Fichiers statiques (CSS, JS, images)
├── templates/            # Templates HTML
├── manage.py             # Commande de gestion Django
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
🛠️ Outils et Technologies
Django : Framework backend.
Pytest : Framework pour les tests.
Flake8 : Validation des normes PEP8.
Locust : Tests de performance.
📝 Auteur
Nom : Votre Nom
Email : votre.email@example.com
GitHub : Votre Profil GitHub
