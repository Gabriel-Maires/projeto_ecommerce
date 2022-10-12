from django.shortcuts import render

# Create your views here.
def produto_page(request):
    return render(request, 'produto_page.html')