from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    brand_code = models.CharField(max_length=50)
    brand_image = models.ImageField(upload_to="Brand/Images", blank=True)

    def __str__(self) -> str:
        return f"{self.brand_name}"

    class Meta:
        db_table = "Brand"
