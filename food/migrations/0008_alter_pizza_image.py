# Generated by Django 5.1.4 on 2024-12-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_alter_pizza_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
