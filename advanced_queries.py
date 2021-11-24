import json

# best_fields


def multi_match_agg_best(query, fields=['name', 'about_author']):
    print("QUERY FIELDS")
    print(fields)
    q = {
        "size": 986,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": 'or',
                "type": "best_fields"
            }
        },
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "dob.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "birthplace.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "education.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "booklist.keyword",
                    "size": 10
                }
            },
            "Language Filter": {
                "terms": {
                    "field": "language.keyword",
                    "size": 10
                }
            }
        }
    }

    q = json.dumps(q)
    return q


# cross_fields


def multi_match_agg_cross(query, fields=['name', 'about_author']):
    print("QUERY FIELDS")
    print(fields)
    q = {
        "size": 986,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": 'or',
                "type": "cross_fields"
            }
        },
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "dob.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "birthplace.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "education.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "booklist.keyword",
                    "size": 10
                }
            },
            "Language Filter": {
                "terms": {
                    "field": "language.keyword",
                    "size": 10
                }
            }}
    }

    q = json.dumps(q)
    return q


# phrase_fields
def multi_match_agg_phrase(query, fields=['name', 'about_author']):
    print("QUERY FIELDS")
    print(fields)
    q = {
        "size": 986,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": 'or',
                "type": "phrase_prefix"
            }
        },
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "dob.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "birthplace.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "education.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "booklist.keyword",
                    "size": 10
                }
            },
            "Language Filter": {
                "terms": {
                    "field": "language.keyword",
                    "size": 10
                }
            }}
    }

    q = json.dumps(q)
    return q

