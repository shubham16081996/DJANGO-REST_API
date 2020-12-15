from django.db import models

# Create your models here.


class AllMovies(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=255)
    Duration = models.FloatField()
    Rating = models.FloatField()
    Type = models.CharField(max_length=100, default='Action')
    Year = models.IntegerField(default=2018)
    Poster = models.ImageField(upload_to='Images/', default="Images/None/Noimg.jpg")
