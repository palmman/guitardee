from django.shortcuts import render, get_object_or_404
from .models import Shop


# Create your views here.

def shop(request):

    shops = Shop.objects.order_by('-created_date')

    brand_search = Shop.objects.values_list('brand', flat=True).distinct()
    categories_search = Shop.objects.values_list('categories', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            shops = shops.filter(description__icontains=keyword)

    if 'brand' in request.GET:
        brand = request.GET['keyword']
        if brand:
            shops = shops.filter(description__iexact=brand)

    

    data = {
        'shops' : shops,
        'brand_search' : brand_search,
        'categories_search' : categories_search
    }
    return render(request, 'shop/shop.html', data)

def shop_single(request, id):

    shop_detail = get_object_or_404(Shop, pk=id)
    data = {
        'shop_detail' : shop_detail,
    }
    return render(request, 'shop/shop_single.html', data)

def cart(request):
    return render(request, 'shop/cart.html')
