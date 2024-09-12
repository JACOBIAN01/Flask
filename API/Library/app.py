from flask import Flask,jsonify,request

app = Flask(__name__)


books_list  = [
    {
        "id": 1,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
    },
    {
        "id": 2,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
    },
    {
        "id": 4,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
    },
    {
        "id": 5,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
    }
]


@app.route('/books', methods = ['GET','POST'])
def books():
    if request.method == 'GET':
        if (len(books_list)>0):
            return jsonify(books_list)
        else:
            'Nothing Found', 404
    
    if request.method =='POST':
        new_author = request.form['author']
        new_title = request.form['title']
        new_year = request.form['year']
        new_id = books_list[-1]['id']+1

        new_obj ={
            'id':new_id,
            'title':new_title,
            'author':new_author,
            'year':new_year
        }

        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id']==id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id']==id:
                book['author'] = request.form['author']
                book['title'] = request.form['title']
                book['year'] = request.form['year']
                update_book ={
                    'id':id,
                    'author':book['author'],
                    'title':book['title'],
                    'year':book['year'],
                }
                return jsonify(update_book)
    if request.method == 'DELETE':
        for index ,book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


        

if __name__ == '__main__':
    app.run(debug=True)
    



        