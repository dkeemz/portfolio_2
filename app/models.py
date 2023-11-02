from django.db import models

# Create your models here.
class Project(models.Model):
    # ...
    image = models.ImageField(upload_to="image",blank=True,null=True)
    title = models.CharField(max_length=50)
    description =models.CharField(max_length=200,default="Item Description")
    live_link = models.CharField(max_length=200,null=True,blank=True)
    github_link = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    
    