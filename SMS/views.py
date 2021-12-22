from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




from .forms import UserInfoModelForm
from .models import Balance, UserInfo, Ticket




def user_create_view(response, *args, **kwargs):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        formprofile = UserInfoModelForm(response.POST)
        if form.is_valid() and formprofile.is_valid():
            print("here")
    
            user = form.save()
            name = formprofile.cleaned_data.get("name")
            lastName = formprofile.cleaned_data.get("lastName")
            telnum = formprofile.cleaned_data.get("telnum")
            gender = formprofile.cleaned_data.get("gender")
            age = formprofile.cleaned_data.get("age")
            print(name,lastName, telnum )
            UserInfo.objects.create(user= user, name= name, lastName=lastName, telnum= telnum, gender=gender, age= age)
            Balance.objects.create(user=user)
            
            return redirect("/index")
    else:
        formprofile = UserInfoModelForm()
        form = UserCreationForm()

    context = {
        'form' : form, 
        'formp': formprofile,       
    }
    return render(response, "registration/register.html", context)

@login_required
def user_update_view(request, uid):
    # user = User.objects.get(userID=uid)
    userinf = get_object_or_404(UserInfo, userID=uid)
    userr = userinf.user
    userr = get_object_or_404(User, username = userr)
    form = UserCreationForm(request.POST or None, instance=userr)
    formprofile = UserInfoModelForm(request.POST or None, instance=userinf)
    if form.is_valid() and formprofile.is_valid():
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        userr.username = username
        userr.password = password
        print(username, password)
        # userr.save()
        name = formprofile.cleaned_data.get("name")
        lastName = formprofile.cleaned_data.get("lastName")
        telnum = formprofile.cleaned_data.get("telnum")
        gender = formprofile.cleaned_data.get("gender")
        age = formprofile.cleaned_data.get("age")
        userinf = get_object_or_404(UserInfo, user=userr)
        userinf.name = name
        userinf.lastName = lastName
        userinf.telnum = telnum
        userinf.age = age
        userinf.gender = gender
        userinf.save()
        
            
        return redirect("/index")
    else:
        formprofile = UserInfoModelForm(request.POST or None, instance=userinf)
        form = UserCreationForm(request.POST or None, instance=userr)

    context = {
        'form' : form, 
        'formp': formprofile,       
    }
    return render(request, "registration/register.html", context)

    
    

def user_delete_view(request, uid):
    # user = User.objects.get(userID=uid)
    user = get_object_or_404(UserInfo, userID=uid)
    if request.method == 'POST':
        user.delete()
    

    context = {
        'obj' : user
    }
    return render(request, "userdelete.html", context)

# Create your views here.
def home_view(request, *args, **kwargs):
    content = {}
    return render(request, "home.html", content)


@login_required(login_url="/login")
def recharge(request):
    if request.method == 'POST':
        login_data = request.POST.dict()
        code = login_data.get("code")
        user = request.user.username
        print(user)
        user = get_object_or_404(User, username=user)
        ticket = Ticket.objects.get(code = code)
        if ticket.used ==True:
            context = {
                'error': "This ticket is used cuh"
            }
            return render(request, "error/error.html", context)
        else:
            ticket.used = True
            ticket.boughtBy = user 
            bal = Balance.objects.get(user = user)
            bal.balance += ticket.value
            ticket.save()
            bal.save()
            return home_view(request)

    return render(request, 'account/recharge.html', {})


