import time

from rest_framework import generics, mixins

from books_api.models import Book
from books_api.serializers import BookSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # for see delay in print items from script <is/books.js>
    def list(self, request, *args, **kwargs):
        time.sleep(2)
        return super().list(request, *args, **kwargs)


# If you need customization of certain methods, then you can take ONLY these methods
# class BookDetailsAPIView(mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin,
#                          generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# If don't you need customization of certain methods, then you can take ALL methods
class BookDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

