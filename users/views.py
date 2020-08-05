from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)
  





def contact_form(request):
    pass

def create_user(request):
    if method == 'POST':
        data = {
            'customer': request.POST.get('customer'),
            'name': request.POST.get('name'),
            'email': request.POST.get('email')
        }

        try:
            response = User.objects.create(
                customer = data.get('customer'),
                name = data.get('name'),
                email = data.get('email')
            )
        except Exception as e:
            print(e)
            pass
    return redirect('/')



        