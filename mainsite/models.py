from django.db import models

# Create your models here.
class Solutions(models.Model):
    id = models.IntegerField(primary_key=True)
    Location = models.CharField()
    description = models.CharField()
    Cost = models.IntegerField()
    free_or_not = models.BooleanField(default=False)
    image = models.CharField()
    class Meta:
        db_table = 'solutions'

    def __str__(self):
        return self.Location

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    email = models.CharField()
    password = models.CharField()
    phone = models.CharField()
    adress = models.CharField()
    gender = models.CharField()
    age = models.CharField()
    is_admin = models.BooleanField()
    last_name = models.CharField()
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name