# Generated by Django 4.1.7 on 2023-05-04 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_cringe_struka_smijer'),
    ]

    operations = [
        migrations.CreateModel(
            name='vijesti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('test', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Cringe',
        ),
    ]
