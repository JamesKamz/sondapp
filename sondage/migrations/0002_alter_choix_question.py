# Generated by Django 4.2 on 2023-04-16 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sondage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choix',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choix', to='sondage.question'),
        ),
    ]