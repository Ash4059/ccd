# Generated by Django 3.0.4 on 2020-03-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cont3',
        ),
        migrations.AddField(
            model_name='post',
            name='cont0',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='cont1',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='cont2',
            field=models.CharField(default='', max_length=500),
        ),
    ]
