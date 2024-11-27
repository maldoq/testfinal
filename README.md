# 📚 **Elenizado : Plateforme de Test**

Bienvenue sur le projet **Elenizado**, une plateforme conçue pour favoriser les interactions entre professeurs et étudiants autour de la langue espagnole. Ce document vous guidera à travers les étapes d'installation, d'exécution et de test du projet.

---

## 📖 **Table des Matières**

- [Introduction](#introduction)
- [Installation et Lancement](#installation-et-lancement)
- [Exécution des Tests](#exécution-des-tests)
- [Plan de Test](#plan-de-test)
- [Structure du Projet](#structure-du-projet)
- [Outils et Technologies](#outils-et-technologies)
- [Auteur](#auteur)

---

## 📝 **Introduction**

**Elenizado** est une plateforme destinée aux étudiants pour :
- Lire des articles récents.
- Ajouter des commentaires ou répondre à des publications.
- Découvrir des événements culturels.
- Contacter des professeurs via un formulaire de requête.

Les tests sont réalisés pour garantir :
1. Une navigation fluide.
2. Un fonctionnement optimal des commentaires.
3. La fiabilité des messages envoyés via le formulaire.

---

## ⚙️ **Installation et Lancement**

### **Prérequis**
- **Python** >= 3.9
- **Django** >= 4.0
- **Virtualenv**
- **Node.js** (si applicable)

### **Étapes d'installation**
1. **Cloner le projet**
   ```bash
   git clone https://github.com/votre-repo/elenizado.git
   cd elenizado
2. **Créer et activer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
4. **Appliquer les migrations**
   ```bash
   python manage.py migrate
5. **Lancer le serveur local**
   ```bash
   python manage.py runserver
6. Accéder à l'application via http://127.0.0.1:8000/.

---

## 🧪 **Exécution des Tests**

### **Lancer les tests unitaires avec Pytest**

