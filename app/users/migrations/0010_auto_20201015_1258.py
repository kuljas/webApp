# Generated by Django 3.1.2 on 2020-10-15 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_auto_20201015_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bider',
            name='korisnik',
        ),
        migrations.RemoveField(
            model_name='oglasivac',
            name='korisnik',
        ),
        migrations.AddField(
            model_name='bider',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oglasivac',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]