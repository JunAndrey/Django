from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    class Meta:
        verbose_name = ["phone"]

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)


    def __str__(self):
        return self.name

