from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class newsUpdata(UpdateView):
    model = Artiles
    template_name = 'news/new.html'
    form_class = ArtilesForm

class newsDelete(DeleteView):
    model = Artiles
    success_url = '/news'
    template_name = 'news/news-del.html'
    context_object_name = 'artiles'

class newsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'artiles'

def new(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form filled invalid'
    form = ArtilesForm()
    data = {'form': form, 'error': error}
    return render(request, 'news/new.html', data)
