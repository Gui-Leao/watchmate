from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length = 30)
    about = models.CharField(max_length = 150)
    website = models.URLField(max_length = 100)
    
    def __str__(self):
        return self.name

# def validate_one_digit(value):
#     if len(str(value)) != 1:
#         raise ValidationError(
#             f'{value} não é um número inteiro de um dígito'
#         )

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform,on_delete = models.CASCADE,related_name = "watchlist",null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    #nada = models.IntegerField(default=0,validators =[validate_one_digit] )
    #askaas = models.CharField(max_length=50,default='nada')
    #ano = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],default = 0)
    
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators =[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null =True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE,related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+ "|" + self.watchlist.title 