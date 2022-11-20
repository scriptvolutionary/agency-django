from django.shortcuts import render

from estate.models import Holder, Immovable, Realtor


def immovable_list(request):
    immovables = Immovable.objects.all()

    return render(request, 'immovable/list.html', {'immovables': immovables})


def holder_list(request):
    holders = Holder.objects.all()

    return render(request, 'holder/list.html', {'holders': holders})


def realtor_list(request):
    realtors = Realtor.objects.all()

    return render(request, 'realtor/list.html', {'realtors': realtors})
