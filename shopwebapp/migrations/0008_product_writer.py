# Generated by Django 2.0.13 on 2021-02-13 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopwebapp', '0007_auto_20210214_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='shopwebapp.Category'),
        ),
    ]
