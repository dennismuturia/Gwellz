from django.shortcuts import render

# Create your views here.
def the_projects(request):
    return render(request, 'projects.html')
