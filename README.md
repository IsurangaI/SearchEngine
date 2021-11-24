
The database contains 102 records of authors with fields such as author’s name, birthplace , birthdate,
school, list of his publications, language and category. Most of these data was extracted from
wikipedia.com, peoplepill.com, ranker.com.


● Indexing
‘ICU tokenizer’standard tokenizer was used for indexing since it supports better for asian
languages.Elastic search ‘edge_ngram’ filter was used to generate n-grams

● Querying Techniques
Searched query was tokenized using the “Sinling tokenizer”.
Keywords are extracted from the search query.
Increase the weights of the related fields that are identified.
For the querying, ‘Cross fields’ and ‘Phrase prefix’ multi-match queries were used.

Advanced Features
● The data is extracted from the user’s query using “Rule-based text mining”
Rule-based text mining is used to understand and extract data from the user entered query string.
Keywords related to author name in Sinhala/English, author birth place in Sinhala/English and
author are maintained in different lists.
● If there is a keyword in the query related to a field, the keyword is removed from the query and
performs a ‘phrase-prefix’ type query. If the author name was typed in English, it’s added to the
author name in the English field to the ‘’final fields’’ and a phrase-prefix was performed. If there
is no keyword in the query, ‘cross-field’ is performed.
● Users can search by author name in Sinhala or English, birthplace of the author in Sinhala or
English, birth year, names of the author’s book, author’s school etc


