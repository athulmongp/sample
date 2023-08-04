from django.shortcuts import render

def home_page(request):
    return render(request,"home.html")

def calculate(request):
    c=''
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            op=request.POST.get('op')

            if op=="+":
                c=n1+n2

            elif op=="-":
                c=n1-n2

            elif op=="*":
                c=n1*n2        

            elif op=="/":
                c=n1/n2
    except:
        c="invalid" 
    print(c)    

    return render(request,"home.html",{'result':c})    