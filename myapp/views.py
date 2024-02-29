from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

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

def update_contact(request, contact_id):
    
    contact_instance = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        
        form = ContactForm(request.POST, instance=contact_instance)
        if form.is_valid():
            form.save()
            
            return redirect('contact_details', contact_id=contact_id)
    else:
        
        form = ContactForm(instance=contact_instance)

    return render(request, 'update_contact.html', {'form': form})
    