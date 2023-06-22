from django.db import models   


class Sucursal(models.Model):
    """Represents a bank branch.

    Attributes:
        name (CharField): Name of the branch.
        address (CharField): Address of the branch.

    Meta:
        db_table (str): Name of the table in the database.
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=False, null=False)
    
    class Meta:
        db_table = "sucursal"