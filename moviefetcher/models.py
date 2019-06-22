from django.db import models


class Filme(models.Model):
    movid = models.CharField(max_length=80, default='!')
    nota_usu = models.SmallIntegerField(default=0)
    nota_meta = models.SmallIntegerField(default=0)

    gen1 = models.CharField(max_length=80, default='!')
    gen2 = models.CharField(max_length=80, default='!')
    gen3 = models.CharField(max_length=80, default='!')


