from django.db import models

class Review(models.Model):
    text = models.TextField()
    rating = models.FloatField()
    sentiment = models.CharField(max_length=10)  # "positive" или "negative"
