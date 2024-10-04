from django.http import HttpResponse
from .models import Category


# Create your views here.
def index(request):
    content="""
    <html>
        <head>
            <title>Store</title>
        </head>
        <body style="background-color: #C8A1E0; color: #F7EFE5;">
            <h1 style="text-align: center">Store</h1>
            <p style="text-align: center">Welcome to the store.</p>
            <p style="text-align: center">
                Here you can browse our products by category.
            </p>
            <p style="text-align: center">
                Click on a category to view the products in that category.
            </p>
            <div style="text-align: center">
                <div style="display: inline-block">
                    <a style="display: block;
                              text-decoration: none;
                              color:#674188;"
                        href="category/2">
                        <img style="display: block"
                             src="https://cdn.pixabay.com/photo/2022/05/29/01/40/rose-7228242_960_720.jpg" 
                             alt="Dresses" 
                             width="200" 
                             height="150">
                        Dresses
                    </a>
                </div>
                <div style="display: inline-block">
                    <a style="display: block; 
                              text-decoration: none;
                              color:#674188;"
                        href="category/1">
                        <img style="display: block" 
                             src="https://cdn.pixabay.com/photo/2020/07/11/16/16/jeans-5394561_960_720.jpg" 
                             alt="Shoes" 
                             width="200" 
                             height="150">
                        Denim and Jeans
                    </a>
                </div>
                <div style="display: inline-block">
                    <a style="display: block; 
                              text-decoration: none; 
                              color:#674188;" 
                        href="category/3">
                        <img style="display: block" 
                            src="https://cdn.pixabay.com/photo/2019/07/27/21/42/t-shirt-4367577_960_720.jpg" 
                            alt="Tops" 
                            width="200" 
                            height="150">
                        Shirts
                    </a>
                </div>
            </div>
            <div style="text-align: center">
                <p>Or Go To Your <a href="/order">Orders</a></p>
            </div>        
        </body>
    </html>
    """
    return HttpResponse(content)

def category(request, category_id):
    categories = Category.objects.get(category_id=category_id)
    content=f"""
    <html>
        <head>
            <title>{categories.category_name}</title>
        </head>
        <body style="background-color: #E2BFD9; color: #F7EFE5;">
            <a href="/">Go Back </a>
            <h1 style="text-align: center">{categories.category_name}</h1>
            <h2 style="text-align: center">
                Here you can view the information about the Category
            </h2>
            <div style="list-style-type: none; font-size: 20px">
                <p style="color:#674188">
                    Category ID: {categories.category_id}
                </p>
                <p style="color:#674188">
                    Category Name: {categories.category_name}
                </p>
                <p style="color:#674188">
                    {categories.category_description}
                </p>
                <p style="color:#674188">
                    Number of Products in the Category: {categories.category_product_count}
                </p>
                <p style="text-align: center">Here you can view the products</p>
            </div>
            <div>
                <div style="font-size: 20px; text-align: center">
                    <div style="display: inline-block; 
                                width:300px; 
                                height:300px; 
                                background-color:#F7EFE5; 
                                margin-right: 20px">
                        <p style="color:#E2BFD9">Example Product 1</p>
                    </div>
                    <div style="display: inline-block; 
                                width:300px; 
                                height:300px; 
                                background-color:#F7EFE5; 
                                margin-right: 20px">
                        <p style="color:#E2BFD9">Example Product 2</p>
                    </div>
                    <div style="display: inline-block; 
                                width:300px; 
                                height:300px; 
                                background-color:#F7EFE5; 
                                margin-right: 20px">
                        <p style="color:#E2BFD9">Example Product 3</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(content)
