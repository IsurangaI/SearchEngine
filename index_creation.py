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
                    "search_analyzer": "standard"
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
                    "search_analyzer": "standard"
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
                    "search_analyzer": "standard"
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
                    "search_analyzer": "standard"
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
                    "search_analyzer": "standard"
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
                    "search_analyzer": "standard"
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
                    "search_analyzer": "standard"

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
                    "search_analyzer": "standard"

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
    my_file = os.path.join(my_file1, 'Authours.json')

    with open(my_file, 'r', encoding='utf8') as tra_file:
        authors = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(authors) if a not in authors[num + 1:]]
        return results_list


def clean_function(song_lyrics):
    if (song_lyrics):
        processed_list = []
        song_lines = song_lyrics.split('\n')

        for place,s_line in enumerate(song_lines):
            process_line = re.sub('\s+',' ',s_line)
            punc_process_line = re.sub('[.!?\\-]', '', process_line)
            processed_list.append(punc_process_line)

        sen_count = len(processed_list)
        final_processed_list = []

        for place,s_line in enumerate(processed_list):
            if (s_line=='' or s_line==' '):
                if (place!= sen_count-1 and (processed_list[place+1]==' ' or processed_list[place+1]=='')) :
                    pass
                else:
                    final_processed_list.append(s_line)
            else:
                final_processed_list.append(s_line)
        final_song_lyrics = '\n'.join(final_processed_list)
        return final_song_lyrics
    else:
        return None

def data_generation(author_array):
    for author in author_array:

        name = author["name"]
        # dob = clean_function(author["song_lyrics"])
        dob = author["dob"]
        birthplace = author["birthplace"]

        education = author["education"]
        book_list = author["booklist"]
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
