from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
import advanced_queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'author-index'

""
syn_writer_sin=["ලියපු" , "ලියන", "ලද", "රචනා", "කළ", "රචකයා", "කතුවරයා"]
syn_writer_eng=["written", "by","wrote","write","writer","author"]
syn_birthplace_sin=["උපත" ,"ලැබූ" , "උපන්" "ස්ථානය", "නගරය", "ගම"]
syn_birthplace_eng=["birth place" ,"from", "town","city", "hailing from"]
syn_language_sin=['භාෂා', 'බස','භාෂාව','බසින්']
syn_language_eng=['language', 'written in']

syn_booklist = ["පොත",  "පොතේ","නවකතාව","කෙටිකතාව"]
synonym_education = [ 'අධ්‍යාපනය', 'ලැබූ','ඉගෙනුම', 'ලැබූ', 'ඉගෙන ගත්ත']

synonym_list = [syn_writer_sin, syn_writer_eng, syn_birthplace_sin, syn_birthplace_eng, syn_language_sin, syn_language_eng,syn_booklist ,synonym_education]



def search(search_query):
    processed_query = ""
    tokens = search_query.split()
    processed_tokens = search_query.split()
    search_fields = []
    sort_num = 0
    field_list = ["author_name","author_name_english", "birth_place", "birth_place_english","language","language","booklist","school"]
    all_fields = ["author_name","birthplace","date_of_birth", "birth_place", "school", "booklist", "about_author", "language", "category","author_name_english","birth_place_english"]
    final_fields = []

    for word in tokens:
        print (word)

        for i in range(len(synonym_list)):
            
            if word in synonym_list[i]:
                print (i)
                print('Adding field', field_list[i], 'for ', word, 'search field list')
                search_fields.append(field_list[i])
                if(field_list[i]=="author_name"):
                    search_fields.append(field_list[i+1])
                if(field_list[i]=="author_name_english"):
                    search_fields.append(field_list[i-1])
                if(field_list[i]=="birth_place"):
                    search_fields.append(field_list[i+1])
                if(field_list[i]=="birth_place_english"):
                    search_fields.append(field_list[i-1])
                if(field_list[i]=="author_name"):
                    search_fields.append(field_list[i+1])
                
                processed_tokens.remove(word)

    if (len(processed_tokens)==0):
        processed_query = search_query
    else:
        processed_query = " ".join(processed_tokens)

    ##Boosting
    # for field in all_fields:
    #     if (field in search_fields):
    #         final_fields.append(field+"^5")
    #     else:
    #         final_fields.append(field)
    final_fields = search_fields
    # print("FINAL FEELDS : ",final_fields)
    
    if(len(search_fields)==0):
        query_es = advanced_queries.multi_match_agg_cross(processed_query, all_fields)
        
    else:
        query_es = advanced_queries.multi_match_agg_phrase(processed_query, list(set(final_fields)))

    # else:
    #     print('Range Query')
    #     if (len(search_fields) == 0):
    #         query_es = advanced_queries.multi_match_agg_sort_cross(processed_query, sort_num, all_fields)
    #     elif (len(search_fields) == 2):
    #         query_es = advanced_queries.multi_match_agg_sort_phrase(processed_query, sort_num, all_fields)
    #     else:
    #         query_es = advanced_queries.multi_match_agg_sort_cross(processed_query, sort_num, final_fields)

    print("QUERY BODY")
    print(query_es)
    search_result = client.search(index=INDEX, body=query_es)
    return search_result





