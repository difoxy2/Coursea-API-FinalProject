# Generated by Django 5.1.1 on 2024-10-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='featured',
            field=models.BooleanField(db_index=True),
        ),
    ]
