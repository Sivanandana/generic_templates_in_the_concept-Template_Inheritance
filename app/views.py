from django.shortcuts import render

# Create your views here.
def templatesinheritance(request):
    return render(request,'templatesinheritance.html')
def child(request):
    return render(request,'child.html')