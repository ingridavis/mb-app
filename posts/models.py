from django.db import models

# Create your models here.

class Post(models.Model): #models.py is calling the Model class with all its attributes
    text = models.TextField()

    def __str__(self):
        return self.text[:50] #slice 

"""
^ magic method  __str__
part of python's built in. Represents class in specific way. 
Without the __str__ it uses the class as an object but
we need a string. 
"""

