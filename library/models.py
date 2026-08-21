from django.db import models

class Catagory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} of {self.category} by {self.publisher}'

class Author(models.Model):
      name = models.CharField(max_length=255)
      email = models.EmailField(max_length=255)
      books = models.ManyToManyField(
          Book,
          through='Authorbook'
      )

      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
        return f'{self.name}'

class Authorbook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return f'{self.book.title} by {self.author.name}'

class Booksdetail(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn= models.CharField(max_length=255)
    pages = models.IntegerField()
    language = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book.title} with {self.pages} in {self.language}'


