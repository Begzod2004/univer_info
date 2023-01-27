from rest_framework import serializers
from apps.universities.models import *



class UniversitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universities
        fields = ('id','degree','title','country','province','tuition_fees','acceptance_rate','location','programs','image','ielts','toefle','sat','gre','gmat','phone_number','email','description','date_created','is_active',)
