
from django.db import models
from application.use_case.utils import constants as cts

ACCOUNT_TYPES_CHOICES = [
    ("A001", "personal account"),
    ("A002", "company account"),
]

class Account(models.Model):
    """Represents a bank account.

    Attributes:
        owner (ForeignKey): Owner of the account (related to the "Client" model).
        balance (FloatField): Account balance.
        number (CharField): Account number.
        type (CharField): Account type (personal or company).
        is_active (BooleanField): Indicates if the account is active.
        create_at (DateField): Account creation date (auto-generated).
        update_at (DateField): Account last update date (auto-generated).

    Meta:
        db_table (str): Name of the table in the database.

    """
    owner = models.ForeignKey("Client", related_name="ACCOUNT_OWNER", on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False, default=cts.DIFAULT_BALANCE_ACCOUNT)
    number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    account_type = models.CharField(max_length=4, choices=ACCOUNT_TYPES_CHOICES, default=ACCOUNT_TYPES_CHOICES[0][0])
    is_active = models.BooleanField(default=True, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, editable=False)
    update_at = models.DateField(auto_now=True)
    

    class Meta:
        db_table = "account"
        