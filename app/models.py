from __future__ import unicode_literals


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from django.conf import settings
import os
from django.core.files import File
from django.conf import settings

from django.conf import settings
import os

"""
county_names=[]
		counties = open(os.path.join(settings.BASE_DIR, 'counties'), 'r')
		for county in counties:
			county_names.append(county)

"""
"""
class Counties(models.Model):
	county_number=models.IntegerField(max_length=47)
	county_name=models.CharField(max_length=50)

"""



class RainDataStore(models.Model):
	counties = open(os.path.join(settings.BASE_DIR, 'counties'), 'r')
				
    	myListofCounties = [tuple(line.split(',')) for line in counties.readlines()]
	
	County=models.CharField(max_length=50, choices=myListofCounties )
	
	months_of_year = (

        ('Jan', 'January'),
        ('Feb', 'February'),
        ('March', 'March'),
        ('May', 'May'),
	('June', 'June'),
	('JUly', 'July'),
	('Aug', 'August'),
	('sep', 'September'),
	('Oct', 'October'),
	('Nov', 'November'),
	('Dec', 'December'),
    
	)
    
	Month = models.CharField(max_length=25,
                                      choices=months_of_year,
                                      )
	Rainfall_Amount=models.FloatField(validators=[MinValueValidator(0)])


	class Meta:
    		unique_together = ('County', 'Month',)




	def __str__(self):
		return self.County














