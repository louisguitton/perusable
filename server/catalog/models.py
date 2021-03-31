import uuid

from django.db import models
from django.contrib.postgres import indexes

class Wine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    variety = models.CharField(max_length=255)
    winery = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True, upload_to='wines')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        indexes = [
            indexes.GinIndex(
                name='catalog_wine_variety_gin_idx', 
                fields=['variety'], 
                opclasses=['gin_trgm_ops'],
            ),
            indexes.GinIndex(
                name='catalog_wine_winery_gin_idx', 
                fields=['winery'], 
                opclasses=['gin_trgm_ops'],
            ),
            indexes.GinIndex(
                name='catalog_wine_desc_gin_idx', 
                fields=['description'], 
                opclasses=['gin_trgm_ops'],
            ),
        ]
