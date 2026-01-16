from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.nom

class Ecosysteme(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")
    localisation = models.CharField(max_length=200, help_text="Localisation typique ou climat", verbose_name="Localisation")

    class Meta:
        verbose_name = "Écosystème"
        verbose_name_plural = "Écosystèmes"

    def __str__(self):
        return self.nom

class Creature(models.Model):
    STATUT_CONSERVATION_CHOICES = [
        ('EX', 'Éteint (Extinct)'),
        ('EW', 'Éteint à l\'état sauvage (Extinct in the Wild)'),
        ('CR', 'En danger critique (Critically Endangered)'),
        ('EN', 'En danger (Endangered)'),
        ('VU', 'Vulnérable (Vulnerable)'),
        ('NT', 'Quasi menacé (Near Threatened)'),
        ('LC', 'Préoccupation mineure (Least Concern)'),
        ('DD', 'Données insuffisantes (Data Deficient)'),
        ('NE', 'Non évalué (Not Evaluated)'),
    ]

    nom_commun = models.CharField(max_length=100, verbose_name="Nom Commun")
    nom_scientifique = models.CharField(max_length=150, unique=True, verbose_name="Nom Scientifique")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='creatures', verbose_name="Catégorie")
    ecosystemes = models.ManyToManyField(Ecosysteme, related_name='creatures', verbose_name="Écosystèmes")
    
    esperance_vie = models.IntegerField(help_text="Espérance de vie moyenne en années", verbose_name="Espérance de Vie")
    poids = models.FloatField(help_text="Poids moyen en kg", verbose_name="Poids (kg)")
    taille = models.FloatField(help_text="Taille moyenne/longueur en mètres", verbose_name="Taille (m)")
    
    statut_conservation = models.CharField(max_length=2, choices=STATUT_CONSERVATION_CHOICES, verbose_name="Statut de Conservation")
    description = models.TextField(verbose_name="Description")
    date_decouverte = models.DateField(null=True, blank=True, verbose_name="Date de Découverte")
    
    image = models.ImageField(upload_to='creatures/', null=True, blank=True, verbose_name="Image")

    class Meta:
        verbose_name = "Créature"
        verbose_name_plural = "Créatures"

    def __str__(self):
        return self.nom_commun
