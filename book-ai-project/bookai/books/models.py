from django.db import models

# Book model represents each knowledge source used in the RAG system
# Each record acts like a "document" from which answers are retrieved
class Book(models.Model):

    # Title of the book (used for matching user queries)
    title = models.CharField(max_length=100)

    # Author name (not used in logic, but useful for completeness)
    author = models.CharField(max_length=100)

    # Main content/description of the book
    # This is what gets returned as answer to the user
    description = models.TextField()

    # Optional external reference link (not currently used in UI)
    link = models.URLField(blank=True)

