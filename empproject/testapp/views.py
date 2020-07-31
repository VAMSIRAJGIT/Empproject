from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

# Create your views here.
def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',context=my_dict)