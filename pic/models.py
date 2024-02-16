from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.TextField()
    def __str__(self):
        return self.title
    



class Image(models.Model):
    title=models.CharField(max_length=200)
    descriptions=models.TextField()
    image=models.ImageField(upload_to='images')
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

