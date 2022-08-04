from django.db import models

class Product(models.Model):

    product_url_image = models.CharField(max_length=200, blank=False, null=False)
    product_url = models.CharField(max_length=200, blank=False, null=False)
    product_url_created_at = models.CharField(max_length=200, blank=False, null=False)
    vendas_no_dia = models.IntegerField(blank=True, null=True)
    consult_date = models.DateField(null=True)
    total_vendas = models.IntegerField(null=True)

    def __str__(self):
        return self.product_url
