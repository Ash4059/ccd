# Generated by Django 3.0.4 on 2020-03-27 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200327_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cont0',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='head0',
            field=models.CharField(default='', max_length=80),
        ),
    ]
