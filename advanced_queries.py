import json


# cross_fields


def multi_match_agg_cross(query, fields):
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
			"BirthPlace Filter": {
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"Book Filter": {
				"terms": {
					"field": "book_list.keyword",
					"size": 10
				}
			},
			"Author Filter": {
				"terms": {
					"field": "author_name.keyword",
					"size": 10
				}
			},
			"Category Filter": {
				"terms": {
					"field": "category.keyword",
					"size": 10
				}
			}
		}
    }

    q = json.dumps(q)
    return q


# phrase_fields
def multi_match_agg_phrase(query, fields=['author_name']):
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
                # "type": "phrase_prefix"
            }
        },
		"aggs": {
			"BirthPlace Filter": {
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"Book Filter": {
				"terms": {
					"field": "book_list.keyword",
					"size": 10
				}
			},
			"Author Filter": {
				"terms": {
					"field": "author_name.keyword",
					"size": 10
				}
			},
			"Category Filter": {
				"terms": {
					"field": "category.keyword",
					"size": 10
				}
			}
		}
    }

    q = json.dumps(q)
    return q

