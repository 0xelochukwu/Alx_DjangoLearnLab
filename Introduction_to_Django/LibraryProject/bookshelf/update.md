```markdown
# Update Operation for Book Model

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book = Book.objects.get(id=book.id)
book.title
