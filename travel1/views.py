from django.shortcuts import render, redirect,get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import blogmodel
from .forms import blogform
from .forms import Profile
from .forms import ProfileUpdateForm
from itertools import chain




def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def loginn(request):
    return render(request,"login.html")
def blog(request):
    return render(request,"blog.html")

def signup(request): 
    if request.method == 'POST':
        f_name = request.POST['Fname']
        l_name = request.POST['Lname']
        u_name = request.POST['Uname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        profile_picture = request.FILES.get('profile_picture')

        if password1 == password2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, "Username already exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('signup')
            else:
                user = User.objects.create_user( first_name=f_name, last_name=l_name, username=u_name, email=email, password=password1 )
                user.save()

                Profile.objects.create(user=user, profile_picture=profile_picture)

                messages.success(request, "Account created successfully!")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match") 
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

    

def login(request):
    if request.method=="POST":
        u_name=request.POST['Uname']
        password1=request.POST['password']
        user=auth.authenticate(username=u_name,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')
 


def addblog(request):
    if request.method == 'POST':
        form = blogform(request.POST, request.FILES,)
        if form.is_valid():
            blog_instance = form.save(commit=False)
            if request.user.is_authenticated:
                blog_instance.author = request.user
            blog_instance.save()

            return redirect('blog')  
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = blogform()  

    return render(request, 'addblog.html', {'form': form})


def blog_list(request):
    if request.user.is_authenticated:
        user_blogs = blogmodel.objects.filter(author=request.user).order_by('-updated_at')
        other_blogs = blogmodel.objects.exclude(author=request.user).order_by('-updated_at')
        blogs = chain(user_blogs, other_blogs)
    else:
        blogs = blogmodel.objects.all().order_by('-created_at')

    return render(request, 'blog.html', {'blogs': blogs})



def blog_detials(request,id):
    blog=get_object_or_404(blogmodel, id=id) 
    context={'blog':blog}
    return render(request,'blog_details.html',context)

def delete(request, id):
    blogmodel.objects.filter(id=id).delete()  
    return redirect('blog') 


def edit(request, id):
    instance_to_be_edited = get_object_or_404(blogmodel, id=id) 
    if request.method == 'POST':
        form = blogform(request.POST, request.FILES, instance=instance_to_be_edited)  
        if form.is_valid():
            form.save()  
            return redirect('blog')  
    else:
        form = blogform(instance=instance_to_be_edited)  
    
    return render(request, 'edit.html', {'frm': form})  


def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')  
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, "profile.html", {"form": form, "profile": profile})


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile  # Ensure this import exists

def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()

        # Handling profile picture
        profile = user.profile  # Assuming a one-to-one relationship
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()

        messages.success(request, 'Your profile has been updated!')
        return redirect('profile')  
    
    # Pass the profile to the template
    profile = request.user.profile
    return render(request, 'edit_profile.html', {'profile': profile})





  
