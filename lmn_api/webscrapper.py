# pip install requests
# pip install b24
# pip install re
# pip install json

import calendar, random
import requests, re, json
from time import sleep
from bs4 import BeautifulSoup
from loremipsum import get_sentences
from datetime import datetime
from random import randint


artist_list = []
show_list = []
venue_list = []
note_list = []
user_list = []

artist_json = []
venue_json = []
show_json = []
note_json = []
user_json = []


def main():

    # makes call to Eventful.com to get pages of Minneapolis area musical events
    # note that getting data from the web and scrapping the pages is extremely slow
    # getting and scrapping 100 shows takes several minutes
    #raw_data_list = getMPLS()

    # test list used to save time during development - built from live data
    # comment out following line and uncomment above function call to run web scrapping for live data
    raw_data_list = getTestData()

    # for line in raw_data_list:
    #     print(line)

    # formats the raw line of data and prints in formatted columns
    if len(raw_data_list) > 0:
        scrubData(raw_data_list)


    # for line in artist_list:
    #     print(line)
    # for line in show_list:
    #     print(line)
    # for line in venue_list:
    #     print(line)

    buildJSON()

    writeOutJSON()


def buildNotes():

    sentences_list = []
    sentences = get_sentences(1250, start_with_lorem=True)

    for sentence in sentences:
        line1 = re.sub("b'", '', sentence)
        line2 = re.sub("'", '', line1)
        sentences_list.append(line2)

    recNum = 0
    for num in range(1,100,2):
        for innerNum in range(randint(1,4)):
            recNum += 1
            rand = randint(1, 6)
            pop1 = sentences_list.pop()
            myDate = randomdate(2018,4)
            #print(myDate)
            nText = sentences_list.pop() + sentences_list.pop() + sentences_list.pop() + sentences_list.pop()
            note_json.append({"model": "lmn.note", "pk": recNum, "fields": {"show": num, "user": rand, "title": pop1, "text": nText, "posted_date": str(myDate)}})

    # for item in note_json:
    #     print(item)


# https://stackoverflow.com/questions/45833559/generate-random-date-in-a-particular-month-and-year
def randomdate(year, month):
    dates = calendar.Calendar().itermonthdates(year, month)
    return random.choice([date for date in dates if date.month == month])


def buildUsers():

    user_json.append({"model": "auth.user", "pk": 1, "fields": {"username": "kevin", "first_name": "Kevin", "last_name": "Kevin-last", "email": "123@aaa.com", "password": "pbkdf2_sha256$100000$FmE0uvtW02K6$lRqwDwm/E0M/0Fgb9v09ZyH4p5simN6vBLy+KyzqDOU="}})
    user_json.append({"model": "auth.user", "pk": 2, "fields": {"username": "bob", "first_name": "Bob", "last_name": "Bob-last", "email": "456@aaa.com", "password": "pbkdf2_sha256$100000$3m7XTcsWfgZE$8FRAIG1EL8d+QxuKKNWeKo4F5aEpRqtxnSeyJbeJwe0="}})
    user_json.append({"model": "auth.user", "pk": 3, "fields": {"username": "mary", "first_name": "Mary", "last_name": "Mary-last", "email": "567@aaa.com", "password": "pbkdf2_sha256$100000$YsLjt3vB2eme$Qj8+si71Zgh3eM0TBpskpbD2OMVEmg1gtAzczYKfQLY="}})
    user_json.append({"model": "auth.user", "pk": 4, "fields": {"username": "jane", "first_name": "Jane", "last_name": "Jane-last", "email": "123@aaa.com", "password": "pbkdf2_sha256$100000$FmE0uvtW02K6$lRqwDwm/E0M/0Fgb9v09ZyH4p5simN6vBLy+KyzqDOU="}})
    user_json.append({"model": "auth.user", "pk": 5, "fields": {"username": "bill", "first_name": "Bill", "last_name": "Bill-last", "email": "wer456@aaa.com", "password": "pbkdf2_sha256$100000$3m7XTcsWfgZE$8FRAIG1EL8d+QxuKKNWeKo4F5aEpRqtxnSeyJbeJwe0="}})
    user_json.append({"model": "auth.user", "pk": 6, "fields": {"username": "betty", "first_name": "Betty", "last_name": "Betty-last", "email": "wer567@aaa.com", "password": "pbkdf2_sha256$100000$YsLjt3vB2eme$Qj8+si71Zgh3eM0TBpskpbD2OMVEmg1gtAzczYKfQLY="}})

    # for line in user_json:
    #     print(line)


    # pbkdf2_sha256$100000$FmE0uvtW02K6$lRqwDwm/E0M/0Fgb9v09ZyH4p5simN6vBLy+KyzqDOU=
    # password: asdfasdf   users: kevin jane

    # pbkdf2_sha256$100000$3m7XTcsWfgZE$8FRAIG1EL8d+QxuKKNWeKo4F5aEpRqtxnSeyJbeJwe0=
    # password: zxcvzxcv   users: bob bill

    # pbkdf2_sha256$100000$YsLjt3vB2eme$Qj8+si71Zgh3eM0TBpskpbD2OMVEmg1gtAzczYKfQLY=
    # password: qwerqwer   users: mary betty


