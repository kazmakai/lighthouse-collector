from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the Lighthouse Model
from .models import Lighthouse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lighthouses_index(request):
    lighthouses = Lighthouse.objects.all() # Retrive all lighthouses
    return render(request, 'lighthouses/index.html', 
    {
        'lighthouses': lighthouses
    }
)

def lighthouses_detail(request, lighthouse_id): 
    # need the lighthouse_id parameter because of lighthouse/<int:lighthouse_id> in urls.py
    lighthouse = Lighthouse.objects.get(id=lighthouse_id)
    return render(request, 'lighthouses/detail.html', { 'lighthouse': lighthouse })

class LighthouseCreate(CreateView):
    model = Lighthouse
    fields = '__all__'

class LighthouseUpdate(UpdateView):
    model = Lighthouse
    fields = ['location', 'built', 'description']

class LighthouseDelete(DeleteView):
    model = Lighthouse
    success_url = '/lighthouses'