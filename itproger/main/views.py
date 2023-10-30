from django.shortcuts import render

def index(request):
    # 'values': ['Ivanov', 'Petro', 'Sidorenko', 'Mamaladze', 'Goridze', 'jon Silver']
    data = {
        'h1': 'List orders',
        'values': ['make a symbol table',
                   'make site',
                   'make super site',
                   'find the error',
                   'make right all',
                   'create a ball']
            }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
