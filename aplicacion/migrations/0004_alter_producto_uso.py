# Generated by Django 4.2.4 on 2023-09-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='uso',
            field=models.CharField(max_length=200),
        ),
    ]
