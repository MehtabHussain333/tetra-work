from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('PC','Pre-Construction'),
    ('GC','General Contracting'),
    ('CM','Construction Management'),
    ('DB','Design and Build'),


)


class Product (models.Model):

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    title = models.CharField(max_length=100)
    description = models.TextField()
    composition = models.TextField(default='')        
    product_image = models.ImageField(upload_to = 'product')
    prodfile = models.FileField(upload_to = 'Files',null=True)
    def _str_(self):
        return self.title

class MainCategory (models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()


    def _str_(self):
        return self.title


class SubCategory (models.Model):
    
    title = models.CharField(max_length=100)
    mcategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return str(self.mcategory.title)