from django.db import models

# Create your models here.
class LinkToken(models.Model):
    user_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    expiration = models.DateTimeField()

    class Meta:
        db_table = "link_token"

class Transaction(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.FloatField()

    class Meta:
        db_table = "transactions"

class Institution(models.Model):
    institution_id = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)

    class Meta:
        db_table = "institution"

class AccessToken(models.Model):
    token = models.CharField(max_length=255)

    class Meta:
        db_table="access_token"