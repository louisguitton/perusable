# Generated by Django 3.1.7 on 2021-03-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='wines'),
        ),
    ]
