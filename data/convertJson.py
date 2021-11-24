import json
import codecs
import os

def formatJson() :
    final_author = []
    school_dict = {}
    book_list = {}
    category = {}
    language = {}

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    author_data = json.load(codecs.open(CURRENT_FOLDER + '/Authors.json','r', 'utf-8-sig'))
    print(type(author_data))
    i=0
    for author_record in author_data:
        i = i+1
        complete_author_record = {}
        author_name = author_record["name"]
        if ("name_english" in author_record):
            author_name_english = author_record["name_english"]
        else :
            author_name_english = "දත්ත නොමැත"
        if ("birth_place_english" in author_record):
            birth_place_english = author_record["birth_place_english"]
        else :
            birth_place_english = "දත්ත නොමැත"


        if ("date_of_birth" in author_record):
            date_of_birth = author_record["date_of_birth"]
        else :
            date_of_birth = "දත්ත නොමැත"

        if ("birth_place" in author_record):
            birth_place = author_record["birth_place"]
        else :
            birth_place = "දත්ත නොමැත"

        
        
        if ("school" in author_record):
            school_dict = [x.strip() for x in author_record["school"].split(',')]
        else :
            school_dict = []
            
        if ("book_list" in author_record):
            book_list = [x.strip() for x in author_record["book_list"].split(',')]
        else :
            book_list = []
        
        if ("about_author" in author_record):
            about_author = author_record["about_author"]
        else :
            about_author = "දත්ත නොමැත"

        if ("language" in author_record):
            language = [x.strip() for x in author_record["language"].split(',')]
        else :
            language = []

        if ("category" in author_record):
            category = [x.strip() for x in author_record["category"].split(',')]
        else :
            category = []

        complete_author_record = {
            "author_name": author_name,
            "author_name_english": author_name_english,
            "date_of_birth": date_of_birth,
            "birth_place": birth_place,
            "birth_place_english": birth_place_english,
            "school": school_dict,
            "book_list": book_list,
            "about_author": about_author,
            "language": language,
            "category": category,
        }

        final_author.append(complete_author_record)
        with open('formatted_authors.json', 'w', encoding='utf-8-sig') as formatted_author:
		    
            json.dump(final_author,formatted_author, indent=4 ,ensure_ascii=False)
            #formatted_author.write(json.dumps(final_author))

formatJson()
        