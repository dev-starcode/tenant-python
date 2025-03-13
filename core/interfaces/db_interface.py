from abc import ABC, abstractmethod

class DBInterface(ABC):
    @abstractmethod
    def create_schema(self ):
        pass

    @abstractmethod
    def create_table(self ):
        pass

    @abstractmethod
    def add_product(self, product_name: str):
        pass

    @abstractmethod
    def list_products(self):
        pass
