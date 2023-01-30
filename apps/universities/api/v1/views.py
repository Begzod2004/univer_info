from rest_framework.viewsets import ModelViewSet
from apps.universities.models import *
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

class UniversitiesListAPIView(ListAPIView):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer
    parser_classes = (FormParser, MultiPartParser)

class UniversitiesCreateAPIView(CreateAPIView):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer
    parser_classes = (FormParser, MultiPartParser)






# class UniversitiesViewSet(ModelViewSet):
#     queryset = Universities.objects.all()
#     serializer_class = UniversitiesSerializer
#     parser_classes = (FormParser, MultiPartParser)