from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from .models import User, Wishlist
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product

class EditProfileView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'avatar')
    template_name = "registration/edit_user.html"
    success_url = reverse_lazy("core:dashboard")


class LoginView(LoginView):
    authentication_form = UserLoginForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()

            messages.success(
                request, f'Your account was successfully created! You can now login!')
            return redirect(reverse("core:dashboard"))
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})


@login_required
def wishlist(request):
    wishlists = request.user.wishlists.all()
    context = {
        'items': wishlists,
    }
    return render(request, 'users/wishlist.html', context)

@login_required
def add_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not Wishlist.objects.filter(user=request.user, product=product).exists():
        Wishlist.objects.create(user = request.user, product = product)
        messages.success(request,f"{product.name} successfully added to the wishlist.")
    else:
        messages.error(request,f"{product.name} is already in the wishlist!")
    return redirect(reverse('wishlist'))


def remove_wishlist(request, pk):
    obj = get_object_or_404(Wishlist, pk=pk)
    if obj.user == request.user:
        obj.delete()
    messages.error(request,f"{obj.product.name} successfully removed the wishlist!")
    return redirect(reverse('wishlist'))
