# Generated by Django 4.0.3 on 2022-04-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closet_api', '0002_alter_clothing_attire_alter_clothing_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='image',
            field=models.CharField(default='Enter color based on color type. See Attached Image', max_length=255),
        ),
    ]