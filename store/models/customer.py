from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=80)
    email= models.EmailField(max_length=80)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=500)

    def register(self):
        self.save

    def is_present(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return None

    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return None

    

    
      
        




