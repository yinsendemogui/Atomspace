from website.models import Video
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


class VideoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1)
    class Meta:
        model = Video
        fields = '__all__'



@api_view(['GET'])
def video(request):
    if request.method == 'GET':
        video_list = Video.objects.order_by('-id')
        serializer = VideoSerializer(video_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

