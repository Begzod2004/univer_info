from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.universities.views import *
from django.urls import path
from rest_framework import routers
from .views import *
 # Filters
    

router = routers.DefaultRouter()
# router.register('Universities', UniversitiesViewSet, basename='Universities')  

urlpatterns = router.urls


urlpatterns +=  [
    # universitet
    path('universitets/', UniversitiesListAPIView.as_view()),
    path('universitets/create', UniversitiesCreateAPIView.as_view()),
]