from django.shortcuts import render
from .models import members

# Create your views here.
def royalteam(request):
    myteam = members.objects.all()
    return render(request, 'ppt.html')