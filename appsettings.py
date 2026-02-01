"""
=============================================================================
CONFIGURACIÓN CENTRALIZADA DE LA APLICACIÓN
=============================================================================

Este módulo contiene la configuración global de la aplicación, cargando
las variables de entorno desde el archivo .env y exponiendo constantes
de configuración.

En este proyecto se utiliza la API pública de CoinGecko para obtener
datos de criptomonedas (precio actual, mercado, etc.).

¿Por qué usar un archivo de configuración centralizado?
-------------------------------------------------------
1. FLEXIBILIDAD: Cambiar URLs o timeouts sin modificar código
2. MANTENIBILIDAD: Un solo lugar para toda la configuración
3. ESCALABILIDAD: Fácil adaptación a otros entornos
4. BUENAS PRÁCTICAS: Separación clara entre lógica y configuración

Contenido del archivo .env (ejemplo):
-------------------------------------
COINGECKO_BASE_URL=https://api.coingecko.com/api/v3

IMPORTANTE:
- CoinGecko NO requiere API KEY
- El archivo .env NUNCA debe subirse a Git

Autor: [Tu nombre]
Fecha: Enero 2026
=============================================================================
"""

import os
from dotenv import load_dotenv


# =============================================================================
# CARGAR VARIABLES DE ENTORNO
# =============================================================================
load_dotenv()


class AppSettings:
    """
    Clase de configuración que contiene todas las constantes de la aplicación.

    Todos los atributos son de clase (class attributes), por lo que se acceden
    directamente sin crear una instancia.

    Ejemplo:
        from appsettings import AppSettings
        base_url = AppSettings.COINGECKO_BASE_URL
    """

    # =========================================================================
    # CONFIGURACIÓN DE LA API DE COINGECKO
    # =========================================================================

    # URL base de la API de CoinGecko
    # Documentación oficial: https://www.coingecko.com/en/api/documentation
    COINGECKO_BASE_URL = os.getenv(
        "COINGECKO_BASE_URL",
        "https://api.coingecko.com/api/v3"
    )

    # Endpoint para obtener precios simples de criptomonedas
    # Ejemplo:
    # /simple/price?ids=bitcoin&vs_currencies=usd
    COINGECKO_SIMPLE_PRICE_ENDPOINT = "/simple/price"

    # =========================================================================
    # CONFIGURACIÓN DE LLAMADAS HTTP
    # =========================================================================

    # Tiempo máximo de espera para peticiones HTTP (en segundos)
    TIMEOUT_SECONDS = 10

    # Moneda por defecto para consultar precios
    # CoinGecko soporta: usd, eur, cop, ars, mxn, etc.
    DEFAULT_CURRENCY = "usd"
