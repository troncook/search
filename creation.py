import os

# Define the base directory
base_dir = r"C:\Users\colto\OneDrive\Desktop\startup\search_engine"

# List of subdirectories to create
sub_dirs = ['templates', 'static']

# Create the subdirectories
for sub_dir in sub_dirs:
    os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)

# Create the app.py file with the flask application code
app_file_content = '''
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data
df = pd.read_csv(
    'business_contracts_dataset.csv', 
    dtype={
        'ContractValue': 'float32', 
        'Jurisdiction': 'category',
        'ContractStatus': 'category',
        'StartDate': 'object',
        'EndDate': 'object',
        'RenewalDate': 'object'
    }
)

date_columns = ['StartDate', 'EndDate', 'RenewalDate']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Create a dictionary
data_dict = df.set_index('ContractID').T.to_dict('dict')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    results = [value for key, value in data_dict.items() if query.lower() in str(value).lower()]
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
'''

with open(os.path.join(base_dir, 'app.py'), 'w') as app_file:
    app_file.write(app_file_content)

# Create the index.html file with the basic search interface
index_file_content = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Contract Search Engine</title>
  </head>
  <body>
    <div class="container mt-5">
      <h1>Search Contracts</h1>
      <form action="/search" method="post">
        <div class="mb-3">
          <input type="text" class="form-control" name="query" placeholder="Enter search query">
        </div>
        <button type="submit" class="btn btn-primary">Search</button>
      </form>
    </div>
  </body>
</html>
'''

with open(os.path.join(base_dir, 'templates', 'index.html'), 'w') as index_file:
    index_file.write(index_file_content)

# Create the results.html file to display search results
results_file_content = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Search Results</title>
  </head>
  <body>
    <div class="container mt-5">
      <h1>Search Results</h1>
      <a href="/">Back to Search</a>
      <div class="mt-3">
        {% for result in results %}
          <div class="card mb-3">
            <div class="card-body">
              {{ result }}
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
  </body>
</html>
'''

with open(os.path.join(base_dir, 'templates', 'results.html'), 'w') as results_file:
    results_file.write(results_file_content)

print("File structure created successfully!")
