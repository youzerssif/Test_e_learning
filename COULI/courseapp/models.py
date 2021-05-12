from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Formateur(models.Model):
    """Model definition for Formateur."""

    # TODO: Define fields here
    GENRE = [
        ('F', 'Femme'),
        ('M', 'Homme'),

    ]
    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auteur')
    photo_profile = models.FileField(upload_to='photo', null='True')
    adresse = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, choices=GENRE)
    contact = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, null=True, blank=True)

    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.user.username)))
        super(Formateur, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Formateur."""

        verbose_name = 'Formateur'
        verbose_name_plural = 'Formateurs'

    def __str__(self):
        """Unicode representation of Formateur."""
        return self.user.username




class Cours(models.Model):
    """Model definition for Cours."""

    # TODO: Define fields here
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE, related_name="formateur_cours")
    titre = models.CharField(max_length=255, null=True)
    description = models.TextField()
    image = models.FileField(upload_to="cours_image", null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.titre)))
        super(Cours, self).save(*args, **kwargs)
    

    class Meta:
        """Meta definition for Cours."""

        ordering = ['-date_add',]
        verbose_name = 'Cours'
        verbose_name_plural = 'Courss'

    def __str__(self):
        """Unicode representation of Cours."""
        return self.titre


class Chapitre(models.Model):
    """Model definition for Chapitre."""

    # TODO: Define fields here
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="chapitre_cours")
    titre = models.CharField(max_length=255, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
            self.slug = '-'.join((slugify(self.titre)))
            super(Chapitre, self).save(*args, **kwargs)
    
    
    class Meta:
        """Meta definition for Chapitre."""

        verbose_name = 'Chapitre'
        verbose_name_plural = 'Chapitres'

    def __str__(self):
        """Unicode representation of Chapitre."""
        return self.titre
