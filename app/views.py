from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from app.models import Image
from app.serializers import ImageSerializer


class ImageList(GenericAPIView):
    def get(self, request):
        obj = Image.objects.all()
        serializer = ImageSerializer(obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(GenericAPIView):
    def get(self, request):
        obj = self.get_object()
        serializer = ImageSerializer(obj)
        return Response(serializer.data)

    def put(self, request):
        obj = self.get_object()
        serializer = ImageSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        obj = self.get_object()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MainTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main.html'

    def get(self, request):
        queryset = Image.objects.values('id', 'getting_time', 'time_of_end_converting_job')
        return Response({'images': queryset})