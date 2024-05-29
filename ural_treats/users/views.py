from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import User
from .forms import UserRegistrationForm

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:index'))
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user(request, user_pk):
    user = get_object_or_404(User, slug=user_pk)

    context = {"user": user}

    return render(request, "profile.html", context=context)
