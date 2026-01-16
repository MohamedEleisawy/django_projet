from rest_framework import serializers
from .models import Creature, Categorie, Ecosysteme

class CategorieSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description']

class EcosystemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecosysteme
        fields = ['id', 'nom', 'description', 'localisation']

class CreatureSerializer(serializers.ModelSerializer):
    categorie = CategorieSimpleSerializer(read_only=True)
    ecosystemes = EcosystemeSerializer(many=True, read_only=True)
    statut_conservation_display = serializers.CharField(source='get_statut_conservation_display', read_only=True)

    class Meta:
        model = Creature
        fields = [
            'id', 'nom_commun', 'nom_scientifique', 'categorie', 'ecosystemes',
            'esperance_vie', 'poids', 'taille', 'statut_conservation', 
            'statut_conservation_display', 'description', 'date_decouverte', 'image'
        ]

class CategorieWithCreaturesSerializer(serializers.ModelSerializer):
    creatures = CreatureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description', 'creatures']
