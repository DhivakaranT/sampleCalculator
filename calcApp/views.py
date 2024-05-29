from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def display(request):
    n1=int(request.POST["txtno1"])
    n2 = int(request.POST["txtno2"])
    v1 = request.POST["operation"]
    if v1=="Add":
        result=n1+n2
    elif v1=="Sub":
        result=n1-n2
    elif v1=="Mul":
        result=n1*n2
    else:
        result=0

    return render(request,'home.html',{"n1":n1,"n2":n2,"res":result})