# Generated by Django 4.0.1 on 2022-02-17 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimerTabla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edit', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
