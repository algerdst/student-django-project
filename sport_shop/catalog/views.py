from django.shortcuts import HttpResponseRedirect, render

from .forms import SearchForm
from .models import  Project



def index(request):
    """
    Отображает главную старницу
    """
    try:
        projects = Project.objects.filter(name__icontains=request.GET['search'])
    except:
        projects = Project.objects.all()
    form = SearchForm()
    data = {
        'projects':projects,
        'form': form
    }
    return render(request, 'catalog/index.html', context=data)

def product(request, slug):
    project = Project.objects.get(slug=slug)
    data = {
        'project': project
    }
    return render(request, 'catalog/project.html', context=data)





