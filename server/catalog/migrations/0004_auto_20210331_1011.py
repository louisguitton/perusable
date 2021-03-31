# Generated by Django 3.1.7 on 2021-03-31 10:11

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_trigram_extension'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='wine',
            index=django.contrib.postgres.indexes.GinIndex(fields=['variety'], name='catalog_wine_variety_gin_idx', opclasses=['gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='wine',
            index=django.contrib.postgres.indexes.GinIndex(fields=['winery'], name='catalog_wine_winery_gin_idx', opclasses=['gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='wine',
            index=django.contrib.postgres.indexes.GinIndex(fields=['description'], name='catalog_wine_desc_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]
