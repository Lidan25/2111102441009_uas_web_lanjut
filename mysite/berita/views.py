from django.shortcuts import render, redirect
from berita.models import Kategori, Artikel
from berita.forms import ArtikelForm


# Create your views here.

def dashboard(request):
  template_name = "dasboard/index.html"
  context = {
    'title': 'halaman dasboard'
  }
  return render(request, template_name, context)

def kategori_list(request):
  template_name = "dasboard/snippets/kategori_list.html"
  kategori = Kategori.objects.all()
  print(kategori)
  context = {
    'title': 'halaman kategori',
    'kategori': kategori
  }
  return render(request, template_name, context)

def kategori_add(request):
  template_name = "dasboard/snippets/kategori_add.html"
  if request.method == "POST":
     nama_input = request.POST.get('nama_kategori')
     Kategori.objects.create (
      nama = nama_input
     )
     return redirect(kategori_list)
    
  pesan = ""
  context = {
    'title': 'tambah kategori',
    'pesan': pesan
  }
  return render(request, template_name, context)

def kategori_update(request, id_kategori):
   template_name = "dasboard/snippets/kategori_update.html"
   try:
      kategori = Kategori.objects.get(id=id_kategori)
   except:
      return redirect(kategori_list)
   if request.method == "POST":
      nama_input = request.POST.get('nama_kategori')
      kategori.nama = nama_input
      kategori.save()
      return redirect(kategori_list)
   
   context = {
     'title': 'update kategori',
     'kategori': kategori
   }
   return render(request, template_name, context)


def kategori_delete(request, id_kategori):
  try:
    Kategori.objects.get(id=id_kategori).delete()
  except:
    pass
  return redirect(kategori_list)

def artikel_list(request):
    template_name = "dasboard/snippets/artikel_list.html"
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
       'title': 'daftar artikel',
       'artikel': artikel
    }
    return render(request, template_name, context)

def artikel_add(request):
    template_name ="dasboard/snippets/artikel_forms.html"
    if request.method == "POST":
       forms = ArtikelForm(request.POST, request.FILES)
       if forms.is_valid():
          pub = forms.save(commit=False)
          pub.author = request.user
          pub.save()
          return redirect(artikel_list)
       else:
          print(forms.error_class)
    forms = ArtikelForm()
    context = {
       'title': 'Tambah artikel',
       'forms': forms
    }
    return render(request, template_name, context)

def artikel_detail(request, id_artikel):
    template_name ='dasboard/snippets/artikel_detail.html'
    artikel = Artikel.objects.get(id=id_artikel)
    context = {
       'title': artikel.judul,
       'artikel': artikel
    }
    return render(request, template_name, context)

def artikel_update(request, id_artikel):
    template_name = "dasboard/snippets/artikel_forms.html"
    artikel= Artikel.objects.get(id=id_artikel)
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
           pub = forms.save(commit=False)
           pub.author = request.user
           pub.save()
           return redirect(artikel_list)
        
    forms = ArtikelForm(instance=artikel)
    context = {
       'title':'Edit artikel',
       'forms' : forms
    }
    return render(request, template_name, context)

def artikel_delete(request, id_artikel):
    try:
       Artikel.objects.get(id=id_artikel).delete()
    except:pass
    return redirect(artikel_list)
