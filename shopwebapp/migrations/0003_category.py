# Generated by Django 2.0.13 on 2021-02-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopwebapp', '0002_auto_20210214_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
