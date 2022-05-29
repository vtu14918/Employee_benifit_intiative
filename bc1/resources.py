from import_export import resources
from .models import Data_store
class DataResource(resources.ModelResource):
    class meta:
        model=Data_store