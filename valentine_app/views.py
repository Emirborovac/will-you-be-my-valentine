from django.shortcuts import render

def valentine(request):
    return render(request, 'valentine.html')
