from django.db import models


class GameType(models.Model):
    """Game Type model
    """

    label = models.CharField(max_length=50)
