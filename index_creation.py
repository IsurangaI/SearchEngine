from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json
import re
import os
client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'author-index'


def createIndex():
    settings = {
        "settings": {
            "index": {
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis": {
                "analyzer": {
                    "sinhala-analyzer": {
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter": ["edge_ngram_custom_filter"]
                    }
                },
                "filter": {
                    "edge_ngram_custom_filter": {
                        "type": "edge_ngram",
                        "min_gram": 2,
                        "max_gram": 50,
                        "side": "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "Name": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",         
                },
                "dob": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "birthplace": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "education": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "booklist": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "about_author": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "language": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",

                },


                "category": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",

                }

            }
        }
    }

    # index = Index(INDEX,using=client)
    # result = index.create()
    result = client.indices.create(index=INDEX, body=settings)
    print(result)


def read_authors():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file1 = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file1, 'formatted_authors.json')

    with open(my_file, 'r', encoding='utf-8-sig') as tra_file:
        authors = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(authors) if a not in authors[num + 1:]]
        return results_list

def data_generation(author_array):
    for author in author_array:

        name = author["author_name"]
        
        author_name_english = author["author_name_english"]
        dob = author["date_of_birth"]
        birthplace = author["birth_place"]

        education = author["school"]
        book_list = author["book_list"]
        about = author["about_author"]
        languages = author["language"]

        category = author["category"]

        yield {
            "_index": INDEX,
            "_source": {
                "name": name,
                "dob": dob,
                'birthplace': birthplace,
                "education": education,
                "booklist": book_list,
                "about_author": about,
                "language": languages,
                "author_name_english" : author_name_english,
                "category": category
            },
        }


createIndex()
tra_authors = read_authors()
helpers.bulk(client, data_generation(tra_authors))
