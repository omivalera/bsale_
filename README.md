# Bsale_ Backend Doc

La implementación de esta API-REST fue mediante Django-rest y conectada una base de datos MySQL.

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
- Respuesta desde: https://testapibsale.herokuapp.com/list/?search=mani
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
- Respuesta desde: https://testapibsale.herokuapp.com/list/?search=coca
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

- Respuesta desde: https://testapibsale.herokuapp.com/groups/2 

        
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
                {
                    "id": 14,
                    "name": "PISCO ESPIRITU DEL ELQUI 40º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/espiritu8936.jpg",
                    "price": 5990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 15,
                    "name": "PISCO ESPIRITU DEL ELQUI 45º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/espiritu8957.jpg",
                    "price": 6990.0,
                    "discount": 5,
                    "category_id": 2
                },
                {
                    "id": 16,
                    "name": "PISCO HORCON QUEMADO 35º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/horcon359049.jpg",
                    "price": 6990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 17,
                    "name": "PISCO HORCON QUEMADO 40º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/horcon409062.jpg",
                    "price": 7990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 18,
                    "name": "PISCO HORCON QUEMADO 46º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/horcon469075.jpg",
                    "price": 8990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 19,
                    "name": "PISCO MISTRAL 35º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/mistral359200.jpg",
                    "price": 4990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 20,
                    "name": "PISCO MISTRAL 40º ",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/mistral409215.jpg",
                    "price": 4990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 21,
                    "name": "PISCO TRES ERRES 35º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/rrr359305.jpg",
                    "price": 4590.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 22,
                    "name": "PISCO TRES ERRES 40º",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/rrr409319.jpg",
                    "price": 4990.0,
                    "discount": 20,
                    "category_id": 2
                },
                {
                    "id": 87,
                    "name": "PISCO MISTRAL 35°",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/358978.jpg",
                    "price": 4990.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 88,
                    "name": "PISCO MISTRAL GRAN NOBEL 40°",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/grannobel9104.jpg",
                    "price": 19900.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 89,
                    "name": "PISCO MISTRAL 40°",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/409346.jpg",
                    "price": 4990.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 90,
                    "name": "PISCO MISTRAL 46°",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/469463.jpg",
                    "price": 7890.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 91,
                    "name": "PISCO MISTRAL NOBEL 40°",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/nobel409551.jpg",
                    "price": 19990.0,
                    "discount": 0,
                    "category_id": 2
                },
                {
                    "id": 92,
                    "name": "PISCO MISTRAL NOBEL 46",
                    "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/nobelanejado9639.jpg",
                    "price": 15990.0,
                    "discount": 15,
                    "category_id": 2
                }
```

- Se filtra por category_id de categoria
- link donde visualizar: 

[Category List](https://testapibsale.herokuapp.com/groups/)

/categories/
- Recibe como parametro {category_id} que tiene como valor un Integer -ejemplo de uso :https://testapibsale.herokuapp.com/categories/2
- Respuesta desde https://testapibsale.herokuapp.com/categories/2
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

