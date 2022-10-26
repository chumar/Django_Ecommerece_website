from django.db import models

# Create your models here.

from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500)
    chead0 = models.CharField(max_length=5000)
    head1 = models.CharField(max_length=500)
    chead1 = models.CharField(max_length=5000)
    head2 = models.CharField(max_length=500)
    chead2 = models.CharField(max_length=5000)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.tilte