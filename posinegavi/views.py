from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request=request,template_name="posinegavi/home.html")