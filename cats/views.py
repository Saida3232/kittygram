# from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics
from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer,CatListSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# @api_view(['GET','POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer= CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
#     cat = Cat.objects.all()
#     serializer = CatSerializer(cat,many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def detail_cat(request, id):
#     cat = Cat.objects.get(id=id)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         cat = Cat.objects.get(id=id)
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = CatSerializer(cat)
#     return Response(serializer.data, status=status.HTTP_200_OK)
# ************************************
# низкоуровневые классы апи
# class APICAT(APIView):
#     def get(self,request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
# ****************************************************************
# дженерики
# class CatList(generics.ListAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
# ****************************************************
# вьюсеты


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        # Нужны только последние пять котиков белого цвета
        cats = Cat.objects.filter(color='White')[:5]
        # Передадим queryset cats сериализатору 
        # и разрешим работу со списком объектов
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return CatListSerializer
        return CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer

#     def get_queryset(self):
#         cat_id = self.kwargs.get('cat_id')
#         new_queryset = Comment.objects.filter(cat=cat_id)
#         return new_queryset
class DeleteUpdateViewSet(mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    pass


class RetrieveCreateViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass


class LightCatViewSet(RetrieveCreateViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
