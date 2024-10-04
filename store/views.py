from django.http import HttpResponse
from .models import Category


# Create your views here.
def index(request):
    content="""
    <html>
        <head>
            <title>Store</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Afacad+Flux:wght@100..1000&display=swap" rel="stylesheet">
        </head>
        <body style="background-color: #F7EFE5; color: #C8A1E0; font-family:Afacad Flux">
            <h1 style="text-align: center; margin-top: 50px">Store</h1>
            <p style="text-align: center; margin-bottom:150px">
                Welcome to the store!
                Shop what's trending this season
            </p>
            <p style="text-align: center">
                Here you can browse our products by category.
            </p>
            <p style="text-align: center">
                Click on a category to view the products in that category.
            </p>
            <div style="text-align: center">
                <div style="display: inline-block; margin-right:30px">
                    <a style="display: block;
                              text-decoration: none;
                              color:#674188;"
                        href="category/2">
                        <img style="display: block"
                             src="https://cdn.pixabay.com/photo/2022/05/29/01/40/rose-7228242_960_720.jpg" 
                             alt="Dresses" 
                             width="350" 
                             height="300">
                        Dresses
                    </a>
                </div>
                <div style="display: inline-block; margin-right: 30px">
                    <a style="display: block; 
                              text-decoration: none;
                              color:#674188;"
                        href="category/1">
                        <img style="display: block" 
                             src="https://cdn.pixabay.com/photo/2020/07/11/16/16/jeans-5394561_960_720.jpg" 
                             alt="Shoes" 
                             width="350" 
                             height="300">
                        Denim and Jeans
                    </a>
                </div>
                <div style="display: inline-block; margin-right: 30px">
                    <a style="display: block; 
                              text-decoration: none; 
                              color:#674188;" 
                        href="category/3">
                        <img style="display: block" 
                            src="https://cdn.pixabay.com/photo/2019/07/27/21/42/t-shirt-4367577_960_720.jpg" 
                            alt="Tops" 
                            width="350" 
                            height="300">
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
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Afacad+Flux:wght@100..1000&display=swap" rel="stylesheet">
            <title>{categories.category_name}</title>
        </head>
        <body style="background-color: #F7EFE5; color: #E2BFD9; font-family: Afacad Flux">
            <a href="/">Go Back </a>
            <h1 style="text-align: center">{categories.category_name}</h1>
            <h2 style="text-align: center">
                Here you can view the information about the Category
            </h2>
            <div style="list-style-type: none; font-size: 20px">
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
                                background-color:#E2BFD9; 
                                margin-right: 40px">
                        <p style="color:#F7EFE5">Example Product 1</p>
                    </div>
                    <div style="display: inline-block; 
                                width:300px; 
                                height:300px; 
                                background-color:#E2BFD9; 
                                margin-right: 40px">
                        <p style="color:#F7EFE5">Example Product 2</p>
                    </div>
                    <div style="display: inline-block; 
                                width:300px; 
                                height:300px; 
                                background-color:#E2BFD9; 
                                margin-right: 40px">
                        <p style="color: #F7EFE5">Example Product 3</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(content)
