# API Proyecto: Euro 2024 ⚽️

## Equipos

Deberá hacer una petición GET al url [https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json](https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json)

Tendrá una respuesta conformada por una lista de diccionarios, los cuales tienen la siguiente estructura:

```json
[
  {
    "id": "31c88261-1efd-444e-95ac-b7c1cd034bfd",
    "code": "GER",
    "name": "Germany",
    "group": "A"
  }
]
```

## Estadios y Restaurantes

Deberá hacer una petición GET al url [https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json](https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json)

Tendrá una respuesta conformada por una lista de diccionarios, los cuales tienen la siguiente estructura:

```json
[
  {
    "id": "c8d1b19a-8262-4699-b7cb-7f0ed8659079",
    "name": "Estadio Olímpico de Berlín",
    "city": "Berlín",
    "capacity": [849, 241],
    "restaurants": [
      {
        "name": "Armas y Montemayor",
        "products": [
          {
            "name": "Artesanal Metal Bacon",
            "quantity": 10132,
            "price": "522.00",
            "adicional": "non-alcoholic",
            "stock": 15
          }
        ]
      }
    ]
  }
]
```

La capacidad del estadio esta data de la forma `[general, vip]` lo que significa que el primer elemento de la lista son la cantidad de boletos de la sección general y el segundo la cantidad de boletos VIP. Todas las filas del estadio serán de 10 asientos.

En adicional, se encuentra la información `adicional` referente a `alcoholic`, `non-alcoholic`, `package` y `plate`

## Partidos

Deberá hacer una petición GET al url [[https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/](https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/)matches.json](https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json)

Tendrá una respuesta conformada por una lista de diccionarios, los cuales tienen la siguiente estructura:

```json
[
  {
    "id": "75b9a987-38a0-4470-8b6c-3d7e7efe18a1",
    "number": 1,
    "home": {
      "id": "a4d9cfd7-ee66-42c5-a863-06e2426f12ab",
      "code": "GER",
      "name": "Germany"
    },
    "away": {
      "id": "021b109e-0fa6-451a-b78e-38f43548130f",
      "code": "SCO",
      "name": "Scotland"
    },
    "date": "2024-06-14",
    "group": "Group A"
  }
  // ...
]
```
