# Bsale_ Backend Doc

La implementación de esta API-REST fue mediante Django-rest y conectada una base de datos MySQL.
[Heroku Deploy](https://testapibsale.herokuapp.com/)

## Endpoints

```json
{
    "list": "https://testapibsale.herokuapp.com/list/?format=api",
    "products": "https://testapibsale.herokuapp.com/products/?format=api",
    "groups": "https://testapibsale.herokuapp.com/groups/?format=api",
    "categories": "https://testapibsale.herokuapp.com/categories/?format=api"
    
}
```

/list/ 

- Se filtra por todos los productos y categorias
- Recibe como parametro {name} -ejemplo de uso : https://testapibsale.herokuapp.com/list/?search=mani
- Respuesta:
```json
{
            "id": 53,
            "name": "Mani Sin Sal",
            "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/manisinsalmp6988.jpg",
            "price": 500.0,
            "discount": 0,
            "category": {
                "id": 5,
                "name": "snack"
            
}
```
- Link donde visualizar:

[Productos y Categorias](https://testapibsale.herokuapp.com/list/)

/product/ 

- Se filtra por todos los productos
- Recibe como parametro {name} -ejemplo de uso : https://testapibsale.herokuapp.com/list/?search=coca
- Respuesta:
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 37,
            "name": "COCA COLA ZERO DESECHABLE",
            "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/cocazero9766.jpg",
            "price": 1490.0,
            "discount": 0,
            "category": {
                "id": 4,
                "name": "bebida"
            }
        },
        {
            "id": 57,
            "name": "COCA COLA NORMAL DESECHABLE 1500cc",
            "url_image": null,
            "price": 1500.0,
            "discount": 0,
            "category": {
                "id": 4,
                "name": "bebida"
            }
        },
        {
            "id": 58,
            "name": "COCA COLA LIGHT DESECHABLE",
            "url_image": null,
            "price": 1500.0,
            "discount": 0,
            "category": {
                "id": 4,
                "name": "bebida"
            }
```
- Link donde visualizar: 
- [Product List](https://testapibsale.herokuapp.com/list/)

/groups/
- Recibe como parametro {category_id} con valor Integer -ejemplo de uso : https://testapibsale.herokuapp.com/groups/2   

- Respuesta:

        
```json
{
            "pisco": [
                {
                    "id": 8,
                    "name": "PISCO ALTO DEL CARMEN 35º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/alto8532.jpg",
                    "price": 7990.0,
                    "discount": 10,
                    "category_id": 2
                },
                {
                    "id": 9,
                    "name": "PISCO ALTO DEL CARMEN 40º ",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/alto408581.jpg",
                    "price": 5990.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 10,
                    "name": "PISCO ARTESANOS 35º ",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/artesanos8818.jpg",
                    "price": 3990.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 11,
                    "name": "PISCO BAUZA 40º ",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/bauza408831.jpg",
                    "price": 4990.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 12,
                    "name": "PISCO CAMPANARIO 35º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/campanario8845.jpg",
                    "price": 2990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 13,
                    "name": "PISCO CAMPANARIO 40º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/campanario408881.jpg",
                    "price": 3990.0,
                    "discount": 20,
                    "category_id": 2
                },
            
```

- Se filtra por category_id de categoria
- link donde visualizar: 

[Category List](https://testapibsale.herokuapp.com/groups/)

/categories/
- Recibe como parametro {category_id} que tiene como valor un Integer -ejemplo de uso :https://testapibsale.herokuapp.com/categories/2
- Respuesta:
```json
{
    "id": 2,
    "name": "pisco"
}
```
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

