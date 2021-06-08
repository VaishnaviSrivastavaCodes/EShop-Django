from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer



class Checkout(View):
    def get(self, request):
        return render(request, 'checkout.html')

    def post(self, request):
        address= request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        products =   Product.get_products_by_id(list(cart.keys()))
        print(address, " : Address", phone , " phone", customer_id, " customer_id" , cart ,"cart",
        products, "products")

        for product in products:
            order = Order(customer = Customer(id =customer_id), 
                        product=product,
                        price = product.price,
                        quantity = cart.get(str(product.id)),
                        address = address,
                        phone = phone
                        )
            order.placeOrder()
        request.session['cart'] ={}
        success_message = "Your order was placed successfully."
        return render(request,'cart.html', {'success_message':success_message})
