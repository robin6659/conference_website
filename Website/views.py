
from django.shortcuts import render
from .import views
from django.http import HttpResponse
from .models import Queries
from django.core.mail import send_mail

def index(request):
  return render(request,"Website/index.html")
def reg(request):
  return render(request,"Website/registration.html")
def callforpaper(request):
  return render(request,"Website/callForPapers.html")
def papersub(request):
  return render(request,"Website/paperSubmission.html")
def acceptedpub(request):
  return render(request,"Website/acceptedPublications.html")


# Create your views here.
def faq(request):
  if request.method == 'POST':
    name = request.POST['name']
    contact_number = request.POST['contact_number']
    email = request.POST['email']
    message = request.POST['message']

    send_mail(
    'ICFOSS Conference Update',
    'Your Query is registered.',
    'devteamicfoss@gmail.com',
    [email],
    fail_silently=False,
)

    b = Queries(name=name, contact_number=contact_number, email=email, message=message )
    b.save()


    return render(request,"Website/index.html")