from django.shortcuts import render, redirect

# Create your views here.

from .models import UserDetails

from .forms import USerForms

def HomeViews(request):
    data = UserDetails.objects.all()

    # for i in data:
    #     print(i)

    context = {
        'data':data
    }

    return render(request, 'index.html', context)


def DetailsView(request, id):

    data = UserDetails.objects.get(id=id)
    print(data)

    context = {
        'data':data
    }

    return render(request, 'details.html', context)




def CreateViews(request):
    form_data = USerForms(request.POST or None)
    if form_data.is_valid():
        form_data.save()
        return redirect('HomeViews')
        

    context = {
        'form_data':form_data
    }
    return render(request, 'create.html', context)


def DeleteView(request, id):
    data = UserDetails.objects.get(id=id)
    data.delete()
    print('sam')
    return redirect('HomeViews')