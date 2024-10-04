from django.http import HttpResponse
from .models import Order


# Create your views here.
def index(request):
    orders = Order.objects.all()
    order_list = []

    for order in orders:
        order_dict = {
            "order id": order.order_id,
            "order date": order.order_date,
            "order status": order.order_status,
            "product id": order.product_id
        }
        order_list.append(order_dict)
    content = f"""
    <html>
        <head>
            <title>Orders Page</title>
        </head>
        <body style="background-color: #C8A1E0; color: #F7EFE5">
            <a href="/">Go Back</a>
            <h1 style="text-align: center">Welcome to the orders page</h1>
            <p style="text-align: center">Here you can view all orders</p>
            <p style="text-align: center">
                Click on the order to view details
            </p>
            <div>
                <h2 style="text-align: center">Your Orders</h2>
                <ul style="list-style-type: none; font-size: 20px">
                    <li>
                        <a style="text-decoration: none; 
                                  color:#674188;"
                            href="/order/1">
                            Order ID: {order_list[0]["order id"]}  |  
                            Order Date: {order_list[0]["order date"].strftime("%B %d, %Y")}  |  
                            Order Status: {order_list[0]["order status"]}  |  
                            Product ID: {order_list[0]["product id"]}
                        </a>
                    </li>
                    <li>
                        <a style="text-decoration: none; 
                                 color:#674188;"
                            href="/order/2">
                            Order ID: {order_list[1]["order id"]}  |  
                            Order Date: {order_list[1]["order date"].strftime("%B %d, %Y")}  |  
                            Order Status: {order_list[1]["order status"]}  |  
                            Product ID: {order_list[1]["product id"]}
                        </a>
                    </li>
                    <li>
                        <a style="text-decoration: none; 
                                  color:#674188;"
                            href="/order/3">
                            Order ID: {order_list[2]["order id"]}  |  
                            Order Date: {order_list[2]["order date"].strftime("%B %d, %Y")}  |  
                            Order Status: {order_list[2]["order status"]}  |  
                            Product ID: {order_list[2]["product id"]}
                        </a>
                    </li>
                </ul>
            <div>
        </body>
    </html>
    """
    return HttpResponse(content)

def individual_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    content = f"""
    <html>
        <head>
            <title>Order Page {order_id}</title>
        </head>
        <body style="background-color: #E2BFD9; color: #F7EFE5;">
            <a style="color:#674188">
                Go back to <a href="/order">Orders Page</a>
            </a>
            <h1 style="text-align: center">Order {order_id}</h1>
            <p style="text-align: center">
                Here you can view the details of Order {order_id}
            </p>
            <div>
                <h2 style="text-align: center">Order Details</h2>
                <ul style="list-style-type: none; font-size: 20px">
                    <li style="color:#674188;">
                        Order ID: {order_id}
                    </li>
                    <li style="color:#674188;">
                        Order Date: {order.order_date.strftime("%B %d, %Y")}
                    </li>
                    <li style="color:#674188;">
                        Order Status: {order.order_status}
                    </li>
                    <li style="color:#674188;">
                        Product ID : {order.product_id}
                    </li>
                    <li style="color:#674188;">
                        Product Quantity : {order.product_quantity}
                    </li>
                    <li style="color:#674188;">
                        Order Total : {order.order_total}$
                    </li>
                    <li style="color:#674188;">
                        Order Address : {order.order_address}
                    </li>
                    <li style="color:#674188;">
                        Category ID : {order.order_category_id}
                    </li>
                </ul>
            </div>
        </body>
    </html>    
    """
    return HttpResponse(content)