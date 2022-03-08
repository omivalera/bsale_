# Bsale_ Backend Doc

La implementación de esta API-REST fue mediante Django-rest y conectada una base de datos MySQL.

## Endpoints

```json
{
    "products": "https://testapibsale.herokuapp.com/products/?format=api",
    "groups": "https://testapibsale.herokuapp.com/categories/?format=api",
    "categories": "https://testapibsale.herokuapp.com/categories/?format=api"
}
```

/products/ 

- Se filtra por productos
- Se asignaron 12 cards por cada pagina
- Link donde visualizar:

[Product List](https://testapibsale.herokuapp.com/products/)

/groups/

- Se filtra por grupo
- link donde visualizar:

[Category List](https://testapibsale.herokuapp.com/categories/)

/categories/

- Se filtra por categoría
- Link donde visualizar:

[Category List](https://testapibsale.herokuapp.com/categories/)

# **Instalación en LOCAL**

Crear y activar entorno virtual

Instalar las dependencias

<aside>
🖥️ `pip install -r requirements.txt`

</aside>

Se ejecuta el server

<aside>
🖥️ `python manage.py runserver`

</aside>

Ve al navegador y entra en 

<aside>
🖥️ http://127.0.0.1:8000/

</aside>