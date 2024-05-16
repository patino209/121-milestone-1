from flask import Flask, render_template, request, redirect
from search import and_search

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST': 
        query = request.form.get('search-input')
        words = query.split()
  
        results = and_search(words)
        return redirect("/search")

  
    return render_template('index.html') 


@app.route('/search', methods=['GET'])
def search():
   

 
if __name__ == '__main__':
   app.run(host='localhost', port='8000')