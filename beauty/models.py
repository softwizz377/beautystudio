from django.db import models
from django.utils import timezone


# Create your models here.
class contact(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	
	
	class Meta:
		db_table="contact"
	def __str__(self):
		return self.name

class appointment(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	date=models.CharField(max_length=200)
	time=models.CharField(max_length=200)
	appointmentfor=models.CharField(max_length=200)
	appointmentplace=models.CharField(max_length=200)
	
	class Meta:
		db_table="appointment"
	def __str__(self):
		return self.name
		
class feedback(models.Model):
	experience=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	message=models.CharField(max_length=200)
	
	
	class Meta:
		db_table="feedback"
	def __str__(self):
		return self.name

class category(models.Model):
	name= models.CharField(max_length=200)	
	image = models.ImageField(upload_to = 'images/', default="")
	class Meta:
		db_table="category"
	def __str__(self):
		return self.name
		
class service(models.Model):
	name=models.CharField(max_length=200)
	category= models.ForeignKey(category,on_delete=models.CASCADE)
	discription=models.TextField(default='')
	price=models.IntegerField()
	image = models.ImageField(upload_to = 'images/')
	class Meta:
		db_table="service"
	def __str__(self):
		return self.name
		
class FAQs(models.Model):
	question=models.CharField(max_length=200)
	answer=models.CharField(max_length=200)
	class Meta:
		db_table="FAQs"
	def __str__(self):
		return self.question


class career(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	gender=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	sentfile=models.FileField(upload_to='resume/', default="")
	class Meta:
		db_table="career"
	def __str__(self):
		return self.name
		
class Product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True)

    class Meta:
	
        ordering = ('name', )
        

    def __str__(self):
        return self.name

    
