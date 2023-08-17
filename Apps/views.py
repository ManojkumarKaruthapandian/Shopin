from django.http import JsonResponse
from django.shortcuts import redirect,render
from Apps.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json


def home(request):
    
    catagory=Catagory.objects.filter(status=0)
    
    highliteAppliances=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Appliances=1)
    highliteMobiles=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Mobiles=1)
    highliteElectronics=Htodays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Electronics=1)
    highliteSports=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Sports=1)
    highliteFashion=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Fashion=1,trending=0)
    highliteGrocery=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Grocery=1)
    highliteToysBeauty=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_ToysBeauty=1)
    highlitetrending_Fashion=todays_deal=Product.objects.filter(status=0,todays_deal=1,trending_Fashion=1,trending=1)
    trendingproduct=Product.objects.filter(status=0,trending=1)
    mobiles=Product.objects.filter(status=0,trending_Mobiles=1)
    fashion=Product.objects.filter(status=0,trending_Fashion=1)
    grocery=Product.objects.filter(status=0,trending_Grocery=1)
    appliances=Product.objects.filter(status=0,trending_Appliances=1)
    sports=Product.objects.filter(status=0,trending_Sports=1)
    electronics=Product.objects.filter(status=0,trending_Electronics=1)
    beautytoys=Product.objects.filter(status=0,trending_ToysBeauty=1)
    
    return render(request,"shop/catagory.html",{"catagory":catagory,"trendingproduct":trendingproduct,"mobiles":mobiles,"fashion":fashion,"grocery":grocery,"appliances":appliances,"sports":sports,"electronics":electronics,"beautytoys":beautytoys,"highliteMobiles":highliteMobiles,"highliteElectronics":highliteElectronics,"highliteAppliances":highliteAppliances,"highliteSports":highliteSports,"highliteFashion":highliteFashion,"highliteGrocery":highliteGrocery,"highliteToysBeauty":highliteToysBeauty,"highlitetrending_Fashion":highlitetrending_Fashion})

def recommend(request):
    catagory=Catagory.objects.filter(status=0)
    trendingproduct=Product.objects.filter(status=0,trending=1)
    return render(request,"shop/products/recommend.html",{"catagory":catagory,"trendingproduct":trendingproduct,})


def about(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/products/about.html",{"catagory":catagory})

def customerservice(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/products/customerservice.html",{"catagory":catagory})



def add_to_favorite(request):
    if request.headers.get('X-requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Favorite.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favorite'}, status=200)  
                else:
                    Favorite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Add to Favorite Succcess'}, status=200)
                    

        else:
            return JsonResponse({'status':'Login to Add Favorite'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)


def favoriteview(request):
    if request.user.is_authenticated:
        catagory=Catagory.objects.filter(status=0)
        favorite=Favorite.objects.filter(user=request.user)
        return render(request,"shop/products/favorite.html",{"catagory":catagory,"favorite":favorite})
    else:
        catagory=Catagory.objects.filter(status=0)
        return render(request,"shop/products/favorite.html",{"catagory":catagory})



def remove_favorite(request,cid):
    favoriteitem=Favorite.objects.get(id=cid)
    favoriteitem.delete()
    return redirect('/favoriteview')


def add_to_recent(request):
    if request.headers.get('X-requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Recentview.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Recentview'}, status=200)  
                else:
                    Recentview.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Add to Recentview Succcess'}, status=200)
                    

        else:
            return JsonResponse({'status':'Login to Add Recentview'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)


def recentview(request):
    if request.user.is_authenticated:
        catagory=Catagory.objects.filter(status=0)
        recentview=Recentview.objects.filter(user=request.user)
        return render(request,"shop/products/recentview.html",{"catagory":catagory,"recentview":recentview})
    else:
        catagory=Catagory.objects.filter(status=0)
        return render(request,"shop/products/recentview.html",{"catagory":catagory})



def remove_recent(request,cid):
    recentviewitem=Recentview.objects.get(id=cid)
    recentviewitem.delete()
    return redirect('/recentview')




def add_to_cart(request):
    if request.headers.get('X-requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)  
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Add to Cart Succcess'}, status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'}, status=200)

        else:
            return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)


def cartview(request):
    if request.user.is_authenticated:
        catagory=Catagory.objects.filter(status=0)
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/products/cartview.html",{"catagory":catagory,"cart":cart})
    else:
        catagory=Catagory.objects.filter(status=0)
        return render(request,"shop/products/cartview.html",{"catagory":catagory})



def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cartview')




def add_to_order(request):
    if request.headers.get('X-requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                
                if product_status.quantity>=product_qty:
                    Order.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                    return JsonResponse({'status':'Product Order Succcess'}, status=200)
                else:
                    return JsonResponse({'status':'Product Stock Not Available'}, status=200)

        else:
            return JsonResponse({'status':'Login to Buy Now'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)


def orderview(request):
    if request.user.is_authenticated:
        catagory=Catagory.objects.filter(status=0)
        order=Order.objects.filter(user=request.user)
        return render(request,"shop/products/orderview.html",{"catagory":catagory,"order":order})
    else:
        catagory=Catagory.objects.filter(status=0)
        return render(request,"shop/products/orderview.html",{"catagory":catagory})



def remove_order(request,cid):
    orderitem=Order.objects.get(id=cid)
    orderitem.delete()
    return redirect('/orderview')


def search(request):
    catagory=Catagory.objects.filter(status=0)
    search_obj=request.GET.get('search')
    result=Product.objects.filter(name__icontains=search_obj)
    if result:
        results=result
    else:
        results=messages.error(request,"Product is not Available")
    return render(request,"shop/products/search.html",{"results":results,"catagory":catagory})




    

def login_page(request):
    catagory=Catagory.objects.filter(status=0)
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect("/login")

    return render(request,"shop/products/login.html",{"catagory":catagory})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged in Successfully")
    return redirect("/")

def registers(request):
    catagory=Catagory.objects.filter(status=0)
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now..!")
            return redirect('/login')
    return render(request,"shop/products/register.html",{"catagory":catagory,"form":form})




def collectioncatagory(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/layouts/main.html",{"catagory":catagory})


def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        catagory=Catagory.objects.filter(status=0)
        products=Product.objects.filter(category=name)
        return render(request,"shop/products/products.html",{"catagory":catagory,"products":products,"headcatagory":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('home')
    


def productview(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            catagory=Catagory.objects.filter(status=0)
            products=Product.objects.filter(name=pname,status=0)
            return render(request,"shop/products/productview.html",{"catagory":catagory,"products":products,"headcatagory":cname})
        else:
            messages.warning(request,"No Such Product Found")
            return redirect('collectionsview')

    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collectionsview')
        
      
        
        

    






