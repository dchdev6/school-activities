from flask import Flask, render_template, request, redirect, url_for
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables when the app starts
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    book = Book(
        isbn=request.form['isbn'],
        title=request.form['title'],
        author=request.form['author'],
        copyright=request.form['copyright'],
        edition=request.form['edition'],
        price=float(request.form['price']),
        qty=int(request.form['qty'])
    )
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit_book(id):
    book = Book.query.get(id)
    if book:
        book.isbn = request.form['isbn']
        book.title = request.form['title']
        book.author = request.form['author']
        book.copyright = request.form['copyright']
        book.edition = request.form['edition']
        book.price = float(request.form['price'])
        book.qty = int(request.form['qty'])
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
