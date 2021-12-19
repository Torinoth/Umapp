from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.template.defaultfilters import slugify


class UmaGirl(models.Model):
    name = models.CharField(
        verbose_name="名前",
        max_length=200,
        help_text="",
    )

    nameEN = models.CharField(
        verbose_name="名前(英語)",
        max_length=200,
        help_text="",
    )

    birthday = models.DateField(
        verbose_name="誕生日",
        help_text="",
    )

    height = models.PositiveSmallIntegerField(
        verbose_name="身長",
        validators=[
            MinValueValidator(140),
            MaxValueValidator(200),
        ]
    )

    weight = models.CharField(
        verbose_name="体重",
        max_length=200,
        help_text="",
    )

    breast = models.PositiveSmallIntegerField(
        verbose_name="胸囲",
        validators=[
            MinValueValidator(70),
            MaxValueValidator(120),
        ]
    )

    waist = models.PositiveSmallIntegerField(
        verbose_name="腰囲",
        validators=[
            MinValueValidator(40),
            MaxValueValidator(100),
        ]
    )

    hip = models.PositiveSmallIntegerField(
        verbose_name="臀囲",
        validators=[
            MinValueValidator(70),
            MaxValueValidator(120),
        ]
    )

    icon = models.ImageField(
        verbose_name="アイコン",
        upload_to='icons/',
        null=True,
        blank=True,
    )

    draftImage = models.ImageField(
        verbose_name="原案",
        upload_to='draftImage/',
        null=True,
        blank=True,
    )

    memo = models.TextField(
        verbose_name="備考",
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('umapp:UmaGirlDetail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            n = self.nameEN.replace(' ', '_')
            self.slug = slugify(n)
        return super().save(*args, **kwargs)
