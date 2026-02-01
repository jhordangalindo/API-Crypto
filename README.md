# Crypto API 💰

## Descripción General

Crypto API es una aplicación desarrollada con **FastAPI** que consume la **API pública de CoinGecko** para obtener información actualizada sobre criptomonedas. Actúa como una capa intermedia que simplifica el acceso a datos financieros en tiempo real.

---

## ¿Qué información devuelve?

* Precio actual en USD
* Capitalización de mercado
* Variación porcentual en las últimas 24 horas

---

## Tecnologías Utilizadas

* **Python 3.10+**
* **FastAPI**
* **httpx** (cliente HTTP asíncrono)
* **Pydantic**
* **CoinGecko API**

---

## API Externa

**CoinGecko API (Pública)**

* URL base: `https://api.coingecko.com/api/v3`
* No requiere API Key
* Documentación oficial: [https://www.coingecko.com/en/api/documentation](https://www.coingecko.com/en/api/documentation)

---

## Endpoints de la Aplicación

### Obtener información de una criptomoneda

```
GET /api/crypto/{coin}
```

#### Ejemplo

```
GET http://127.0.0.1:8000/api/crypto/bitcoin

```

# ============================================================================
# ENDPOINT: OBTENER CRIPTOMONEDA POR ID
# ============================================================================
@router.get(
    "/{coin}",
    response_model=CryptoResponseDTO,
    summary="Consultar una criptomoneda",
    description="Obtiene precio, market cap y cambio 24h de una criptomoneda"
)
async def get_crypto(
    coin: str,
    http_client: httpx.AsyncClient = Depends(get_http_client)
):
    return await crypto_service.get_crypto(
        coin=coin,
        http_client=http_client
    )


#### Respuesta

```json
{
  "coin": "bitcoin",
  "price_usd": 43000,
  "market_cap_usd": 840000000000,
  "change_24h_percent": 2.5
}
```


#### Respuesta

```json
{
  "supported_coins": [
    "bitcoin",
    "ethereum",
    "solana",
    "cardano",
    "dogecoin"
  ]
}
```

---

## Manejo de Errores

| Código | Descripción                |
| ------ | -------------------------- |
| 400    | Petición inválida          |
| 404    | Criptomoneda no encontrada |
| 500    | Error interno              |
| 503    | CoinGecko no disponible    |

---

## Arquitectura del Proyecto

```
controllers/
 └── cryptocontroller.py
services/
 └── cryptoService.py
clients/
 └── cryptoClient.py
DTOs/
 └── cryptoDtos.py
```

Arquitectura basada en capas para mantener separación de responsabilidades.

---


```

<!-- Ejecutar servidor -->

```
uvicorn main:app --reload
```

---

## Documentación Automática

* Swagger UI: [http://127.0.0.1:8000/docs](http://localhost:8000/docs)

---

## Autor

* **Jhordan Galindo**
* Enero 2026

---

## Licencia

MIT License
