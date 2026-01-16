from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Creature, Categorie, Ecosysteme
from .serializers import CreatureSerializer, CategorieWithCreaturesSerializer, EcosystemeSerializer

class CreatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Creature.objects.all().order_by('nom_commun')
    serializer_class = CreatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categorie', 'ecosystemes', 'statut_conservation']
    search_fields = ['nom_commun', 'nom_scientifique', 'description']

class CategorieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorie.objects.all().order_by('nom')
    serializer_class = CategorieWithCreaturesSerializer

class EcosystemeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ecosysteme.objects.all().order_by('nom')
    serializer_class = EcosystemeSerializer
