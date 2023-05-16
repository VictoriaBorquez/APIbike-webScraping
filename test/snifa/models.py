from django.db import models

class Result(models.Model):
    proceedings = models.CharField(max_length=200)
    auditable_unit = models.CharField(max_length=200)
    url_auditable_unit = models.URLField()
    name_social_reason = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    detail = models.URLField()

