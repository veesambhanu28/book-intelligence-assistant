from django.urls import path
from .views import get_books, ask_question, home

# URL routing for the books app
# Maps frontend requests to corresponding backend view functions
urlpatterns = [

    # Home route → loads main UI (index.html)
    path('', home),

    # API route → returns list of all books (used to display available books)
    path('books/', get_books),

    # API route → handles user questions and returns AI response
    path('ask/', ask_question),
]