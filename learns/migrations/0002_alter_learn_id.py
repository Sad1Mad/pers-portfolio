# Generated by Django 4.1 on 2022-08-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