def writeOutJSON():


    try:

        with open('fixtures/artist.json', 'w') as fp:
            # prettify the json using json.dumps
            json_string = json.dumps(artist_json, indent=4)
            fp.write(json_string)
        with open('fixtures/venue.json', 'w') as fp:
            json_string = json.dumps(venue_json, indent=4)
            fp.write(json_string)
        with open('fixtures/show.json', 'w') as fp:
            json_string = json.dumps(show_json, indent=4)
            fp.write(json_string)
        with open('fixtures/user.json', 'w') as fp:
            json_string = json.dumps(user_json, indent=4)
            fp.write(json_string)
        with open('fixtures/note.json', 'w') as fp:
            json_string = json.dumps(note_json, indent=4)
            fp.write(json_string)


    except Exception as e:
        print("file error writing out JSON file: % e" % e)



def buildJSON():

    num = 0
    afirst_time = True
    for item in artist_list:
        if afirst_time:
            num += 1
            artist_json.append({"model":"lmn.artist", "pk":num, "fields": {"name":item}})
            afirst_time = False
        else:
            afirst_time = False
            for aitem in artist_json:
                if aitem["fields"]["name"] in item:
                    #print("In build artist table duplicate = " + aitem["fields"]["name"])
                    found = True
                    break
                else:
                    found = False
            if not found:
                num += 1
                artist_json.append({"model": "lmn.artist", "pk": num, "fields": {"name": item}})

    num = 0
    first_time = True
    for item in venue_list:

        if first_time:
            num = 1
            venue_json.append(
                {"model": "lmn.venue", "pk": num, "fields": {"name": item[0], "city": item[1], "state": item[2]}})
            first_time = False
        else:
            found = False
            #print('value searching for: ' + item[0] + '***')
            for vitem in venue_json:
                #print('value in venue dictionary: ' + vitem['fields']['name'] + '***')
                if vitem['fields']['name'] in item[0]:
                    found = True
                    #print("******************** found *********************")
                    break
                else:
                    found = False

            if not found:
                num += 1
                venue_json.append({"model":"lmn.venue", "pk":num, "fields": {"name": item[0], "city": item[1], "state": item[2]}})

    num = 0
    for item in show_list:

        num += 1
        venue_key = getVenue(venue_list[num-1][0])
        artist_key = getArtist(artist_list[num-1])
        #print("returned artist key number: " + str(artist_key))
        datetime_object = datetime.strptime(item, '%b %d, %Y')

        if venue_key > 0 and artist_key > 0:
            show_json.append({"model":"lmn.show", "pk":num, "fields": {"show_date": str(datetime_object), "artist": artist_key, "venue": venue_key }})
        else:
            print("error: venue or artist for show was not found")


    buildUsers()

    buildNotes()



def getArtist(artist):

    num = 0
    for aitem in artist_json:

        num += 1
        if aitem['fields']['name'] in artist:
            return num

    return 0

