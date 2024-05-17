from flask import Flask, render_template, request, redirect
from backend.search import and_search, load_index
import os

results = None
query = ""

# Set the folder paths for html and css files for Flask
template_dir = os.path.abspath('frontend/templates')
static_dir = os.path.abspath('frontend/static')

# Instantiate Flask
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Main route - displays search bar and search button
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    # POST request sends search query to backend and retrieves results
    if request.method == 'POST': 
        global query
        global results

        query = request.form.get('search-input')
        words = query.split()
  
        results = and_search(words)
        return redirect("/search")

  
    return render_template('index.html') 

# Generates HTML file with query results
@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html', query=query, links=results)

 
if __name__ == '__main__':
    # Load index to memory before app runs
    load_index()

    # Initiate server
    app.run(host='localhost', port='8000')