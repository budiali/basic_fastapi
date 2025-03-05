from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "category": "fantasy"
    },
    {
        "title": "Jurassic Park",
        "author": "Michael Crichton",
        "category": "science fiction"
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",      
        "category": "thriller"
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "adventure"
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "category": "novel"
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "category": "fantasy"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "novel"
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "category": "science fiction"
    },
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",        
        "category": "novel"
    },
    {
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "category": "fantasy"
    }
]