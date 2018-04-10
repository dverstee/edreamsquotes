from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    quoter = models.CharField(max_length=200)
    quotee = models.CharField(max_length=200)

    def __str__(self):
        return self.quote_text