from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html",{"todos": items})
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            pass
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


