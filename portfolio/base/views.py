
from django.shortcuts import render
from .models import Con,Pro
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect


# Create your views here.



def home(request):
    projects = Pro.objects.all()
    if request.method == "POST":

        name =request.POST["name"]
        email =request.POST["email"]
        subject =request.POST["subject"]
        messege =request.POST["message"]
        send_mail(email,messege,email,[settings.EMAIL_HOST_USER], fail_silently=False)
        data = Con(name=name,email=email,subject=subject,messege=messege)
        data.save()
        return redirect('home')


    context ={
        'projects':projects
    }

    return render(request,'home.html',context)

    #132c9569-000a-4e54-8ce3-7d22c9371072
def verify(request):



    return render(request,'132c9569-000a-4e54-8ce3-7d22c9371072.html')
