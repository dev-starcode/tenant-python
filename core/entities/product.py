from uuid import uuid4

class Product:
    def __init__(self, name: str, product_id: str = None):
        self.product_id = product_id or str(uuid4())
        self.name = name
