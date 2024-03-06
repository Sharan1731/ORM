from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    Page_no=models.IntegerField();
    name=models.CharField(max_length=20);
    Chapter=models.CharField(max_length=20);
    Author=models.CharField(max_length=20);
    Established=models.CharField(max_length=20);
class Book_DBAdmin(admin.ModelAdmin):
    list_display=("Page_no","name","Chapter","Author","Established")
