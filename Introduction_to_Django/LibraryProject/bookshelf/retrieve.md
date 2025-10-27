
```markdown
# Retrieve Operation for Book Model

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books
# Retrieve a single book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
