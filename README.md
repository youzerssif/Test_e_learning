# Test_e_learning
Ce projet est un test de validation donnée par Soro n'beh


# Pour lancer l'application

## 1 vous devez cloner le projet et creer un environnement virtuel couli_venv avec ces commande:
```python
python -m venv couli_venv
```


## 2 activer l'environnement, entrer dans le dossier projet et lancer les installations

### pour windows
```python
source couli_venv/Script/activate
cd Couli
pip install -r requirements.txt
```

### pour Mac ou linux
```python
source couli_venv/bin/activate
cd Couli
pip install -r requirements.txt
```

## 3 Apres les installation faites une migration et lancer l'application
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## Pour creer un utilisateur et se connecter a la partir admin
```python
python manage.py createsuperuser
```
puis suivre les instructions, se rendre sur admin http://127.0.0.1:8000/admin/ et se connecter

## Voici le lien youtube pour une presentation de l'interface
https://youtu.be/O2G3_JdJFQo

