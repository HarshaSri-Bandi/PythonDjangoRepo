from django.shortcuts import render

# Create your views here.

def electronics(request):
    product_dict={
    "product1" : "Mac",
    "product2" : "Iphone",
    "product3" : "Dell"
    }
    return render(request, "productApp/products.html", product_dict)



def toys(request):
    product_dict={
    "product1" : "car",
    "product2" : "drone",
    "product3" : "Doll"
    }
    return render(request, "productApp/products.html", product_dict)


def shoes(request):
    product_dict={
    "product1" : "addidas",
    "product2" : "H&M",
    "product3" : "Levis"
    }
    return render(request, "productApp/products.html", product_dict)

def index(request):
    return render(request, 'productApp/index.html')


