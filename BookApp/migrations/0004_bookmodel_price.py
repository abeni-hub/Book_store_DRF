# Generated by Django 4.2.17 on 2024-12-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0003_delete_book_goodmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
