# Generated by Django 3.1.2 on 2020-10-15 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201014_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponuda', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.korisnik')),
            ],
        ),
        migrations.CreateModel(
            name='Oglasivac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.korisnik')),
            ],
        ),
        migrations.RemoveField(
            model_name='predmet',
            name='korisnik',
        ),
        migrations.DeleteModel(
            name='Aukcija',
        ),
        migrations.AddField(
            model_name='bid',
            name='bider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.bider'),
        ),
        migrations.AddField(
            model_name='bid',
            name='predmet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.predmet'),
        ),
        migrations.AddField(
            model_name='predmet',
            name='bideri',
            field=models.ManyToManyField(to='users.Bider'),
        ),
        migrations.AddField(
            model_name='predmet',
            name='oglasivac',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.oglasivac'),
        ),
    ]
