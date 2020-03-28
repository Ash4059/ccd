from django.db import models
import datetime
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    pubd=models.DateField(("Date"), default=datetime.date.today)
    title = models.CharField(max_length=50, default="")
    head0 = models.CharField(max_length=80, default="")
    head1 = models.CharField(max_length=80, default="")
    head2= models.CharField(max_length=80, default="")
    cont0 = models.CharField(max_length=300, default="")
    cont1 = models.CharField(max_length=400, default="")
    cont2 = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to="coffee/images/", default="")
    def __str__(self):
        return self.title