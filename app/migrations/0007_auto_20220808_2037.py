# Generated by Django 3.2.1 on 2022-08-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_surfaces_glass_or_aluminium'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='color',
            new_name='standard_thinckness',
        ),
        migrations.RemoveField(
            model_name='product',
            name='opacity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tone_of_color',
        ),
        migrations.AlterField(
            model_name='product',
            name='deleted',
            field=models.IntegerField(default='0'),
        ),
    ]
