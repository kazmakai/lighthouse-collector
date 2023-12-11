from django.shortcuts import render

lighthouses = [
  {'name': 'Planier Light', 'location': 'Marseille, France', 'height': 66, 'constructed': 1326},
  {'name': 'Maasvlakte Light', 'location': 'Maasvlakte, Netherlands', 'height': 66, 'constructed': 1974},
  {'name': 'Bari Light', 'location': 'Bari, Italy', 'height': 62, 'constructed': 1869},
  {'name': 'Punta Penna Lighthouse', 'location': 'Vasto, Italy', 'height': 70, 'constructed': 1906},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lighthouses_index(request):
    return render(request, 'lighthouses/index.html', {
        'lighthouses': lighthouses
    })