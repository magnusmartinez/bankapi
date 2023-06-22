from django.db import models   

def get_dynamic_image_filename(instance, filename):
    """Function to generate the dynamic path of the client's image file.

    Args:
        instance (Client): Instance of the "Client" model.
        filename (str): Name of the image file.

    Returns:
        str: Dynamic path of the image file.

    """
    print(instance)
    return f"client/image/{instance.id}/{filename}"

GENDER_CHOICES = [
        ('M', 'masculino'),
        ('F', 'femenino')
]
MARITAL_STATUS_CHOICES = [
        ('MS1', 'soltero'),
        ('MS2', 'casado')
]


class Client(models.Model):  
    """Represents a client who is the owner of the account.

    Attributes:
        first_name (CharField): First name of the client.
        last_name (CharField): Last name of the client.
        sucursal (ForeignKey): Branch office associated with the client (related to the "Sucursal" model).
        gender (CharField): Gender of the client.
        address (CharField): Address of the client.
        image (ImageField): Profile image of the client.
        phone_number (CharField): Phone number of the client.
        email (EmailField): Email address of the client.
        dni (CharField): Identification number of the client.
        birthday (DateField): Birthday of the client.
        marital_status (CharField): Marital status of the client.
        occupation (CharField): Occupation of the client.
        place_of_birth (CharField): Place of birth of the client.
        is_active (BooleanField): Indicates if the client is active.
        create_at (DateField): Client creation date (auto-generated).
        update_at (DateField): Client last update date (auto-generated).

    Meta:
        db_table (str): Name of the table in the database.

    """
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    sucursal = models.ForeignKey("Sucursal", related_name="CLIENT_SUCURAL", on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=1, null=False, blank=False, choices=GENDER_CHOICES)
    address = models.CharField(max_length=125, blank=False, null=False, default="N/A")
    image = models.ImageField(blank=False, null=False, max_length=255, upload_to=get_dynamic_image_filename, default="client/image/default.png")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    dni = models.CharField(max_length=11, blank=False, null=False, unique=True)
    birthday = models.DateField(blank=True, null=True)
    marital_status = models.CharField(max_length=3, blank=False, null=False, choices=MARITAL_STATUS_CHOICES)
    occupation = models.CharField(max_length=50, blank=True, null=True, default="N/A")
    place_of_birth = models.CharField(max_length=50, blank=True, null=True, default="N/A")

    is_active =  models.BooleanField(default=True, blank=False, null=False)
    create_at = models.DateField(auto_now_add=True, editable=False)
    update_at = models.DateField(auto_now=True)


    class Meta:
        db_table = "client"
