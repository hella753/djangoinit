from django.http import HttpResponse
from .models import Order


def index(request):
    orders = Order.objects.all()
    content = f"""
    <html>
        <head>
            <title>Orders Page</title>
            <link
                rel="preconnect"
                href="https://fonts.googleapis.com">
            <link
                rel="preconnect"
                href="https://fonts.gstatic.com"
                crossorigin>
            <link
                href="https://fonts.googleapis.com/css2?family=Afacad+Flux:wght@100..1000&display=swap"
                rel="stylesheet">
        </head>
        <body style="background-color: #F7EFE5;
              color: #674188;
              font-family:Afacad Flux">
            <a href="/">Go Back</a>
            <h1 style="text-align: center">
                Welcome to the orders page
            </h1>
            <p style="text-align: center">
                Here you can view all orders
            </p>
            <p style="text-align: center">
                Click on the order to view details
            </p>
            <div>
                <h2 style="text-align: center;  margin-top:70px">
                    Your Orders
                </h2>
                <ul style="list-style-type: none;
                    font-size: 20px;
                    margin-left:300px">
    """

    for order in orders:
        order_dict = {
            "order id": order.order_id,
            "order date": order.order_date,
            "order status": order.order_status,
            "product id": order.product_id
        }
        if order_dict["order status"] == "Delivered":
            order_color = "#C8A1E0"
        else:
            order_color = "#E2BFD9"

        content += f"""
             <li style="background-color:{order_color}; width:760px">
                <a style="text-decoration: none;
                    color:#674188;"
                    href="/order/{order_dict["order id"]}">
                    Order ID: {order_dict["order id"]}  |
                    Order Date: {
                        order_dict["order date"].strftime("%B %d, %Y")
                    }  |
                    Order Status: {order_dict["order status"]}  |
                    Product ID: {order_dict["product id"]}
                </a>
            </li>
        """
    content += """
                </ul>
            </div>
        </body>
    </html>
    """
    return HttpResponse(content)


def individual_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    if order.order_status == "Delivered":
        order_color = "#C8A1E0"
    else:
        order_color = "#E2BFD9"
    content = f"""
    <html>
        <head>
            <title>Order Page {order_id}</title>
            <link
                rel="preconnect"
                href="https://fonts.googleapis.com">
            <link
                rel="preconnect"
                href="https://fonts.gstatic.com" crossorigin>
            <link
                href="https://fonts.googleapis.com/css2?family=Afacad+Flux:wght@100..1000&display=swap"
                rel="stylesheet">
        </head>
        <body style="background-color: #F7EFE5;
              color: #674188;
              font-family:Afacad Flux">
            <a style="color:#674188">
                Go back to <a href="/order">Orders Page</a>
            </a>
            <h1 style="text-align: center; margin-top: 70px">
                Order {order_id}
            </h1>
            <p style="text-align: center">
                Here you can view the details of Order {order_id}
            </p>
            <div>
                <h2 style="text-align: center; margin-top:50px">
                    Order Details
                </h2>
                <ul style="list-style-type: none;
                           font-size: 20px;
                           width:300px;
                           margin-left:550px;
                           margin-top:20px;
                           padding:20px;
                           background-color:{order_color}">
                    <li style="color:#674188">
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
                        Category : {order.order_category_id}
                    </li>
                </ul>
            </div>
        </body>
    </html>
    """
    return HttpResponse(content)
