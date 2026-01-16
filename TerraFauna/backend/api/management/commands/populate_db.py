from django.core.management.base import BaseCommand
from api.models import Creature, Categorie, Ecosysteme
from faker import Faker
import random
import requests
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Remplit la base de données avec des données factices et des images'

    def handle(self, *args, **kwargs):
        self.stdout.write('Suppression des anciennes données...')
        Creature.objects.all().delete()
        Categorie.objects.all().delete()
        Ecosysteme.objects.all().delete()

        fake = Faker('fr_FR')

        self.stdout.write('Création des Catégories...')
        # Define categories and their specific animals with English keywords for images
        data_species = {
            'Mammifères': [('Lion', 'lion'), ('Tigre', 'tiger'), ('Éléphant', 'elephant'), ('Girafe', 'giraffe'), ('Loup', 'wolf'), ('Ours Brun', 'bear'), ('Kangourou', 'kangaroo'), ('Panda', 'panda'), ('Zèbre', 'zebra'), ('Gorille', 'gorilla')],
            'Reptiles': [('Crocodile', 'crocodile'), ('Cobra Royal', 'snake'), ('Iguane', 'iguana'), ('Dragon de Komodo', 'komodo dragon'), ('Tortue Géante', 'tortoise'), ('Caméléon', 'chameleon'), ('Gecko', 'gecko')],
            'Oiseaux': [('Aigle Royal', 'eagle'), ('Perroquet Ara', 'parrot'), ('Pingouin', 'penguin'), ('Hibou Grand-Duc', 'owl'), ('Colibri', 'hummingbird'), ('Autruche', 'ostrich'), ('Faucon', 'falcon')],
            'Amphibiens': [('Grenouille Verte', 'frog'), ('Salamandre Tachetée', 'salamander'), ('Crapaud Commun', 'toad'), ('Triton', 'newt')],
            'Insectes': [('Papillon Monarque', 'butterfly'), ('Mante Religieuse', 'mantis'), ('Abeille', 'bee'), ('Fourmi', 'ant'), ('Scarabée', 'beetle')],
            'Poissons': [('Grand Requin Blanc', 'shark'), ('Poisson Clown', 'clownfish'), ('Saumon', 'salmon'), ('Thon Rouge', 'tuna'), ('Raie Manta', 'stingray'), ('Hippocampe', 'seahorse')],
            'Arachnides': [('Tarentule', 'tarantula'), ('Veuve Noire', 'spider'), ('Scorpion Impérial', 'scorpion')]
        }
        
        cat_objs = {}
        for cat_name in data_species.keys():
            cat_objs[cat_name] = Categorie.objects.create(nom=cat_name, description=fake.text())

        self.stdout.write('Création des Écosystèmes...')
        ecosystemes = ['Forêt Tropicale', 'Savane', 'Désert', 'Toundra', 'Récif Corallien', 'Abysses', 'Urbain', 'Zones Humides']
        eco_objs = [Ecosysteme.objects.create(nom=e, description=fake.text(), localisation=fake.country()) for e in ecosystemes]

        self.stdout.write('Création des Créatures (avec images)...')
        
        count = 0
        for cat_name, species_list in data_species.items():
            category = cat_objs[cat_name]
            for species_name, english_keyword in species_list:
                # Generate random stats
                esperance_vie = random.randint(1, 100)
                poids = round(random.uniform(0.1, 5000), 2)
                taille = round(random.uniform(0.1, 30), 2)
                
                creature = Creature(
                    nom_commun=species_name, 
                    nom_scientifique=f"{species_name.lower().replace(' ', '_')}_{fake.word()}",
                    categorie=category,
                    esperance_vie=esperance_vie,
                    poids=poids,
                    taille=taille,
                    statut_conservation=random.choice([c[0] for c in Creature.STATUT_CONSERVATION_CHOICES]),
                    description=fake.paragraph(nb_sentences=5),
                    date_decouverte=fake.date_between(start_date='-200y', end_date='today')
                )
                
                # Fetch Image
                try:
                    img_url = f"https://loremflickr.com/400/300/{english_keyword}"
                    response = requests.get(img_url, timeout=5)
                    if response.status_code == 200:
                        creature.image.save(f"{english_keyword}.jpg", ContentFile(response.content), save=False)
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Erreur téléchargement image pour {species_name}: {e}"))

                creature.save()
                
                # Add random ecosystems
                creature.ecosystemes.set(random.sample(eco_objs, k=random.randint(1, 3)))
                creature.save()
                count += 1
                self.stdout.write(f" - {species_name} ajouté.")

        self.stdout.write(self.style.SUCCESS(f'Base de données peuplée avec succès avec {count} créatures et leurs photos !'))
