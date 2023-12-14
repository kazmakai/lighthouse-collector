from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the Lighthouse Model
from .models import Lighthouse
from .forms import VisitorForm


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
    visitor_form = VisitorForm()
    return render(request, 'lighthouses/detail.html', { 
        'lighthouse': lighthouse, 'visitor_form': visitor_form 
    })

def add_visitor(request, lighthouse_id):
    form = VisitorForm(request.POST)
    if form.is_valid():
        new_visitor = form.save(commit=False)
        new_visitor.lighthouse_id = lighthouse_id
        new_visitor.save()
    return redirect('detail', lighthouse_id=lighthouse_id)

class LighthouseCreate(CreateView):
    model = Lighthouse
    fields = '__all__'

class LighthouseUpdate(UpdateView):
    model = Lighthouse
    fields = ['location', 'built', 'description']

class LighthouseDelete(DeleteView):
    model = Lighthouse
    success_url = '/lighthouses'