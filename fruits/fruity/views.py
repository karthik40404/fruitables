from django.shortcuts import render

def fruity(req):
    return render(req, 'index.html')

def contact(req):
    return render(req, 'contact.html')
