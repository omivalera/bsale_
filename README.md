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
- Link donde visualizar =

[Product List](https://testapibsale.herokuapp.com/products/)

/groups/

- Se filtra por grupo
- link donde visualizar =

[Category List](https://testapibsale.herokuapp.com/categories/)

/categories/

- Se filtra por categoría
- Link donde visualizar =

[Category List](https://testapibsale.herokuapp.com/categories/)

# **Instalación en LOCAL**

Al clonar el repositorio y antes de inicializar el server es MUY IMPORTANTE

<aside>
🚨 Eliminar el archivo **`bs-config.js` este forma parte del deploy en remoto**

</aside>

<aside>
🚨 Cambiar en el archivo `scripts.js`la variable `base_URL` que vendrá con el valor del deploy. 
Se debe colocar en su lugar  “http://127.0.0.1:8000/”

</aside>

Instalar las dependencias con 

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