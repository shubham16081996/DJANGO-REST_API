# Generated by Django 3.1.3 on 2020-11-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201107_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmovies',
            name='Poster',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='allmovies',
            name='Type',
            field=models.CharField(default='Action', max_length=100),
        ),
    ]
