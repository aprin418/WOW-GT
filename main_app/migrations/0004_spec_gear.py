# Generated by Django 3.2.4 on 2021-06-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_gear'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='gear',
            field=models.ManyToManyField(to='main_app.Gear'),
        ),
    ]
