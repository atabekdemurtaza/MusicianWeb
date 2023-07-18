from django.db import models


class Product(models.Model):

    class Status(models.TextChoices):
        GOOD = 'G', 'Bad'
        BAD  = 'B', 'Good'

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    condition = models.CharField(max_length=2, choices=Status.choices, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']



class Repair(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='repairs/%Y/%m/%d/')
    date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

        
