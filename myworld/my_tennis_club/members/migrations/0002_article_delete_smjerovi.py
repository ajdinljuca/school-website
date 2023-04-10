# Generated by Django 4.1.7 on 2023-04-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('published', models.DateField(null=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='img/')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Smjerovi',
        ),
    ]
