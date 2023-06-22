from django.db import models

STATUS_CHOICES = [       
    ("S01", "pending"),         
    ("S02", "completed"),         
    ("S03", "canceled"),         
]

class Transfer(models.Model):
    """
    Model representing a bank transfer.

    Attributes:
        source_account (Account): The source account from which the transfer is made.
        destination_account (Account): The destination account to which the transfer is sent.
        amount (DecimalField): The amount of the transfer.
        create_at (DateTimeField): The date and time when the transfer was initiated.
        description (TextField): Optional description or reason for the transfer.
        status (CharField): The status of the transfer.
        reference (CharField): Optional reference associated with the transfer.
        code (CharField): Code associated with the transfer. It is unique by transfer
        commission (FloatField): Commission applied to the transfer
    Meta:
        db_table (str): The name of the table in the database.
    """
    source_account = models.ForeignKey("Account", related_name="TRANSFERS_SOURCE_ACCOUNT", on_delete=models.DO_NOTHING)
    destination_account = models.ForeignKey("Account", related_name="TRANSFERS_DESTINATION_ACCOUNT", on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="S02")
    reference = models.CharField(max_length=50, blank=True, null=True, default="N/A")
    code = models.CharField(max_length=16, blank=False, null=False, unique=True)
    commission = models.FloatField(blank=False, null=False, editable=False)
    is_active =  models.BooleanField(default=True, blank=False, null=False)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "transfer"