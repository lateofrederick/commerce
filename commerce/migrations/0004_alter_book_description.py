# Generated by Django 3.2 on 2022-09-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
