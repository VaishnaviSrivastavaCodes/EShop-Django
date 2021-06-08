from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData= request.POST
        name= postData.get('name')
        email=postData.get('email')
        password=postData.get('password')
        phone=postData.get('phone')
        values={
            'name':name,
            'phone':phone,
            'email':email
        }
        customer= Customer(name=name, phone=phone, email=email, password= password)
        error_message=Signup.validate_customer(customer)
        if error_message:
            return render(request,'signup.html',{'error':error_message, 'values':values}) 
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
        return redirect('homepage')
    def validate_customer(customer):
        error_message=None
        if not customer.name:
                error_message="Please enter name."
        if not customer.email:
                error_message="Please enter email."
        if len(customer.password)<6:
                error_message='Password should have at least 6 characters.'
        if len(customer.phone) != 10:
            error_message='Phone number should have 10 digits.'

        if(Customer.is_present(customer)):
                    error_message='Email user already exists.'
        return error_message