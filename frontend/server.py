from flask import Flask, render_template, request, redirect
from search import and_search
import time

app = Flask(__name__)
results = None
query = ""
 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST': 
        global query
        query = request.form.get('search-input')
        words = query.split()
  
        global results
        results = and_search(words)
        return redirect("/search")

  
    return render_template('index.html') 


@app.route('/search', methods=['GET'])
def search():
    print(results)

    html = "<h1>Results for query: " + query + "<br>"
    for url in results:
       html += url
       html += "<br>"
    
    html += "</h1>"

    return html

 
if __name__ == '__main__':
   app.run(host='localhost', port='8000')