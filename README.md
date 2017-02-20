# sketchbadges

# Description

- Partir d'une structure Django vierge
- Rajouter les users + un model Model3d() qui représente un modèle 3d
- Implémenter une fonctionnalité de 'badges': 
    - il existe plusieurs types de badge, chacun étant décerné pour une action ou série d'action effectuée par l'utilisateur sur le site
    - La liste des badges qu'un user a obtenu doit être accessible via l'api
    - Le backend doit "décerner" les badges aux users (ie: détecter quand une action a été réalisée et donner le badge au user)
  
*Exemples de badges:*
- **Star**: le modèle d'un user a plus de 1k views
- **Collector**: un user a uploadé plus de 5 modèles
- **Pionneer**: le user est inscrit depuis plus de 1 an sur le site

# Lancer le projet

1. Cloner le projet
2. Créer un fichier .env en copiant le fichier env.example
3. Personnaliser le .env
4. Lancer les commandes suivantes: 
   * `python manage.py migrate`
   * `python manage.py loaddata studio/fixtures/groups.yaml`
   * `python manage.py createsuperuser`
   * `python manage.py runserver`
   
# TODO

* Ecrire plus de tests: models, views
* Configuration pour environnement de production et de tests

