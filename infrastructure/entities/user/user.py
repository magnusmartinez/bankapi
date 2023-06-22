

from django.db import models
from django.contrib.auth.models import AbstractUser



def get_dynamic_image_filename(instance, filename):
    """Function to generate the dynamic path of the user's image file.

    Args:
        instance (User): Instance of the "User" model.
        filename (str): Name of the image file.

    Returns:
        str: Dynamic path of the image file.

    """
    print(instance)
    return f"user/image/{instance.id}/{filename}"


class User(AbstractUser):
    """
    Custom user model that extends the AbstractUser model provided by Django.

    Inherits the following fields from AbstractUser:
    - username: Required. 150 characters or fewer.
    - first_name: First name of the user (optional).
    - last_name: Last name of the user (optional).
    - email: Email address of the user (optional).
    - is_staff: Designates whether the user can access the admin site.
    - is_active: Designates whether the user is active.
    - date_joined: Date and time when the user joined.

    Additional field:
    - image: Profile image of the user.

    Meta:
        db_table (str): Name of the table in the database.

    """
    image = models.ImageField(blank=False, null=False, max_length=255, upload_to=get_dynamic_image_filename, default="user/image/default.png")
    
    class Meta:
        db_table = 'user'
        