# Generated by Django 5.0.6 on 2024-05-30 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionBoulangerie', '0002_alter_approvisionnement_semaine_appro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livraison',
            name='date_livraison',
            field=models.IntegerField(),
        ),
    ]
