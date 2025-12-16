from django.shortcuts import render, HttpResponse, redirect
from .models import Review, Product
from django.db.models import Q
# Create your views here.


def index(request):
    products = Product.objects.filter(is_featured=True)[
        :5]  # 4-5 featured products
    return render(request, 'Home/index.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


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


def cart(request):
    return render(request, 'cart.html')


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
