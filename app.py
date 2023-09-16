from flask import Flask, render_template, request, redirect, url_for
from spacy import load
from data_loader import load_data

app = Flask(__name__)
nlp = load("en_core_web_trf")
data_dict = load_data()

@app.route('/')
def home():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    sort_by = request.form.get('sort_by')
    order = request.form.get('order')

    if query:
        processed_query = nlp(query.lower())
        # dates = extract_date_range(processed_query)  # Uncomment and define this function to handle date range queries

        # Prepare query for keyword search by removing date entities
        # for date in dates:  # Uncomment once date extraction is implemented
        #     query = query.replace(date, '')
        
        # Create a list of keywords that excludes hyphenated names
        keywords = [token.text for token in nlp(query.lower()) if "-" not in token.text]

        # Add the full query to the keywords list to search for exact matches
        keywords.append(query.lower())

        results = []

        # If date entities are found, filter results based on date range
        # if dates:  # Uncomment once date extraction is implemented
        #     ... (same as previous code)
        # else:  # If no date entities found, use keyword search
        results = [
            value for value in data_dict.values()
            if any(keyword in str(value).lower() for keyword in keywords)
        ]

        if sort_by and sort_by != "none":
            results = sorted(results, key=lambda x: x.get(sort_by), reverse=(order == 'desc'))

        return render_template('results.html', results=results)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)




