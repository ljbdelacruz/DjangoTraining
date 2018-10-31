from django.db import models


class Users(model.Mod):
    name=models.CharField(max_length=70);
    def __str__(self):
        return self.name






