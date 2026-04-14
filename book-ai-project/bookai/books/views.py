from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json
import re
import random

# Simple in-memory cache to store previous answers
# Helps avoid repeated processing for same questions
cache = {}

# Renders the main UI page
def home(request):
    return render(request, 'index.html')

# API to return all books data (used in frontend)
def get_books(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

# Main API for handling user questions
@csrf_exempt
def ask_question(request):
    if request.method == "POST":

        # Parse incoming JSON data from frontend
        data = json.loads(request.body)

        # Clean and normalize the question (remove special chars + lowercase)
        question = re.sub(r'[^\w\s]', '', data.get("question", "").lower())

        # Handle empty input case
        if not question:
            return JsonResponse({"answer": "Please enter a valid question."})

        # Check if answer already exists in cache (optimization)
        if question in cache:
            return JsonResponse({"answer": cache[question]})

        # Fetch all books from database
        books = Book.objects.all()

        answers = []
        matched_titles = set()

        # Loop through books and match based on title
        for book in books:
            title = book.title.lower()

            # Basic keyword matching logic
            if title in question or title in question.split():

                # Avoid duplicate answers
                if book.title not in matched_titles:
                    answers.append(book.description)
                    matched_titles.add(book.title)

        # If exactly one match found
        if len(answers) == 1:
            final_answer = answers[0]

        # If multiple matches, return top 2 results
        elif len(answers) > 1:
            final_answer = "\n\n".join(answers[:2])

        # If no match found, return fallback generic response
        else:
            responses = [
                f"{question.capitalize()} is an important concept in technology.",
                f"{question.capitalize()} is widely used in modern systems.",
                f"{question.capitalize()} helps solve real-world problems."
            ]
            final_answer = random.choice(responses)

        # Store result in cache for faster future access
        cache[question] = final_answer

        return JsonResponse({"answer": final_answer})

    # Handle invalid request methods
    return JsonResponse({"answer": "Invalid request"})