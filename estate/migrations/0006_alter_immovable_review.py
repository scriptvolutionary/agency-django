# Generated by Django 4.1.3 on 2022-11-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_alter_contract_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immovable',
            name='review',
            field=models.ImageField(upload_to='estate/static/immovables', verbose_name='Фотография'),
        ),
    ]