from django.db import models


# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    isdeleted = models.BooleanField(default=False)
    createdon = models.DateTimeField(auto_now_add=True)
    modifiedon = models.DateTimeField(auto_now=True)
    createdby = models.CharField(max_length=128, blank=True, null=True)
    modifiedby = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Report'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'