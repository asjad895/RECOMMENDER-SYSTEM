from flask import Flask, render_template, request,redirect,url_for
import pickle
import numpy as np

app = Flask(__name__)

book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
model = pickle.load(open('nn_model.pkl', 'rb'))
title = pickle.load(open('title.pkl', 'rb'))

def recommend(book):
    ind = np.where(book_pivot.index==book)[0][0]
    distances, suggestion = model.kneighbors(book_pivot.iloc[ind, :].values.reshape(1, -1), n_neighbors=6)
    rec_book = []
    for j in range((len(suggestion))):
        rec_book.append(book_pivot.index[suggestion[j]])
    return rec_book

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/documentation")
def doc():
    return render_template('doc.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_book = request.form.get('book')
        recom_m = recommend(selected_book)
        return redirect(url_for('recommendation'))
    else:
        return render_template('index.html', books=title)

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        # do something with the recommendation form data
        selected_book = request.form.get('book')
        recom_m = recommend(selected_book)
        return render_template('recommendation.html', recommended_books=recom_m)
    return render_template('recommendation.html')



if __name__ == '__main__':
    app.run(debug=True)