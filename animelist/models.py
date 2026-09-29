from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    submitted_by = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submitted_by} on {self.anime.title}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
