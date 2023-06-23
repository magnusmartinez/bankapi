from django.db import models   


class Sucursal(models.Model):
    """Represents a bank branch.

    Attributes:
        name (CharField): Name of the branch.
        address (CharField): Address of the branch.
        is_active (BooleanField): Indicates if the branch is active or not. Represent deleted or not.
        create_at (DateTimeField): Date and time when the branch was created.
        update_at (DateTimeField): Date and time when the branch was updated.
    Meta:
        db_table (str): Name of the table in the database.
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=False, null=False)
    is_active =  models.BooleanField(default=True, blank=False, null=False)  
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)

    
    class Meta:
        db_table = "sucursal"