from django.db import models

STATUS_CHOICES = [       
    ("S01", "pending"),         
    ("S02", "completed"),         
    ("S03", "canceled"),         
]

TRANSACTION_TYPES_CHOICES = [
    ("T001", "deposit"),
    ("T002", "withdrawal")
]

ORIGIN_CHOICES = [
    ("C001", "bank teller"),
    ("C002", "atm"),
]

class Transaction(models.Model):
    """Model representing a bank transaction.

    Attributes:
        origin (CharField): The origin from which the transaction originates.
        destination_account (Account): The destination account of the transaction (foreign key to Account model).
        amount (DecimalField): The amount of the transaction.
        commission (FloatField): The commission associated with the transaction.
        status (str): The status of the transaction. Choices are "pending", "completed", or "canceled".
        is_active (bool): Indicates whether the transaction is active.
        create_at (DateTimeField): The date and time of the transaction creation (auto-generated on creation).
        description (str): A description of the transaction.
        transaction_type (str): The type of transaction. Choices are "personal account" or "company account".
        reference_number (str): The unique reference number of the transaction.
        additional_notes (str): Additional notes or information related to the transaction.

    Meta:
        db_table (str): The name of the database table for the Transaction model.
    """

    origin = models.CharField(max_length=4, choices=ORIGIN_CHOICES, default=ORIGIN_CHOICES[0][0])
    destination_account = models.ForeignKey("Account", related_name="TRANSACTION_DESTINATION_ACCOUNT", on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="S01")
    is_active =  models.BooleanField(default=True, blank=False, null=False)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=255, blank=True, default="N/A")
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES_CHOICES)
    commission = models.FloatField(blank=False, null=False, editable=False)
    reference_number = models.CharField(max_length=16, blank=False, null=False, unique=True)
    additional_notes = models.TextField(blank=True, default="N/A")

    class Meta:
        db_table = "transaction"
