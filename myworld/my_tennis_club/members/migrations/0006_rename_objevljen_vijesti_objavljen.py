# Generated by Django 4.1.7 on 2023-05-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_vijesti_objevljen_alter_vijesti_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vijesti',
            old_name='objevljen',
            new_name='objavljen',
        ),
    ]
