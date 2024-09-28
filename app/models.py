from django.db import models

# Create your models here.
class hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotelpic')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class media(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='newsphoto')

    
class ourcommunity(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ourcommunity')
    def __str__(self):
        return self.name
  

    
class exploreproperties(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='propertyphoto')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class unexplore(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='unexplore')
    location = models.CharField(max_length=100)


class gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class package(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    package =  models.CharField(max_length=100)

    def __str__(self):
        return self.name


class carrer(models.Model):
    job_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.job_name


class testimonial(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

