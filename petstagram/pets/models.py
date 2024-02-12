from django.db import models
from django.utils.text import slugify


# null means it might be 'null' in our DB, depending on option chosen ('True'/'False')
# blank means we can give him an empty string, depending on option chosen ('True'/'False')


class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )  # 'True' because it is an optional parameter

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )  # null=False and blank=True is typically used for autogenerated stuff

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # we add it here, to be sure it generates a pk for the slug, instead of 'None'
        if not self.slug:  # slugify("My name") -> "My-name"
            self.slug = slugify(f'{self.name}-{self.pk}')

        super().save(*args, **kwargs)

