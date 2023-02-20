# RECOMMENDER SYSTEM
___
#  Book Recommender System Using KNN Clustering
___
- This code is a web application for a book recommender system that uses the K-Nearest Neighbors algorithm for clustering. The user can select a book from a dropdown menu, and upon clicking the "RECOMMEND" button, the system will recommend five books that are similar to the selected book.

- The system loads the required data from three pickle files: "book_pivot.pkl", "nn_model.pkl", and "title.pkl". "book_pivot.pkl" contains a pivot table of the book ratings data, "nn_model.pkl" contains the trained KNN model, and "title.pkl" contains a list of book titles. These pickle files are loaded using the "pickle" module.
___
- The "recommend" function takes in the selected book as input, and returns five recommended books based on the KNN algorithm. The function first identifies the index of the selected book in the pivot table, and then calculates the distances and suggestions using the KNN model. The recommended books are returned as a list.
def recommend(book):
    ind=np.where(book_pivot.index==book)[0][0]
    distances, suggestion=model.kneighbors(book_pivot.iloc[ind, :].values.reshape(1, -1), n_neighbors=6)
    rec_book=[]
    for j in range((len(suggestion))):
        rec_book.append(book_pivot.index[suggestion[j]])
    return rec_book

___
- The user interface is created using the "streamlit" library. The app has two tabs: "WEB APP FOR BOOK RECOMMENDATION" and "ABOUT". The first tab allows the user to select a book and receive recommendations. The second tab provides a brief explanation of the app and a link to the developer's Github repository.

- The app also includes a background image that is loaded from a local file using the "base64" and "os" modules. The image is added to the page using HTML/CSS code in a Markdown string.

- Finally, the app includes a "random_emoji" function that randomly selects an emoji from a list of eight emojis. This function is called when the "RECOMMEND" button is clicked, but it is commented out in the code.
___
## .[Model Building Notebook](https://github.com/asjad895/RECOMMENDER-SYSTEM/blob/main/BOOK%20RECOMMENDER(CLUSTERING)/book.ipynb)
## .Result:
![WebApp Response](https://www.loom.com/share/18da53f9264b41a0ad8238a58ae5ee9a)

