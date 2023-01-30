from django.db import models
from apps.account.models import Account

DEGREE_STATUS = (
    ('bakalavr',"Bakalavr"),
    ('magistratur',"Magistratur")
)


class Universities(models.Model):
    degree = models.CharField(max_length=123,choices=DEGREE_STATUS, help_text="bakalrmi yoki magistraturami")
    title = models.CharField(max_length=65)
    country = models.CharField(max_length=120)
    province = models.CharField(max_length=120,help_text="Viloyat")
    tuition_fees = models.FloatField(max_length=123,help_text='kantract uchun....')
    acceptance_rate = models.CharField(max_length=123, help_text="kirish foizi")
    location = models.CharField(max_length=120,help_text="lacatsiyasi")
    programs = models.CharField(max_length=123,help_text="Yonalishlari")
    image = models.ImageField(upload_to='univer/')
# Language score
    ielts = models.FloatField(help_text="Ilts darajasi",null=True,blank=True) #null bolishi munkun
    toefle = models.IntegerField(help_text="Amerika til darsajasi",null=True,blank=True) #null
    sat = models.IntegerField(help_text="matematika va inglis tili darajasi",null=True,blank=True) #null
    gre = models.CharField(max_length=123, help_text="imtihon score",null=True,blank=True) #null
    gmat = models.FloatField(max_length=123, help_text="magistratura uchun inglis tili va matematika", null=True,blank=True) #null
# Contact
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()

    description = models.TextField(help_text="batafsil malumot")
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)


