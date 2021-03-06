from django.db import models

class Director(models.Model):
    name=models.CharField(max_length=100,unique=True)

class Actor(models.Model):
    actor_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)

class Movie(models.Model):
    name=models.CharField(max_length=100)
    movie_id=models.CharField(max_length=100,primary_key=True)
    release_date=models.DateField()
    actors=models.ManyToManyField(Actor,
                    through='Cast',
                    through_fields=('movie','actor'),
                    )
    box_office_collection_in_crores=models.FloatField()
    director=models.ForeignKey(
                Director,
                on_delete=models.CASCADE
                )
    
class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_debut_movie=models.BooleanField(default=False)
    role=models.CharField(max_length=50)
    
class Rating(models.Model):
    movie=models.OneToOneField(Movie,on_delete=models.CASCADE)
    rating_one_count=models.IntegerField(default=0)
    rating_two_count=models.IntegerField(default=0)
    rating_three_count=models.IntegerField(default=0)
    rating_four_count=models.IntegerField(default=0)
    rating_five_count=models.IntegerField(default=0)
