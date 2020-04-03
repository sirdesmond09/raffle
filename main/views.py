from django.shortcuts import redirect, render
from .models import Number
import random
import time
# Create your views here.

def create(request):

    if request.method == "POST":
        title    = request.POST.get('title')
        enteries = request.POST.get('enteries')

        new_entery = Number.objects.create(title = title, enteries = enteries)
    
        return redirect('/')

    return render(request, 'base.html',)


def draw(request):

    if request.method == "POST":
        draws    = request.POST.get('draw')
        title    = request.POST.get('entery')
        print(draws)



        chosen = []

        numbers = Number.objects.get(title = title)
        num = numbers.enteries

        num_list = [x for x in num.split(',')]
        print(num_list)

        if int(draws) < len(num_list):
            for i in range(int(draws)):
                choice = random.choice(num_list)
                chosen.append(choice)
                num_list.remove(choice)
                
                context = {
                    choice : choice
                    }
                print('\n\n', choice)
                print('\n\n', chosen)
                time.sleep(3)

            
                return(context)
            return render(request,context)

    return render(request, 'numbers.html')