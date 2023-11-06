from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.db.models import Q
from django.templatetags.static import static
def home(request):
    items=Product.objects.filter(is_sold=False)[:6]
    categories=Category.objects.all()
    img_menu_open = static('image/icon.svg')
    img_close_menu = static('image/icon-close.svg')
    bg_menu=static('image/bg.jfif')
    context={'categories':categories,'items':items,'img_menu_open': img_menu_open, 'img_close_menu': img_close_menu,'bg_menu':bg_menu}
    return render(request,'market/index.html',context)

def product_detail(request,item,year,month,day):
    item=get_object_or_404(Product, slug=item,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    related_items=Product.objects.filter(category=item.category, is_sold=False).exclude(slug=item)[:3]
    context={'item':item, 'related_items':related_items}
    return render(request,'market/detail.html',context)

def search_items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category_id',0)
    categories=Category.objects.all()
    items=Product.objects.filter(is_sold=False)

    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context={'items':items, 'query':query,'categories':categories,
             'category_id':int(category_id)}

    return render(request,'market/browse.html',context)


