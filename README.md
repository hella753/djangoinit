# Django Init Project

## Description
This project is a simple clothing store website. It has a homepage, category pages, orders page and order detail page.
Project uses Django and sqlite3 database.

Project Structure:
```
djangoinit/
├── djangoinit
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── order
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── store
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

```

Database name: `db` <br>
Tables created: `order_order` and `store_category`<br>

Primary keys: `order_id` and `category_id` <br>
Foreign keys in `order_order`: `order_customer_id`, `order_category_id`<br>

Each table has 3 records for testing purposes.

Table Structures:

**order_order:**

| order_id | order_date | order_status | product_id     | product_quantity | order_total | order_customer_id | order_address | order_category_id |
|----------|------------|--------------|----------------|------------------|-------------|-------------------|---------------|-------------------|
| 1        | _date_     | _status_     | _id_           |   _quantity_     | _total_     | _customer_id_     | _address_     | _category_id_     |

**store_category:**

| category_id | category_name | category_description | category_product_count | category_image |
|-------------|---------------|----------------------|------------------------|----------------|
| 1           | _name_        | _description_        | _count_                | _url_          |


## **Components** ##
* **store** - This app contains the models and views for the store.
* **order** - This app contains the models and views for the orders.
* **db.sqlite3** - Database file.

## **Features** ##
* **Homepage** - Can be accessed at `/` or `/store/` Displays the categories.
* **Category Detail Page** - Can be accessed at `/store/category/{category_id}/` or `/category/{category_id}/` Displays the products in the category.
* **Order Page** - Can be accessed at `/order/` Displays the orders.
* **Order Detail Page** - Can be accessed at `/order/{order_id}/` Displays the details of each order.
* **Admin Panel** - Can be accessed at `/admin/`. Default username: `admin`, password: `admin`.
* **Database** - sqlite3 database is used.

## Dependencies
* **Python 3.X**
* **Django 5.1.1**

## Usage
Clone the repository:
```bash
git clone https://github.com/hella753/djangoinit.git
cd djangoinit
```
To install the dependencies, use the following command in your terminal:
```bash
pip install -r requirements.txt
```
To run the development server, use the following command in your terminal:
```bash
python manage.py runserver
```
To access the application, open your browser and go to http://127.0.0.1:8000/

