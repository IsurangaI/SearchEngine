
# **Setting up the Environment** 

* Download and Install the ElasticSearch <br/>
* Install the ICU_Tokenizer plugin on the ElasticSearch<br/>
* Install the python3 with pip3<br/>
* git clone https://https://github.com/nigma97/SearchEngine <br/>
* cd Search_eng_asg<br/>
* python -m venv env<br/>
* env/Scripts/activate<br/>
vpip install -r requirements.txt<br/>

# **Running the Project** 
* First start the ElasticSearch locally on port 9200.<br/>
* Then run index_creation.py file to create the index and insert data.<br/>
* Next run the main.py to start the search engine.<br/>
* Then visit http://localhost:5000/ for see the user interface.<br/>
* Finally add your search query in the search box for searching.<br/>

# **File structure** 
* data - Folder contains scraped data with python code used for format the json<br/>
* templates - Folder contains Html user interface of the search engine<br/>
* documents - Folder contains project proposal & project report<br/>
* images - Folder contains diagrams used in README.md<br/>
* index_creation.py - Python code for index creating and data inserting<br/>
* search_function.py - Python code use for process search query<br/>
* advanced_queries.py - Elastic Search queries<br/>
* requirements.txt - python requirements<br/>

**Basic Functionalities**

* It supports searching by the author,booklist, date of birth, birth_place,school etc.
* Search engine can identify keywords both Sinhala and English like ලියන ලද, උපන්,from, wrote. 
* User can search author names/birthplace in Sinhala or English.

![image](https://user-images.githubusercontent.com/47548926/143293438-9376e0d1-2868-400a-9007-9040271414c1.png)

**● Indexing**
‘ICU tokenizer’standard tokenizer was used for indexing since it supports better for asian
languages.Elastic search ‘edge_ngram’ filter was used to generate n-grams

**● Querying Techniques**
Searched query was tokenized using the “Sinling tokenizer”.<br/>
Keywords are extracted from the search query.<br/>
Increase the weights of the related fields that are identified.<br/>
For the querying, ‘Cross fields’ and ‘Phrase prefix’ multi-match queries were used.<br/>

