# Generated by Django 4.2.1 on 2023-06-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_delete_likeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]
