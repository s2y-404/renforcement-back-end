# Projet API - Django

## Introduction

Ce projet est une API basée sur Django qui inclut l'authentification des utilisateurs et la gestion des opérations liées aux codes à usage unique (OTP).

## Instructions de configuration

### 1. Cloner le dépôt

Tout d'abord, clonez le dépôt depuis GitHub ou votre plateforme de gestion de version :

```bash
git clone https://github.com/s2y-404/renforcement-back-end.git
cd renforcement-back-end
```

### 2. Installer les dépendances

Installez les packages Python nécessaires répertoriés dans le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

### 3. Créer un fichier `.env`

Dans le répertoire racine du projet, créez un fichier `.env`. Ce fichier contiendra vos variables d'environnement, y compris les identifiants pour l'envoi d'emails. Vous devez renseigner les variables **EMAIL_HOST_USER** et **EMAIL_HOST_PASSWORD** (mot de passe d'application). Ces identifiants sont nécessaires pour l'envoi d'emails par l'application.

```
EMAIL_HOST_USER=<votre-adresse-email>
EMAIL_HOST_PASSWORD=<votre-mot-de-passe-application>
```

Pour générer un mot de passe d'application, suivez ce [guide d'aide de Google](https://support.google.com/accounts/answer/185833?hl=fr#:~:text=Un%20mot%20de%20passe%20d,en%20deux%20%C3%A9tapes%20est%20activ%C3%A9e.).

### 4. Lancer l'application

Après avoir configuré l'environnement, vous pouvez lancer le serveur de développement Django :

```bash
python manage.py runserver
```

## Utilisateurs

Il existe trois utilisateurs par défaut avec des permissions différentes : 

1. **user_view** : Un utilisateur avec des permissions de consultation uniquement.
2. **user_edit** : Un utilisateur avec des permissions de consultation et de modification.

### Mot de passe des utilisateurs

Pour chaque utilisateur, le mot de passe est composé de son nom d'utilisateur avec deux underscores (__).
Par exemple, pour l'utilisateur user_none, le mot de passe sera :

```
user__view
```
