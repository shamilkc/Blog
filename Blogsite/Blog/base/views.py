from django.shortcuts import render,redirect
from . models import BlogPost,Comment,Category,Email,Contact
from .forms import CommentForm

def index(request):
    blog_posts = BlogPost.objects.all().order_by('-updated')[:8]

    context ={
        'blog_posts':blog_posts
    }
    return render(request,'index.html',context)


def about(request):
    context ={}
    return render(request,'about.html',context)


def category(request):
    category = Category.objects.all()
    context ={
        'category':category
    }
    return render(request,'category.html',context)


def single_post(request,pk):
    post = BlogPost.objects.get(id=pk)
    
    form = CommentForm()

    comments = Comment.objects.filter(post=post).order_by('-updated')

    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            
            form.save(commit=False)
            form.instance.post = post
            form.instance.user = request.user
            form.save()

            return redirect(request.path_info)

    
    context ={
        'post':post,
        'form':form,
        'comments':comments,
    }
    return render(request,'post_detailed.html',context)


def category_post(request,pk):
    categoryblogs = BlogPost.objects.filter(category_id=pk)
    
    categoryHeading = Category.objects.get(id=pk)
   
    context ={
        'categoryblogs':categoryblogs,
        'categoryHeading':categoryHeading
    }
    return render(request,'category_post.html',context)



def blogs_page(request):
    
    if request.GET.get('q') != None:
        query = request.GET.get('q')
        blog_posts = BlogPost.objects.filter(title__icontains=query).order_by('-updated')
    else:
        blog_posts = BlogPost.objects.all().order_by('-updated')
    
    context ={
        'blog_posts':blog_posts
    }
    return render(request,'blogs_page.html',context)

def emailsub(request):
    if request.method == "POST":
        if request.POST['email']:
            email = request.POST['email']
            sub = Email(email=email)
            sub.save()
        
    return redirect('home')

def contact(request):
    if request.method == "POST":
        if request.POST['email']:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            sub = Contact(name=name,email=email,message=message)
            sub.save()
        
    return redirect('home')



    
