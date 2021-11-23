import scrapy
import json
import re

class SongScraper(scrapy.Spider):
    name = 'song_scraper'
    a =[]
    start_urls = ['https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords']

    for i in range (2,23,1):
        start_urls.append('https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page='+str(i))

    def parse(self, response):
       # //*[@id="pt-cv-view-9c94ff8o8i"]/div[4]
       #/html/body/div[1]/div[1]/div/main/article/div/div[3]/div[1]/div[4]/div[1]/div/h4/a
       
        for quote in response.xpath('//div[@class="pt-cv-ifield"]'):
            #  //*[@id="pt-cv-view-9c94ff8o8i"]/div[4]/div[1]/div/h4/a
            next_page = quote.xpath('h4/a/@href').get()
            #print (next_page)
            yield response.follow(next_page, self.parse_author)


        
    def parse_author(self, response):

        title = response.xpath('//*[@id="genesis-content"]/article/header/h1/text()').get()
        artist = response.xpath('//*[@id="genesis-content"]/article/div[3]/div[1]/div[2]/div/div/ul/li[1]/span/a/text()').get()
        lyrics = response.xpath('//*[@id="genesis-content"]/article/div[3]/div[1]/div[3]/div/ul/li[1]/span/a/text()').get()
        music = response.xpath('//*[@id="genesis-content"]/article/div[3]/div[1]/div[3]/div/ul/li[2]/span/a/text()').get()
        genre = response.xpath('//*[@id="genesis-content"]/article/div[3]/div[1]/div[2]/div/div/ul/li[2]/span/a/text()').getall()
        s_lyrics = " ".join(response.xpath('//div[@class="su-column-inner su-u-clearfix su-u-trim"]/pre/text()').getall() or response.xpath('//*[@id="genesis-content"]/article/div[3]/pre/text()').getall())
        visits = response.xpath('//div[@class="tptn_counter"]/text()').get()
        str_visits = re.findall("\d+", visits)
        if (len(str_visits)>1):
            int_visits = str_visits[0] + str_visits[1]
        else:
            int_visits = str_visits[0]

        space_set = set([' '])
        processed = ''
        regex = r"([A-z])+|[0-9]|\||-|—|∆|([.!?\\\/\(\)\+#&])+"
        lyric_lines = s_lyrics.split('\n')
        for line in lyric_lines:
            new1 = re.sub(regex, '', line)
            new = re.sub('\new1+', '', new1)
            chars = set(new)
            if not ((chars == space_set) or (len(chars) is 0)):
                processed += new + '\n'

        song_lyrics = processed.strip()
        
        
        if (not(artist is None) and not(lyrics is None) and not(music is None)>0 and len(song_lyrics)>0 and len(title)>0 and len(genre)>0):

            obj = {
                'title' : title,
                'artist' : artist,
                'lyrics_by' : lyrics,
                'music_by' : music,
                'genre' : genre,
                'song_lyrics' : song_lyrics,
                'visits' : int(int_visits)

            }
            self.a.append(obj)
    


    def closed(self,reason):
        with open ("scraped_songs.json",'w',encoding="utf8") as outfile:
            json.dump(self.a,outfile, indent=4 ,ensure_ascii=False)