from django.shortcuts import render, HttpResponse, redirect
from .models import Review
# Create your views here.


def index(request):
    return render(request, 'Home/index.html')
# return HttpResponse("This is home page")


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


def product(request):
    return render(request, 'product.html')
