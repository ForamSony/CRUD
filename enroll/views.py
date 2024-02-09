from django.shortcuts import render
from .forms import studentregistration
from .models import student
from django.http import HttpResponseRedirect

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = (studentregistration(request.POST))
        if fm.is_valid():
          fm.save()
    else:
        fm = studentregistration()    
    stu = student.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'st':stu})

# def update_data(request,id):
#     return render(request,'enroll/updatestd.html',{'id':id})

def update_data(request,id):
    
    if request.method == 'POST':
       pi = student.objects.get(pk=id)
       fm = studentregistration(request.POST,instance=pi)
       if fm.is_valid():
          fm.save()
    else:
          pi = student.objects.get(pk=id)
          fm = studentregistration(instance=pi)
    return render(request,'enroll/updatestd.html', {'form':fm})

def delete_data(request,id):
    
    if request.method == 'POST':
       pi = student.objects.get(pk = id)
       pi.delete()
       return HttpResponseRedirect('/') 