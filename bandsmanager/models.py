from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField('play date')

    def __str__(self):
        return self.name

class Vote(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.votes
