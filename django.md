# 📘 Documentation Complète - TerraFauna

**TerraFauna** est une encyclopédie interactive de la biodiversité. Ce fichier documente l'intégralité du travail réalisé : architecture, code source des modèles, et choix techniques, entièrement francisés.

---

## 🏗️ 1. Architecture du Projet

Le projet est divisé en deux parties distinctes :

- **Backend (`/backend`)** : Serveur Django exposant une API REST.
- **Frontend (`/frontend`)** : Application React (Vite) consommant l'API.

### Technologies

- **Langage** : Python 3.14 (Backend), JavaScript (Frontend).
- **Frameworks** : Django 6.0, Django REST Framework, React 18.
- **Base de Données** : SQLite (Transitionnable vers Oracle via `settings.py`).
- **Outils** : `Faker` (Données de test), `ReportLab` (PDF), `Matplotlib` (Stats).

---

## 🐍 2. Backend (Django)

### Modèles de Données (`api/models.py`)

Les modèles ont été traduits pour refléter le domaine métier en français.

```python
class Categorie(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    # ...

class Ecosysteme(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    localisation = models.CharField(...)
    # ...

class Creature(models.Model):
    nom_commun = models.CharField(max_length=100, verbose_name="Nom Commun")
    nom_scientifique = models.CharField(...)

    # Relations
    categorie = models.ForeignKey(Categorie, ...)
    ecosystemes = models.ManyToManyField(Ecosysteme, ...)

    # Caractéristiques physiques
    esperance_vie = models.IntegerField(verbose_name="Espérance de Vie")
    poids = models.FloatField(verbose_name="Poids (kg)")
    taille = models.FloatField(verbose_name="Taille (m)")

    statut_conservation = models.CharField(...) # Choix UICN (EX, EN, LC...)
```

### API REST (`api/views.py` & `urls`)

Endpoints disponibles :

- `GET /api/creatures/` : Liste paginée des créatures (Filtres: `categorie`, `ecosystemes`).
- `GET /api/creatures/{id}/` : Détail d'une créature.
- `GET /api/categories/` : Liste des catégories.
- `GET /api/ecosystemes/` : Liste des écosystèmes.

### Interface d'Administration

L'admin Django a été personnalisé avec :

1.  **Export PDF** : Action de masse pour télécharger les fiches d'identité.
2.  **Statistiques** : Vue graphique (`matplotlib`) de la répartition des espèces.

---

## ⚛️ 3. Frontend (React)

### Navigation (`Home.jsx`)

Une grille de cartes affichant les créatures.

- **Filtrage** : Utilisation des paramètres URL `?ecosystemes=ID`.
- **Pagination** : Gestion des pages via l'API Django.

### Détails (`CreatureDetail.jsx`)

Page immersive affichant toutes les caractéristiques traduits (Poids, Taille, Statut).

- **Rebond** : Clic sur un tag Écosystème -> Redirection vers la liste filtrée.

---

## 📝 4. Historique des Réalisations (Log)

1.  **Initialisation** : Création de la structure `TerraFauna/` avec `backend` (Django) et `frontend` (Vite).
2.  **Configuration** : Mise en place de `corsheaders` et `REST_FRAMEWORK`.
3.  **Développement Backend** :
    - Création des modèles `Creature`, `Categorie`, `Ecosysteme`.
    - Script `populate_db` générant 50 animaux fictifs en français.
    - Implémentation de l'export PDF (Identity Card).
    - Implémentation de la vue Stats (Graphique).
4.  **Développement Frontend** :
    - Création des composants `Navbar`, `Home`, `CreatureDetail`.
    - Intégration API via `Axios`.
    - Styling CSS moderne (Global + Modules).
5.  **Francisation Complète** : Refactoring de tout le code (Variables: `lifespan` -> `esperance_vie`, etc.) pour répondre à la demande 100% Français.

---

_Ce fichier est généré automatiquement pour suivre l'état du projet._
