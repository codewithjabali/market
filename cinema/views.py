from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'contact.html')

def read(request):
    return render(request, 'market.html')



def market(request):
    username = request.POST.get('user_name')
    useremail = request.POST.get('user_email')
    userphone = request.POST.get('user_phone')
    message = request.POST.get('message')
    if request.method == "POST":
        if not username or not useremail or not userphone or not message:
            return redirect("about")
        contact = Contact(name=username, email=useremail, phone=userphone, message=message)
        contact.save()
        message = "Your message has been sent successfully! We will get back to you soon via your contact details. make sure your contact is valid"
        return render(request, 'contact.html', {'message': message})
    
    return render(request, 'contact.html')


def view_customers(request):
    contacts = Contact.objects.all()
    return render(request, 'customers.html', {'contacts': contacts})
# Create your views here.
