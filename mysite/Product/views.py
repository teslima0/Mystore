import django
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from . models import CustomUser, Product, Category, Comment
from . forms import ProductForm, CommentForm
#note


#@login_required(login_url='products/login')
def ShowAllProduct(request):
    
    category = request.GET.get('category')
    
    if category == None:
        products = Product.objects.order_by('-price').filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 3)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)             
    else:
        products = Product.objects.filter(category__name=category)
       
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'customer/showProduct.html', context)

#@login_required(login_url='products/login')
def ShowAllProducts(request):
    
    category = request.GET.get('category')
    
    if category == None:
        products = Product.objects.order_by('-price').filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 3)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)             
    else:
        products = Product.objects.filter(category__name=category)
       
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'products/showProducts.html', context)



@login_required(login_url='Product:login')
def productDetail(request, pk):
    
    eachProduct = Product.objects.get(id=pk)

    num_comments = Comment.objects.filter(product=eachProduct).count()

    context = {
        'eachProduct': eachProduct,
        'num_comments': num_comments,
    }

    return render(request, 'products/productDetail.html', context)



@login_required(login_url='Product:login')
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        if request.user.is_superuser or request.user.adminceo:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('Product:showProducts')
    else:
        if request.user.is_superuser or request.user.adminceo:
            form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'products/addProduct.html', context)


@login_required(login_url='Product:login')
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Product:showProducts')

    context = {
        "form":form
    }

    return render(request, 'products/updateProduct.html', context)



@login_required(login_url='Product:login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('Product:showProducts')



#@login_required(login_url='Product:showProducts')
def searchBar(request):
    if request.method == 'POST':
        query = request.POST['query']
        if query:
            products = Product.objects.filter(name__contains=query) 
            context = {
            "products":products
    }
            
            return render(request, 'products/searchbar.html', context)
           # return redirect('Product:showProducts')
        else:
            print("No information to show")
            return render(request, 'products/searchbar.html', {})

def add_comment(request, pk):
    eachProduct = Product.objects.get(id=pk)

    form = CommentForm(instance=eachProduct)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachProduct)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('Product:showProducts')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'products/add_comment.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.filter(product=pk).last()
    product_id = comment.product.id
    comment.delete()
    return redirect('Product:showProducts')
    #return redirect(reverse('product', args=[product_id]))




# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                print('Username exists! try another username...')
                return redirect('Product:register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    print('Email is already taken! try another one')
                    return redirect('Product:register')
                else:
                    user = CustomUser.objects.create_user(username=username, email=email, password=password1, user_type=3)
                    user.save()
                    return redirect('Product:login')   
        else:
            print('Password did not matched!..')
            return redirect('Product:register')
    else:
        return render(request, 'products/register.html')        
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                Product:login(request,user)
                if user.user_type=="1":
                    return redirect('Product:showProducts')
                elif user.user_type=="2":
                    return redirect('Product:showProduct')
                else:
                    return redirect('Product:showProduct')
        else:
            messages.error(request,"Invalid Login Details")
            return render(request, 'products/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print('Login Successfull!')

            if user.user_type=="1":
                return redirect('Product:showProducts')
            elif user.user_type=="2":
                return redirect('Product:showProduct')
            elif user.user_type=="3":
                return redirect('Product:showProduct')
            else:
                return HttpResponseRedirect('Invalid credential')
            
        else:
            print('invalid credentials')
            return redirect('Product:login') 
    else:
        return render(request, 'products/login.html')           


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from websites..')
        return redirect('Product:login')

def logout_view(request):
    logout(request)
    return redirect('Product:login')