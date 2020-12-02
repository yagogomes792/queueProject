from django.db import models

# Create your models here.
class AddWaitTime(models.Model):

    endereco = models.CharField(max_length=400, null=False)
    data = models.DateField(null=False)
    tempo = models.FloatField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.endereco