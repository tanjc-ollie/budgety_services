from django.db import models

# Create your models here.
class LinkToken(models.Model):
    user_id = models.CharField(max_length=256)
    token = models.CharField(max_length=256)
    expiration = models.DateTimeField()

    class Meta:
        db_table = "link_token"

class Transaction(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.FloatField()

    class Meta:
        db_table = "transactions"
