from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
    
class Company(models.Model):
    name = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"
        
        

class Property(models.Model):
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    images = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='properties', default=1, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.address
    
    class Meta:
       verbose_name_plural = "Properties"
       
    # def save(self, **kwargs):
    #     self.address = self.address.upper()
    #     super(Property,self).save()   
    
class Comment(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="comments")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f' Rating: {str(self.rating)}  Address: {self.property}'