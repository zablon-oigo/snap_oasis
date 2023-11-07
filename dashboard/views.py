from django.shortcuts import render
from market.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    items=Product.objects.filter(seller=request.user)
    context={'items':items}
    return render(request, 'dashboard/index.html', context)
