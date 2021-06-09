from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def post(self , request):
        customer = request.session.get('customer')
        if not customer:
            products = Product.get_all_products()
            categories = Category.get_all_categories()
            category_id = request.GET.get('category')
            if category_id:
                products=Product.get_all_products_by_category_id(category_id)
            else:
                products=Product.get_all_products()
            alert_message="Please login to add items to your cart."
            data = {'products':products, 'categories':categories, 'alert':alert_message}
            return render(request,"index.html", data)
        else:
            product_id = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                if product_id:
                    quantity = cart.get(product_id)
                else:
                    quantity= cart.get(remove)
                if quantity:
                    if remove:
                            if quantity>1:
                                quantity = quantity -1
                                cart[remove]  = quantity
                            else:
                                cart.pop(remove)
                    else:
                            quantity=quantity+1
                            cart[product_id] = quantity
                else:
                    cart[product_id] = 1
            else:
                cart = {}
                cart[product_id] = 1
            request.session['cart'] = cart
            return redirect('homepage')




        



    def get(self, request):
        # request.sessions.flush()
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            products=Product.get_all_products_by_category_id(category_id)
        else:
            products=Product.get_all_products()
        data = {'products':products, 'categories':categories}
        return render(request,"index.html", data)
            


