from flask import g, request
import psycopg2

def tenant_middleware(app):
    @app.before_request
    def set_tenant():
        tenant_name = request.headers.get("tenant")  

        if not tenant_name:
            return {"error": "Tenant not provided"}, 400

        g.tenant_name = tenant_name
        g.set_schema = lambda conn: conn.cursor().execute(f"SET search_path TO {tenant_name};")

