# Generated by Django 2.2 on 2019-06-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movid', models.CharField(default='!', max_length=80)),
                ('nota_usu', models.SmallIntegerField(default=0)),
                ('nota_meta', models.SmallIntegerField(default=0)),
                ('gen1', models.CharField(default='!', max_length=80)),
                ('gen2', models.CharField(default='!', max_length=80)),
                ('gen3', models.CharField(default='!', max_length=80)),
            ],
        ),
    ]