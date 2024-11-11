from django.shortcuts import render

def fruity(req):
    return render(req, 'index.html')
