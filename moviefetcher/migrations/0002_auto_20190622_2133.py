# Generated by Django 2.2 on 2019-06-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviefetcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='movid',
            field=models.CharField(default='!', max_length=240),
        ),
    ]
