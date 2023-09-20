from django.shortcuts import render
import datetime
# Create your views here.
def display(request):
    date=datetime.datetime.now()
    msg="hello AIDS students G section"
    t_dict={'DATE':date,'str':msg}
    return render(request,'templapp/test.html',context=t_dict)

