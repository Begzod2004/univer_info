from django.db import models
from apps.account.models import Account

# class Category(models.Model):
#     parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent category", limit_choices_to={'is_active': True, 'parent_category__isnull': True}, related_name='children', null=True, blank=True)
#     title = models.CharField(max_length=50, verbose_name="Category title")
#     slug = models.SlugField()
#     is_active = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     def __str_(self):
#         return self.title




