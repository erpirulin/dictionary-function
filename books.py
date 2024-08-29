books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}
 
book = input()
 
#cambiar esta parte para usar el método .get()
if book in books:
    print(books.get(book))
else:
    print("Book not found")
