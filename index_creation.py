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
                "author_name": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",         
                },
                "author_name_english": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },     
                },
                "date_of_birth": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "birth_place": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",                   
                },
                "birth_place_english": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },                 
                },
                "school": {
                    "type": "text",
                    "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                    },
                    "analyzer": "sinhala-analyzer",
                },
                "book_list": {
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

    with open(my_file,'r', encoding='utf-8-sig') as tra_file:
        authors = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(authors) if a not in authors[num + 1:]]
        return results_list

def data_generation(author_array):
    for author in author_array:

        author_name = author["author_name"]
        
        author_name_english = author["author_name_english"]
        date_of_birth = author["date_of_birth"]
        birth_place = author["birth_place"]
        birth_place_english = author["birth_place_english"]

        school = author["school"]
        book_list = author["book_list"]
        about = author["about_author"]
        languages = author["language"]

        category = author["category"]

        yield {
            "_index": INDEX,
            "_source": {
                "author_name": author_name,
                "date_of_birth": date_of_birth,
                'birth_place': birth_place,
                'birth_place_english': birth_place_english,

                "school": school,
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
