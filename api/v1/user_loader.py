from models import storage
from models.farmer import Farmer

def load_user(farmer_id, storage):
    """
       Function that will handle farmer
    """
    farmer = storage.get(Farmer, farmer_id)
    return farmer if farmer else None
