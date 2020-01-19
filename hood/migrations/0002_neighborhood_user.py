# Generated by Django 3.0.2 on 2020-01-19 22:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='hood.Profile'),
            preserve_default=False,
        ),
    ]
