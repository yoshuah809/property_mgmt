from django.db import models

# Create your models here.

class Property(models.Model):
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    images = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.address
    
    class Meta:
       verbose_name_plural = "Properties"
       
    # def save(self, **kwargs):
    #     self.address = self.address.upper()
    #     super(Property,self).save()   
    
    