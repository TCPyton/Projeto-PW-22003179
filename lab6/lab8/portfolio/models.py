from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
      author =  models.CharField(max_length = 60)
      data = models.DateField(default=datetime.now)
      title = models.CharField(max_length=30)
      description = models.CharField(max_length= 1000)
      link = models.URLField(default= 'www.google.com')
      image = models.ImageField(default = '')
      date_criated = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.title[:30]

class QuizzScore(models.Model):
        name = models.CharField(max_length=20)
        score = models.IntegerField() 

        def __str__(self):
            return f"{self.name};{self.score}"

class Quizz(models.Model):
    name = models.CharField(max_length = 40)
    question1 = models.CharField(max_length = 20)
    question2 = models.BooleanField(default=True)
    question3 = models.BooleanField(default=True)
    question4 = models.CharField(max_length = 30)
    question5 = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name}"