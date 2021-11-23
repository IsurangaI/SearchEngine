import requests,time
import json,re,os
from urllib.error import HTTPError
from googletrans import Translator
translator = Translator()


def translate_field(field_array,field_all_dict):
	if field_array:
		translated_field_array = []
		if type(field_array) == list:
			for eng_data in field_array:
				eng_data = eng_data.strip()
				if eng_data in field_all_dict:
					sin_data = field_all_dict[eng_data]
				else:
					try:
						sin_tran_data = translator.translate(eng_data, src='en', dest='si')
						sin_data = sin_tran_data.text
					except HTTPError:
						time.sleep(5)
					try:
						sin_tran_data = translator.translate(eng_data, src='en', dest='si')
						sin_data = sin_tran_data.text
					except HTTPError:
						print("error")
					field_all_dict.update({eng_data: sin_data})
				translated_field_array.append(sin_data)
			return translated_field_array, field_all_dict
		else:
			eng_data = field_array.strip()
			if eng_data in field_all_dict:
				sin_data = field_all_dict[eng_data]
			else:
				try:
					sin_tran_data = translator.translate(eng_data, src='en', dest='si')
					sin_data = sin_tran_data.text
				except HTTPError:
					time.sleep(5)
				try:
					sin_tran_data = translator.translate(eng_data, src='en', dest='si')
					sin_data = sin_tran_data.text
				except HTTPError:
					print("error") 
				field_all_dict.update({eng_data: sin_data})
			translated_field_array.append(sin_data)
			return translated_field_array[0], field_all_dict
	else:
		return None,field_all_dict



def translate():
	genres_dict = {}
	artists_dict = {}
	lyricis_dict = {}
	music_dict = {}

	with open('translated_songs.json', 'r',encoding='utf8') as s_file:
		final_songs = json.loads(s_file.read())

    
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	song_file = os.path.join(THIS_FOLDER, 'scraped_songs.json')

	with open(song_file, 'r', encoding='utf8') as f:
		scraped_songs = json.loads(f.read())
    # scraped_songs  = open(song_file,encoding='utf8')

    
	i=0
	for scraped_song in scraped_songs:
		i=i+1
		if(i%10==0):
			time.sleep(15)
        
        
		complete_song = {}
		title = scraped_song["title"]
		artist = scraped_song["artist"]
		genre = scraped_song["genre"]
		lyricist = scraped_song["lyrics_by"]
		music = scraped_song["music_by"]
		song_lyrics = scraped_song["song_lyrics"]
		views = scraped_song['visits']
        
        
		translated_artist, artists_dict = translate_field(artist, artists_dict)
		time.sleep(2)
		
		translated_lyrics, lyricis_dict = translate_field(lyricist, lyricis_dict)
		time.sleep(2)
		
		translated_music, music_dict = translate_field(music, music_dict)
		time.sleep(2)

		translated_genre, genres_dict = translate_field(genre, genres_dict)
		time.sleep(2)
        
        
		complete_song = {
            "title": title,
            "song_lyrics": song_lyrics,
            "views": views,
            "english_artist": artist,
            "english_lyrics": lyricist,
            "english_music": music,
            "english_genre": genre,
            "sinhala_artist": translated_artist,
            "sinhala_lyrics": translated_lyrics,
            "sinhala_music": translated_music,
            "sinhala_genre": translated_genre,
        }
        

		final_songs.append(complete_song)
		with open('translated_songs.json', 'w', encoding='utf8') as tra_songs:
			json.dump(final_songs,tra_songs, indent=4 ,ensure_ascii=False)
			#tra_songs.write(json.dumps(final_songs))
		
        
		print(music_dict)

if __name__ == "__main__":
	translate()
