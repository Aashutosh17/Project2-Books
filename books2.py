from fastapi import FastAPI , Body
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id : str
    title : str
    author : str
    description : str
    rating : int

    def __init__(self,id,title,author, description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id : int
    title : str
    author : str
    description : str
    rating : float = Field(..., ge=0 , le =5)


BOOKS = [
    Book(1,"Introduction to programming", "Aashika",'A Good Book',4.5),
    Book(2, "DSA", "Aashutosh", 'Perfect for interviews', 5),
    Book(3, "DBMS", "Shreyan", 'All about data', 4),
    Book(4, "Operating System", "Alina", 'All about OS and Computers', 5),
]

@app.get("/books")
async def read_all_books():
    return BOOKS



"""# This:
Book(id=5, title="Python for Fun", author="Aashika", description="Learn Python easily", rating="5")

# Is the same as:
Book(**book_request.model_dump())
model_dump() --> Converts Pydantic model to dict
"""
@app.post('/create-book')
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return {"message" : "Book Created successfully!"}




























