"""
=============================================================================
PUNTO DE ENTRADA DE LA APLICACIÓN FASTAPI
=============================================================================

Este es el archivo principal de la aplicación. Aquí se configura e inicializa
la instancia de FastAPI y se registran todos los routers (controladores).

FastAPI es un framework moderno y de alto rendimiento para construir APIs
con Python 3.7+ basado en estándares como OpenAPI y JSON Schema.

Autor: Jordan Galindo
Fecha: Enero 2026
=============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importamos el router del controlador de criptomonedas
from controllers.cryptocontroller import router as crypto_router


# =============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =============================================================================
app = FastAPI(
    title="Crypto API",
    description="""
    ## API de Criptomonedas 💰

    Esta API permite consultar información en tiempo real sobre criptomonedas
    como Bitcoin, Ethereum y otras, utilizando la API pública de CoinGecko.

    ### Funcionalidades:
    * Consultar precio actual en USD
    * Ver capitalización de mercado
    * Consultar variación porcentual en 24 horas

    ### Tecnologías utilizadas:
    * FastAPI
    * httpx
    * Pydantic
    * CoinGecko API
    """,
    version="1.0.0"
)


# =============================================================================
# CONFIGURACIÓN DE CORS (IMPORTANTE)
# =============================================================================
# Permite que la API sea consumida desde:
# - Navegadores
# - Frontend (React, Vue, etc.)
# - Swagger UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # En producción, limitar dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =============================================================================
# ENDPOINT RAÍZ (HOME)
# =============================================================================
@app.get(
    "/",
    summary="Página de inicio",
    description="Endpoint de bienvenida que confirma que la API está funcionando",
    tags=["General"]
)
def home():
    """
    Endpoint de bienvenida.

    Returns:
        dict: Información básica de la API
    """
    return {
        "message": "Welcome to the Crypto API 🚀",
        "status": "API funcionando correctamente",
        "docs": "/docs",
        "endpoints": {
            "crypto": "/api/crypto/{coin}"
        },
        "version": "1.0.0"
    }


# =============================================================================
# REGISTRO DE ROUTERS
# =============================================================================
# Aquí se registran todos los controladores de la aplicación
# Ejemplo de rutas disponibles:
# - GET /api/crypto/bitcoin
# - GET /api/crypto/ethereum
app.include_router(crypto_router)


# =============================================================================
# EJECUCIÓN EN DESARROLLO
# =============================================================================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
