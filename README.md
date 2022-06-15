## Status

<span>[![CircleCI](https://circleci.com/gh/SaiedZ/OC-P13-Python-OC-Lettings-FR/tree/master.svg?style=svg)](https://circleci.com/gh/SaiedZ/OC-P13-Python-OC-Lettings-FR/tree/master)
![Heroku](https://heroku-badge.herokuapp.com/?app=oc-letting)</span>


## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## CI/CD - Intégration continue / déploiement continu

### Description du process CI/CD

Le pipeline a été mis en place via CircleCi. Il est constitué des étapes suivantes :

-   Compilation et test de l'environnement local
-   Création de l'image Docker, via le fichier Dockerfile, et téléchargement vers le dockerhub.
-   Déploiement sur heroku  à partir de l'image envoyée précédemment sur dockerhub.

> *Chaque étape doit être complétée avec succès pour passer à la suivante.*
> *La troisième étape à savoir le déploiement sur heroku n'est enclenché que les commit faits sur la branche **master**.*

Chacune de ces trois étapes est détaillées dans le graph ci-dessous.

```mermaid
flowchart LR
		 subgraph compile-and-test-local-environment
		 	 id1([checkout])
			 id2([Installing dependencies])
			 id3([Runing tests])
			 id4([Lingting with flake8])
			 id999([Store pytest report to artifact])
			 id1-->id2-->id3-->id4-->id999
		 end
		 subgraph build-push-docker
			 id5([checkout])
			 id6([Build Docker image])
			 id7([Loging to Docker])
			 id8([Taging with hash commit and pushing the docker image])
			 id5-->id6-->id7-->id8
		 end
		 subgraph deploy-heroku
			 id9([checkout])
			 id10([Loging to Docker])
			 id11([Login to Heroku])
			 id12([Pull docker image])
			 id13([tagging docker image])
			 id14([pushing to heroku registry])
			 id15([releasing app])
			 id9-->id10-->id11-->id12-->id13-->id14-->id15
		 end
 compile-and-test-local-environment --> build-push-docker
 build-push-docker-- Only Master Branch -->deploy-heroku
```

### Configuration

#### Prérequis

-   Un compte GitHub
-   Un compte Docker et installation en local
-   Un compte CircleCI relié au compte Github
-   Un compte Heroku
-   Un compte Sentry