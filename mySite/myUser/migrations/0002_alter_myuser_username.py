# Generated by Django 3.2.9 on 2021-11-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]