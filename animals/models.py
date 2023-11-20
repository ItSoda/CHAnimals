from django.db import models

from users.models import Users


class Images(models.Model):
    """Model for one images"""

    name = models.CharField("Название", max_length=100)
    image = models.ImageField(upload_to="all_images")

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Name: {self.name}"


class Animals(models.Model):
    """Model for one animal"""

    name = models.CharField("Имя", max_length=120)
    species = models.CharField("Порода", max_length=200)
    age = models.PositiveIntegerField(default=0)
    content = models.TextField()
    images = models.ManyToManyField(to=Images)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "животное"
        verbose_name_plural = "Животные"

    def __str__(self) -> str:
        return f"Name: {self.name} | species: {self.species}"
