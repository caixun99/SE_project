from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('market:index'))

def register(request):
    if request.method!='POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('market:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)


