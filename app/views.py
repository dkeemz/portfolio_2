from django.shortcuts import render
from .models import Project
# Create your views here.
def index(req):
    return render(req,"index.html")

def skills(req):
    return render(req,"skills.html")

def projects(req):
    projects=Project.objects.all().order_by('-id')
    return render(req,"projects.html",{'projects':projects})
