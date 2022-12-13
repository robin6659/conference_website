
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

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
def committee(request):
  return render(request,"Website/committee.html")
def update(request):
  return render(request,"Website/updatePage.html")

def faq(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    print(form)
    if form.is_valid():
      email = request.POST['email']
      form.save()
      send_mail(
                       'ICFOSS Conference Update',
                        'Your Query is registered.',
                        'devteamicfoss@gmail.com',
                     [email],
                   fail_silently=False,
                   )
    return render(request,'Website/index.html')
  else:
    return render(request, 'Website/index.html',{'form': form})
    form = ContFm()
    return render(request, 'Website/index.html',{'form': form})
















# Create your views here.
# def faq(request):
#   if request.method == 'POST':
#     name = request.POST['name']
#     contact_number = request.POST['contact_number']
#     email = request.POST['email']
#     message = request.POST['message']

#     send_mail(
#     'ICFOSS Conference Update',
#     'Your Query is registered.',
#     'devteamicfoss@gmail.com',
#     [email],
#     fail_silently=False,
# )

#     b = Queries(name=name, contact_number=contact_number, email=email, message=message )
#     b.save()


#     return render(request,"Website/index.html")