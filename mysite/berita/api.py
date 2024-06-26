from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from berita.serializer import BiodataSerializer, KategoriSerializer, ArtikelSerializer
from berita.models import Kategori, Artikel
from pengguna.models import Biodata

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_author_list(request):
    user = Biodata.objects.all()
    serializer = BiodataSerializer(Biodata, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_kategori_list(request):
    kategori = Kategori.objects.all()
    serializer = KategoriSerializer(kategori, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT', 'POST'])
@permission_classes((permissions.AllowAny,))
def api_kategori_detail(request, id_kategori):
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except:    
        return Response({'message:data kategori ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":  
        serializer = KategoriSerializer(kategori, many=False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:pass
   
    
    
api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def api_kategori_add(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_artikel_list(request):
    key_token = "5fe9c4804ac04ec5f100bf7ae68151b903131304807603eda6b98be753d80f1e"
    
    token = request.headers.get('token')
    if token == None:
        if token != key_token:
            return Response({'message:Masukan Token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if token != key_token:
            return Response({'message:Masukan Token yang benar'}, status=status.HTTP_401_UNAUTHORIZED)
    
    kategori = Artikel.objects.all()
    serializer = ArtikelSerializer(Artikel, many=True)
    data = {
        'count': Artikel.count(),
        'rows': serializer.data
    } 
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
@permission_classes((permissions.AllowAny,))
def api_artikel_detail(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
    except:    
        return Response({'message:data artikel ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArtikelSerializer(artikel, many=False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
         serializer = ArtikelSerializer(artikel, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == "DELETE" :
        artikel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def api_artikel_add(request):
    print("Lidan")
    serializer = ArtikelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)