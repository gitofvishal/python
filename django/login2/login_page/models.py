from django.db import models

# Create your models here.


class logs(models.Model):
    uname = models.CharField(primary_key=True,max_length=122)
    pas = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    
        
    def __str__(self):
        return self.uname
    