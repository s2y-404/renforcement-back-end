# Generated by Django 5.1.2 on 2024-10-18 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('biographie', models.TextField()),
                ('date_de_naissance', models.DateField()),
                ('date_de_décès', models.DateField(blank=True, null=True)),
                ('nationalité', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos_auteurs/')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('site_web', models.URLField(blank=True, null=True)),
                ('email_contact', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_editeurs/')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('date_évaluation', models.DateTimeField(auto_now_add=True)),
                ('recommandé', models.BooleanField(default=False)),
                ('titre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('résumé', models.TextField()),
                ('date_de_publication', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('nombre_de_pages', models.IntegerField()),
                ('langue', models.CharField(max_length=100)),
                ('image_de_couverture', models.ImageField(blank=True, null=True, upload_to='couvertures_livres/')),
                ('format', models.CharField(max_length=50)),
                ('auteurs', models.ManyToManyField(related_name='livres', to='renforcementbackend.auteur')),
                ('categories', models.ManyToManyField(related_name='livres', to='renforcementbackend.categorie')),
                ('editeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='renforcementbackend.editeur')),
            ],
        ),
        migrations.CreateModel(
            name='Exemplaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('état', models.CharField(max_length=50)),
                ('date_acquisition', models.DateField()),
                ('localisation', models.CharField(max_length=100)),
                ('disponibilité', models.BooleanField(default=True)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renforcementbackend.livre')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField(auto_now_add=True)),
                ('date_retour_prévue', models.DateTimeField()),
                ('date_retour_effective', models.DateTimeField(blank=True, null=True)),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('termine', 'Terminé'), ('en_retard', 'En retard')], max_length=50)),
                ('remarques', models.TextField(blank=True, null=True)),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emprunt_user', to=settings.AUTH_USER_MODEL)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunt_livre', to='renforcementbackend.livre')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('visible', models.BooleanField(default=True)),
                ('modéré', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_user', to=settings.AUTH_USER_MODEL)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_livre', to='renforcementbackend.livre')),
            ],
        ),
    ]
