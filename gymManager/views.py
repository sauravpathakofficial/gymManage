from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import createMembership,createMember
from .models import GymMembership,GymMember
from django.urls import reverse

def home(request):
    return render(request, 'gymManager/gymManager.html')

     

def membership(request):
  mydata = GymMembership.objects.all().values()
  context = {
    'mymembers': mydata,
  }
  return render(request,'gymManager/membership.html',context)

def member(request):
  mydata = GymMember.objects.all().values()
  context = {
    'mymembers': mydata,
  }
  return render(request,'gymManager/member.html',context)


def createGymMemberShip(request):
    if request.POST:
        form =createMembership(request.POST,request.FILES)
        for key, value in request.POST.items():
            print('Key: %s' % (key) ) 
            print('Value %s' % (value) )

        if form.is_valid():
            form.save()
            # return render(request,'gymManager/card.html')
        return redirect('/')    
    return render(request,'gymManager/createGymMembership.html',{'form':createMembership})    

def createGymMember(request):
    if request.POST:
        form =createMember(request.POST)
        # for key, value in request.POST.items():
        #     print('Key: %s' % (key) ) 
        #     print('Value %s' % (value) )

        if form.is_valid():
            form.save()

        return redirect('/')    
    return render(request,'gymManager/createGymMember.html',{'form':createMember})     

  
def updateGymMembership(request, id):
  mymember = GymMembership.objects.get(id=id)
  template = loader.get_template('gymManager/updateGymMembership.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updateGymMembershipRecord(request, id):
  membership = request.POST['membership']
  instructor = request.POST.get('instructor',False)
  time = request.POST.get('time',False)
  capacity=request.POST.get('capacity',False)
  temp = GymMembership.objects.get(id=id)
  temp.membership = membership
  temp.instructor = instructor
  temp.time=time
  temp.capacity=capacity
 
  temp.save()
  return redirect('/') 


  
def updateGymMember(request, id):
  mymember = GymMember.objects.get(id=id)
  template = loader.get_template('gymManager/updateGymMember.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updateGymMemberRecord(request, id):
  name = request.POST['name']
  email = request.POST.get('email',False)
  phone = request.POST.get('phone',False)
  membership=request.POST.get('membership',False)
  temp = GymMember.objects.get(id=id)
  temp.membership = membership
  temp.name = name
  temp.email=email
  temp.phone=phone
 
  temp.save()
  return redirect('/') 



