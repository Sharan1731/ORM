# Ex02 Django ORM Web Application
## Date: 6.3.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![Screenshot 2024-03-11 201712](https://github.com/Sharan1731/ORM/assets/144980172/7cb0e0f5-dbb8-424f-a7ce-f4b929f5a84c)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import Book_DB,Book_DBAdmin 
admin.site.register (Book_DB,Book_DBAdmin)

models.py

from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    Page_no=models.IntegerField();
    name=models.CharField(max_length=20);
    Chapter=models.CharField(max_length=20);
    Author=models.CharField(max_length=20);
    Established=models.CharField(max_length=20);
class Book_DBAdmin(admin.ModelAdmin):
   ("Page_no","name","Chapter","Author","Established")
```
## OUTPUT
![alt text](<Screenshot 2024-03-06 110230.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
