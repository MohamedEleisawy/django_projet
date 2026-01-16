from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatureViewSet, CategorieViewSet, EcosystemeViewSet

router = DefaultRouter()
router.register(r'creatures', CreatureViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'ecosystemes', EcosystemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
