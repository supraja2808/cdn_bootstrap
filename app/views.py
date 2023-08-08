from django.shortcuts import render

# Create your views here.
def cdn_bootstrap(request):
    return render(request,'cdn_bootstrap.html')

def badges(request):
    return render(request,'badges.html')

def breadcrumb(request):
    return render(request,'breadcrumb.html')

def buttons(request):
    return render(request,'buttons.html')

def button_group(request):
    return render(request,'button_group.html')

def card(request):
    return render(request,'card.html')

def carousel(request):
    return render(request,'carousel.html')

def collapse(request):
    return render(request,'collapse.html')

def dropdowns(request):
    return render(request,'dropdowns.html')

def forms(request):
    return render(request,'forms.html')

def input_group(request):
    return render(request,'input_group.html')


def jumbortan(request):
    return render(request,'jumbortan.html')

def list_group(request):
    return render(request,'list_group.html')