def getVenue(venue):

    num = 0
    for vitem in venue_json:
        num += 1
        #print('value in venue dictionary: ' + vitem['fields']['name'] + '***')
        if vitem['fields']['name'] in venue:

            #print("******************** found venue key *********************")
            return num

    return 0  # error, venue was not found



def getMPLS():
    # http://minneapolis.eventful.com/events/categories/music#!page_number=1&category=music
    MAXPAGES = 10
    raw_data_list = []

    print("Getting web data from %s pages total, please be patient." % MAXPAGES)
    for page in range(1, MAXPAGES+1):
        # result = requests.get("http://minneapolis.eventful.com/events/categories/music")
        httpString = "http://minneapolis.eventful.com/events/categories/music?page_number=" + str(
            page) + "&category=music"
        print(httpString)
        try:
            result = requests.get(httpString)
            sleep(1)  # pause Python to allow return from call, not sure if this is needed
            print(result.status_code)
        except Exception as e:
            print('An exception happened while get web data: %s' % e)

        if result.status_code == 200:
            c = result.content                      # page returned
            soup = BeautifulSoup(c, "html.parser")  # parse the page into beautiful soup format
            samples2 = soup.find_all("a", 'tn-frame')   # extract all a tags with class contains 'tn-frame'
            #print(samples2)

            for item in samples2:
                myURL = item.get('href')
                myURL = "http:" + myURL
                result = requests.get(myURL)        # call Eventful.com for each individual event's data
                c = result.content
                minisoup = BeautifulSoup(c, "html.parser")
                samples3 = minisoup.find("meta", {"name": "description"})['content']  # extract string with required
                                                                                      # event information
                raw_data_list.append(samples3)
        else:
            print("There was a problem getting web data. Web call return code = %s" % result.status_code)
            print("Web address: %s " % httpString)

    return raw_data_list


def scrubData(raw_data_list):

    # print()
    # print("Events scrapped from Eventful.com: ")
    # print()
    line_count = 0
    for line in raw_data_list:
        # print("'" + line + "',") ### builds raw line scrapped from web for development test data
        # example line='Counting Crows &amp; Live - Band on Sep 16, 2018 in Prior Lake, MN(Minneapolis / Saint Paul metro area) at Mystic Lake Casino Hotel.'

        # regex to remove 'amp;' from some artist names, is html for &
        line1 = re.sub('amp;', '', line)

        # regex removes period at the end of line (immediately following venue name)
        line2 = re.sub('\.', '', line1)

        # ['Taylor Swift', ' on ', 'Sep 1, 2018 in Minneapolis, MN at US Bank Stadium']
        myGroup = re.split(r'( on +)', line2)
        # myGroup[0]=artist

        # ['Sep 1, 2018', ' in ', 'Minneapolis, MN', ' at ', 'US Bank Stadium']
        date_cityst_venue = re.split(r'( in +| at +)', myGroup[2])
        # date_cityst_venue[0]=date
        # date_cityst_venue[2]=city, state
        # date_cityst_venue[4]=venue

        # regex splits apart city, state field
        myCitySt = re.split(r'(, )', date_cityst_venue[2])
        # myCitySt[0]=city

        # regex splits apart state abbrev. from "(Minneapolis / Saint Paul metro area)" literal
        myState = re.split(r'(\(.*\))', myCitySt[2])
        # myState[0]=state abbrev.

        #print('%80s %15s %15s %4s %40s' % (myGroup[0], date_cityst_venue[0], myCitySt[0], myState[0], date_cityst_venue[4][:30])
        #      + ('  field sizes: %d %d %d %d %d' % (len(myGroup[0]), len(date_cityst_venue[0]), len(myCitySt[0]), len(myState[0]), len(date_cityst_venue[4][:40]))))

        line_count += 1

        artist_list.append(myGroup[0])

        show_list.append(date_cityst_venue[0])

        venue_list.append((date_cityst_venue[4][:40],myCitySt[0],myState[0]))

    # print()
    # print("%s events found for Minneapolis area." % line_count)


