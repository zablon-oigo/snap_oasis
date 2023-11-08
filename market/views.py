from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category
from django.db.models import Q
from django.contrib import messages
from .forms import ProductForm
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
def home(request):
    items=Product.objects.filter(is_sold=False)[:6]
    categories=Category.objects.all()
    img_menu_open = static('image/icon.svg')
    img_close_menu = static('image/icon-close.svg')
    bg_menu=static('image/bg.jfif')
    context={'categories':categories,'items':items,'img_menu_open': img_menu_open, 'img_close_menu': img_close_menu,'bg_menu':bg_menu}
    return render(request,'market/index.html',context)

@login_required
def product_detail(request,item,year,month,day):
    item=get_object_or_404(Product, slug=item,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    related_items=Product.objects.filter(category=item.category, is_sold=False).exclude(name=item)[:3]
    context={'item':item, 'related_items':related_items}
    return render(request,'market/detail.html',context)

@login_required
def search_items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    categories=Category.objects.all()
    items=Product.objects.filter(is_sold=False)

    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context={'items':items, 'query':query,'categories':categories,
             'category_id':int(category_id)}

    return render(request,'market/browse.html',context)

@login_required
def add_Item(request):
    if request.method =='POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.seller=request.user
            item.save()
            messages.success(request,'Item added successfully')
            return redirect(item.get_absolute_url())
        else:
            messages.error(request,'Please correct the following error')
    else:
        form=ProductForm()
    return render(request, 'market/add_item.html',{'form':form})

@login_required
def update_Item(request,pk):
    item=get_object_or_404(Product,pk=pk,is_sold=False, seller=request.user)
    if request.method == 'POST':
        form=ProductForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            updateItem=form.save(commit=False)
            updateItem.seller=request.user
            updateItem.save()
            messages.success(request, 'Update request was successfull')
            return redirect(updateItem.get_absolute_url())
        else:
            messages.error(request, 'Please correct the following error')
    else:
        form=ProductForm(instance=item)
    return render(request, 'market/add_item.html',{'form':form,'pk':pk})

@login_required
def delete_Item(request,pk):
    item=get_object_or_404(Product, pk=pk, seller=request.user, is_sold=False)
    if request.method == 'POST':
        item.delete()
        messages.success(request,'The Item was deleted successfully')
        return redirect('market:home')
    return render(request, 'market/delete.html', {'item':item})


        
        


