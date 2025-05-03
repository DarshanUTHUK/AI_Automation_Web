import random
import re

from faker import Faker

fake = Faker()

def generate_random_user_for_registration():
    """
    Generate random user details for registration.
    Returns Random user details for registration.
    """
    name = fake.first_name().lower()
    number = random.randint(10000, 99999)

    return name + str(number)
