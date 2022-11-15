from django.db import models
from apps.categories.models import Category
from apps.settings.models import Currency

# Create your models here.
class Courses(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()

    image = models.ImageField(
        upload_to= "course_image/"
    )
    price = models.IntegerField(
    )
    category = models.ForeignKey(
        Category,
        max_length=255,
        on_delete=models.CASCADE,
        related_name="courses_category",
        verbose_name="Kатегории курсов"
    )
    currency = models.ForeignKey(
        Currency,
        on_delete = models.CASCADE,
        related_name = "course_currency"
    )
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
