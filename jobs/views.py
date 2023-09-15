from django.shortcuts import render

from .models import Job
#render : to generate or produce a visual output based on some input or data.
# Create your views here.
def home(request):
    jobs= Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})
