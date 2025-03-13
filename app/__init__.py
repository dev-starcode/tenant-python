from flask import Flask
from presentation.tenant_middleware import tenant_middleware
from presentation.routes import products_bp

def create_app():
    app = Flask(__name__)

    # Registra o middleware para configurar o tenant
    tenant_middleware(app)

    # Registra as rotas
    app.register_blueprint(products_bp)

    return app
