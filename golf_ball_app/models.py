from django.db import models

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
class Ball(models.Model):

    brand = models.CharField(
        max_length=2,
        choices=BRANDS
    )
    name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return f"{self.brand}:{self.name}"
    
class Attribute(models.Model):
    
    spin = models.CharField(
        max_length=1,
        choices=SPIN
    )
    
    feel = models.CharField(
        max_length=1,
        choices=FEEL
    )
    
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ball} spin:{self.spin} feel:{self.feel}"
    
    
    
    