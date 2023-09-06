from django.shortcuts import render

def show_main(request):
    context = {
        'name': "Adrian",
        'class': 'PBP D'
    }

    return render(request, 'main.html', context)

# Create your views here.
