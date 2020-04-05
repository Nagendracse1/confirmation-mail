from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
# Create your views here.
def form(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('number')
        how_hear = request.POST.get('hear')

        var_detail = Detail(name=name, email=email, mobile_no=mobile_no, how_hear=how_hear)
        var_detail.save()
        send_mail('Confirmation mail', 'Your form have been successfully submitted', 'nagendra.cse1@gmail.com', [email], fail_silently=False, )

        return render(request, 'thanks.html')
    else:
        return render(request,'index.html')