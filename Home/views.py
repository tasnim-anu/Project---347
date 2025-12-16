from django.shortcuts import render, HttpResponse, redirect
from .models import Review, Product
from django.db.models import Q
# Create your views here.


def index(request):
    products = Product.objects.filter(is_featured=True)[:5]
    cart_items_count = 0  
    return render(request, 'Home/index.html', {'products': products,'cart_items_count': cart_items_count})



def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'Home/index.html')


def logout(request):
    return render(request, 'Home/index.html')



def review(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        product_name = request.POST.get("product_name")
        review_text = request.POST.get("review_text")
        star_rating = request.POST.get("star_rating")

        if user_name and product_name and review_text and star_rating:
            Review.objects.create(
                user_name=user_name,
                product_name=product_name,
                review_text=review_text,
                star_rating=int(star_rating)
            )
            return redirect('Review')

    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'review.html', {"reviews": reviews})

from django.shortcuts import render

def cart(request):
    # Example cart items for beginner-level demo
    cart_items = [
        {"product": {"name": "Resin Art", "price": 20}, "quantity": 2},
        {"product": {"name": "Custom Work", "price": 15}, "quantity": 1},
    ]

    # Calculate total for each item
    for item in cart_items:
        item["total"] = item["product"]["price"] * item["quantity"]

    # Calculate overall total
    total_amount = sum(item["total"] for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_amount": total_amount,
    }
    return render(request, 'Home/cart.html', context)



# Home → only 4/5 products
def home_products(request):
    products = Product.objects.filter(is_featured=True)[:5]
    return render(request, 'home.html', {
        'products': products
    })


def product_list(request):
    products = Product.objects.all()

    search_query = request.GET.get('search', '')
    category_query = request.GET.get('category', '')

    if search_query:
        products = products.filter(name__icontains=search_query)

    if category_query:
        products = products.filter(category=category_query)

    context = {
        'products': products
    }
    return render(request, 'Home/product_list.html', context)

# Category → all category products


def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'Home/product.html', {'products': products})


# Search → search result page
def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(short_description__icontains=query)
    )
    return render(request, 'Home/product.html', {
        'products': products,
        'search': query
    })

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Home/signup.html', {'form': form})














