from django.db import models
from django.contrib.auth.models import User

BRANDS = [
    ('B', 'Bridgestone'),
    ('C', 'Callaway'),
    ('H', 'Honma'),
    ('K', 'Kirkland'),
    ('M', 'Mizuno'),
    ('Sl', 'Slazenger'),
    ('Sr', 'Srixon'),
    ('Ta', 'Taylormade'),
    ('Ti', 'Titleist'),
    ('To', 'TopFlite'),
    ('Vi', 'Vice'),
    ('Vo', 'Volvik'),
    ('W', 'Wilson'),
]

SPIN = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High')
]


FEEL = [
    ('S', 'Soft'),
    ('F', 'Firm')
]


# Create your models here.
class Brand(models.Model):
    name = models.CharField(
        max_length=2,
        choices=BRANDS
    )
    def __str__(self):
        return self.get_name_display()
    
    

class Ball(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    spin = models.CharField(
        max_length=1,
        choices=SPIN
    )
    feel = models.CharField(
        max_length=1,
        choices=FEEL
    )
    
    def __str__(self):
    
        return f"{self.brand}: {self.name} has a {self.get_spin_display()} spin and {self.get_feel_display()} feel"
  
    


    
    
    
    
    