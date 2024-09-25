from django.db import models

# Create your models here.
class DbAllStocks(models.Model):
    id           = models.AutoField(primary_key=True, unique=True)
    code         = models.CharField(max_length=5)
    company_name = models.CharField(max_length=30)
    listing_board = models.CharField(max_length=15)

    def __str__(self):
        return self.code
    
    class Meta:
        db_table = "DbAllStocks"