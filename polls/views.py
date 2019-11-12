from django.http import HttpResponseForbidden, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import serializers
from . import models



@api_view(['GET', 'POST'])
def post_view(request):
    if request.method == 'GET':
        try:
            post_query = models.Post.objects.all().order_by(('created'))
        except models.Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PostSerializer(post_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            comment_query = models.Comment.objects.all().order_by(('post'))
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(comment_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def comment(request):
    if request.method == 'POST':
        try:
            comment_query = models.Comment.objects.all().order_by('post')
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(comment_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def image_view(request):
    if request.method == 'GET':

        try:
            comment_query = models.UploadImageTest.objects.all().order_by('name')
            print(comment_query)
        except models.UploadImageTest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ImageSerializer(comment_query, many=True)
        return HttpResponse(serializer.data,  content_type="image/jpg")

