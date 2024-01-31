from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]

@app.route('/', methods=['GET'])
def get_books():
    # Get query parameters
    genre = request.args.get('genre')
    author = request.args.get('author')
    title = request.args.get('title')

    # Filter books based on query parameters
    filtered_books = books.copy()

    if genre:
        filtered_books = [book for book in filtered_books if genre.lower() in book['genre'].lower()]

    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    return jsonify({"books": filtered_books})

if __name__ == '__main__':
    app.run(debug=True)