def getTestData():
    # live data as of 04/06/2018
    raw_data_list = [
        'Bon Jovi on Apr 28, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Maroon 5: Red Pill Blues Tour 2018 on Sep 18, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Rod Stewart &amp; Cyndi Lauper on Aug 15, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Journey &amp; Def Leppard on Jul 27, 2018 in Minneapolis, MN at Target Field.',
        'Bruno Mars &amp; Cardi B on Sep 11, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Justin Timberlake on Sep 28, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Keyshia Cole and Tank on Oct 27, 2018 in Minneapolis, MN at Orpheum Theatre.',
        'Vans Warped Tour 2018 on Jul 22, 2018 in Shakopee, MN(Minneapolis / Saint Paul metro area) at Canterbury Park.',
        'Metallica on Sep 4, 2018 in Minneapolis, MN at Target Center.',
        'Sugarland on Aug 24, 2018 in Saint Paul, MN at Minnesota State Fair.',
        'Jason Mraz on Aug 28, 2018 in Saint Paul, MN at Minnesota State Fair Grandstand.',
        'Counting Crows &amp; Live - Band on Sep 16, 2018 in Prior Lake, MN(Minneapolis / Saint Paul metro area) at Mystic Lake Casino Hotel.',
        'Tech N9ne on Apr 21, 2018 in Minneapolis, MN at The Armory.',
        'Kenny Chesney: Trip Around the Sun Tour on May 5, 2018 in Minneapolis, MN at U.S. Bank Stadium.',
        'MercyMe &amp; Tenth Avenue North on Apr 13, 2018 in Minneapolis, MN at Target Center.',
        'Joan Baez on Oct 6, 2018 in Minneapolis, MN at State Theatre.',
        'The Pretenders on Jul 16, 2018 in Minneapolis, MN at State Theatre.',
        'Luke Bryan, Sam Hunt &amp; Jon Pardi on Jul 21, 2018 in Minneapolis, MN at Target Field.',
        'Zac Brown Band &amp; OneRepublic on Aug 10, 2018 in Minneapolis, MN at Target Field.',
        'Bruno Mars &amp; Cardi B on Sep 12, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Foo Fighters on Oct 18, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Justin Timberlake - The Man Of The Woods Tour on Sep 29, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Paramore &amp; Foster The People on Jul 5, 2018 in Minneapolis, MN at The Armory.',
        'Taylor Swift on Sep 1, 2018 in Minneapolis, MN at U.S. Bank Stadium.',
        'An Acoustic Evening w/ Andrew McMahon in the Wilderness &amp; Friends on Apr 13, 2018 in Minneapolis, MN at Varsity Theater.',
        'Robert Earl Keen on Apr 12, 2018 in Minneapolis, MN at Varsity Theater.',
        'CALEXICO on Apr 23, 2018 in Minneapolis, MN at Fine Line Music Cafe. with special guest RYLEY WALKER18+ SHOW – please review our minor policy under F.A....',
        'Franz Ferdinand on Apr 27, 2018 in Minneapolis, MN at First Avenue.',
        'Tim McGraw &amp; Faith Hill on Jul 7, 2018 in Minneapolis, MN at Target Center.',
        'Panic! At The Disco, Hayley Kiyoko &amp; Arizona on Jul 11, 2018 in Minneapolis, MN at Target Center.',
        'Leon Bridges on Sep 20, 2018 in Saint Paul, MN at Palace Theatre St. Paul.',
        'Ringo Starr And His All Starr Band on Sep 23, 2018 in Saint Paul, MN at Ordway Center for the Performing Arts.',
        'Elton John on Feb 22, 2019 in Minneapolis, MN at Target Center.',
        'Alice Cooper on Aug 30, 2018 in Saint Paul, MN at Ordway Center for the Performing Arts.',
        'Needtobreathe, Johnnyswim &amp; Forest Blakk on Sep 7, 2018 in Minneapolis, MN at The Armory.',
        'O.A.R. &amp; Matt Nathanson on Sep 7, 2018 in Prior Lake, MN(Minneapolis / Saint Paul metro area) at Mystic Lake Casino Hotel.',
        'Josh Groban &amp; Idina Menzel on Nov 2, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Elton John on Feb 21, 2019 in Minneapolis, MN at Target Center.',
        '3 Doors Down &amp; Collective Soul on Jul 26, 2018 in Minneapolis, MN at The Armory.',
        'Rise Against (18+ Event) on Sep 6, 2018 in Minneapolis, MN at The Armory.',
        'Lyle Lovett and His Large Band on Aug 29, 2018 in Minneapolis, MN at State Theatre.',
        'On The Run II: Beyonce &amp; Jay-Z on Aug 8, 2018 in Minneapolis, MN at US Bank Stadium.',
        'Jorja Smith on May 1, 2018 in Minneapolis, MN at Fine Line Music Cafe.',
        'Camila Cabello on Apr 20, 2018 in Minneapolis, MN at State Theatre.',
        'Marco Antonio Solis: Y La Historia Continua on Apr 21, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Voices for Vision - Featuring Kat Perkins &amp; Blind Joe on Apr 21, 2018 in Minneapolis, MN at State Theatre.',
        'AJR on Apr 8, 2018 in Minneapolis, MN at Music Hall Minneapolis.',
        'Brian Fallon on Apr 17, 2018 in Minneapolis, MN at Music Hall Minneapolis.',
        'Ty Segall Tickets (18+ Event) on Apr 7, 2018 in Minneapolis, MN at 7th Street Entry.',
        'Jethro Tull on Aug 31, 2018 in Minneapolis, MN at State Theatre.',
        'TAUK on Apr 12, 2018 in Minneapolis, MN at Fine Line Music Cafe.',
        'Albert Hammond Jr Tickets (21+ Event) on Apr 7, 2018 in Saint Paul, MN at Turf Club.',
        'Echosmith on Apr 13, 2018 in Minneapolis, MN at First Avenue.',
        'Dessa on Apr 6, 2018 in Minneapolis, MN at First Avenue.',
        'Charlie Puth: The Voicenotes Tour on Aug 8, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Sam Smith on Aug 14, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Margo Price on Apr 14, 2018 in Minneapolis, MN at First Avenue.',
        'The Decemberists on Apr 7, 2018 in Saint Paul, MN at Palace Theatre St. Paul.',
        'Jack White on Aug 6, 2018 in Minneapolis, MN at The Armory.',
        'James Bay on Oct 2, 2018 in Minneapolis, MN at State Theatre.',
        'Kate Nash on Apr 19, 2018 in Minneapolis, MN at First Avenue.',
        'Smashing Pumpkins on Aug 19, 2018 in Saint Paul, MN at Xcel Energy Center.',
        'Erasure - World Be Gone Tour on Jul 29, 2018 in Minneapolis, MN at State Theatre.',
        'Wyclef Jean on Apr 13, 2018 in Minneapolis, MN at The Pourhouse.',
        'U Wanna Dance *Swing*Blues*Cajun*Zydeco* on Apr 6, 2018 in Minneapolis, MN at Minneapolis, Minnesota, United States. http://www.uwannadance.com is a FRE...',
        'Monster Jam on Apr 7, 2018 in Minneapolis, MN at US Bank Stadium. Tickets are now on sale for Monster Jam® at U.S. Bank Stadium in Minneapolis on Saturd...',
        'Thursday Morning Artist Series on Apr 12, 2018 in Minneapolis, MN at MacPhail Center for Music. Complimentary Coffee and Donuts at 10:00 am Tickets $15,...',
        'Cradle of Filth on Apr 14, 2018 in Minneapolis, MN at Music Hall Minneapolis.',
        'Irish Singer Máirín Uí Chéide in Concert on Apr 7, 2018 in Saint Paul, MN at Celtic Junction Arts Center. The Traditional Singers Club presents a concer...',
        'The sword on Apr 7, 2018 in Minneapolis, MN at Skyway Theatre. Skyway Theatre Presents The Sword Saturday, April 7th, 2018 @ Skyway Theatre :::: w/ supp...',
        'Ed Sheeran: 2018 North American Stadium Tour on Oct 20, 2018 in Minneapolis, MN at U.S. Bank Stadium.',
        'Taylor Swift on Aug 31, 2018 in Minneapolis, MN at U.S. Bank Stadium.',
        'The Belfast Cowboys on Apr 6, 2018 in Minneapolis, MN at The Hook and Ladder Theater & Lounge. This nine-piece band has been playing in and around Minne...',
        'The Eagles, Jimmy Buffett and The Coral Reefer Band on Jun 30, 2018 in Minneapolis, MN at Target Field.',
        'Tony Bennett with - special guest Antonia Bennett on May 10, 2018 in Minneapolis, MN at State Theatre.',
        'Todrick Hall on Apr 8, 2018 in Minneapolis, MN at Varsity Theater.',
        'Tonic Sol-fa and Shaun Johnson Big Band Experience on Apr 12, 2018 in Burnsville, MN(Minneapolis / Saint Paul metro area) at Burnsville Performing Arts ...',
        '5 Seconds of Summer on Apr 15, 2018 in Minneapolis, MN at Varsity Theater.',
        'BRIAN FALLON &amp; THE HOWLING WEATHER on Apr 17, 2018 in Minneapolis, MN at Music Hall Minneapolis.',
        'Coast Modern on Apr 9, 2018 in Saint Paul, MN at Amsterdam Bar and Hall.',
        'SiriusXM Presents Alt Nation&amp;#39;s Advanced Placement Tour on Apr 19, 2018 in Saint Paul, MN at Amsterdam Bar and Hall.',
        'Janine on Apr 11, 2018 in Saint Paul, MN at Amsterdam Bar and Hall.',
        'KC &amp; the Sunshine Band on Apr 12, 2018 in Prior Lake, MN(Minneapolis / Saint Paul metro area) at Mystic Lake Casino Hotel.',
        'Decemberists Tickets (18+ Event) on Apr 6, 2018 in Saint Paul, MN at Palace Theatre St. Paul.',
        'KC and the Sunshine Band Tickets (18+ Event) on Apr 12, 2018 in Prior Lake, MN(Minneapolis / Saint Paul metro area) at Mystic Lake Casino Hotel.',
        'Cradle of Filth Tickets (18+ Event) on Apr 14, 2018 in Minneapolis, MN at Music Hall Minneapolis.',
        'Matt and Kim Tickets (18+ Event) on Apr 16, 2018 in Minneapolis, MN at First Avenue.',
        'TAUK Tickets (18+ Event) on Apr 12, 2018 in Minneapolis, MN at First Avenue.',
        'Missio Tickets (21+ Event) on Apr 9, 2018 in Saint Paul, MN at Turf Club.',
        'Moose Blood on Apr 12, 2018 in Burnsville, MN(Minneapolis / Saint Paul metro area) at The Garage Burnsville. with Lydia, Souvenirs',
        'Progressive Nightclub on Apr 9, 2018 in Saint Paul, MN at Cinema Ballroom. Samba',
        "Chad Prather on Apr 27, 2018 in Minneapolis, MN at The Women's Club of Minneapolis.",
        'Dumbfoundead on Apr 29, 2018 in Minneapolis, MN at Loring Pasta Bar.',
        'Robyn Hitchcock on Apr 26, 2018 in Saint Paul, MN at Turf Club.',
        'Lord Huron on Apr 22, 2018 in Saint Paul, MN at Palace Theatre St. Paul.',
        'George Ezra on Apr 30, 2018 in Minneapolis, MN at First Avenue.',
        'Khruangbin on Apr 21, 2018 in Saint Paul, MN at Turf Club.',
        'X Ambassadors on May 1, 2018 in Saint Paul, MN at Myth.',
        'Trampled By Turtles on May 4, 2018 in Saint Paul, MN at Palace Theatre St. Paul.',
        'Unknown Mortal Orchestra Tickets (18+ Event) on May 4, 2018 in Minneapolis, MN at First Avenue.'
    ]
    return raw_data_list


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/11205386/python-beautifulsoup-get-an-attribute-value-based-on-the-name-attribute/11205758
