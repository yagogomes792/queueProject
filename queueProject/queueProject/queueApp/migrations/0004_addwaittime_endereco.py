# Generated by Django 3.1.3 on 2020-12-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queueApp', '0003_addwaittime'),
    ]

    operations = [
        migrations.AddField(
            model_name='addwaittime',
            name='endereco',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
