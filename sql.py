from bookclub.models import Author, Book, Reader, BookReading

books = Book.objects.all().select_related('author')
Book.objects.all().values('author', 'title') # dict, например, для дальнейшей сериализации данных в JSON

Book.objects.all().values_list('author', 'title') # Список
Book.objects.all().values_list('author', flat=True) #<QuerySet [1, 2, 2, 2, 3, 4, 4, 5, 6]>