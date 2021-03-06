# Generated by Django 3.0.7 on 2021-01-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
