# Generated by Django 3.1 on 2020-08-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
