--
Authors : Mohamed Ele
url : https://linkedin.com/in/mohamed-
Category : Dcp-25
Date : 2026-01-16
Title : Django
--

## Créer un projet django

- Django = admin
- Django React Freamwork = api en lecture seule
- Vue ou React ou Angular = front, listes/detail/pagination/rebonds servi par Django --> static
- Admin = export PDF d'une fiche, graphiques matplotlib, Export de la bdd, génerér des données aléatoirement
- BDD = Oracle
- Une table principale( 7 champs minimum), une ou plusieurs 1-N, une ou plusieurs N-N
- Sujet libre   


Sujet : Plateforme éducative d'exploration de la biodiversité mondiale.
une application dédiée à la découverte des espèces animales. L'idée est de proposer une expérience éducative où l'utilisateur explore des 'fiches créatures' via une interface moderne en Single Page Application (SPA). Le projet repose sur une base Oracle gérée par un back-office Django complet permettant aux experts naturalistes d'administrer les données, de générer des rapports statistiques et d'exporter des fiches d'identité au format PDF


python --version && pip list
pip install djangorestframework django-cors-headers faker matplotlib reportlab
$ python -m django startproject backend && cd backend && python manage.py startapp api 
python manage.py makemigrations && python manage.py migrate