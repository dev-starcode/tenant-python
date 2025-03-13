from interfaces.db_interface import DBInterface

class ProductUseCase(DBInterface):
    
    def __init__(self, DBInterface):
        self.repository = DBInterface

    def add_product(self, product_name):
        # self.repository.
        # Adiciona o produto no banco de dados (implemente a lógica aqui)
        pass

    def list_products(self):
        # Garantir que o schema esteja configurado
        # self.repository.
        
        # Busca os produtos no banco de dados
        return self.repository.fetch_all("SELECT * FROM products")
