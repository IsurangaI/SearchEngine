from flask import Flask, render_template, request
from search_function import search
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def search_box():
    if request.method == 'POST':
        print ("POST")
        query = request.form['searchTerm']
        search_result = search(query)
        print (search_result)
        hits_result = search_result['hits']['hits']
        aggregations = search_result['aggregations']
        results_count = len(hits_result)
        return render_template('interface.html',query=query,hits=hits_result,num_results=results_count,aggs=aggregations)
    if request.method == 'GET':
        print ("GET")
        return render_template('interface.html',init='True')

if __name__ == "__main__":
    app.run(debug=True)