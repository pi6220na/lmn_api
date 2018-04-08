Live Music Notes Opinions Pictures (lmnop)

MCTC ITEC Capstone Project 5 – Eight member team

lmn\_api

**webscrapper.py**  - Jeremy

This program is currently setup to do the following:

- Get musical show events from Eventful.com for the Minneapolis area
- Scrub the data from the web pages (including using regex)
- Generate JSON format files for these database tables:
  - Shows
  - Artists
  - Venues
  - Notes
  - Users
- Currently setup to get 100 show events

While work is continuing on building the API the JSON files can be used to automatically load the Postgres database as it is currently defined in the base lmn project.

- --Copy the JSON files into the fixtures subdirectory
- --At a command prompt (same directory as you would run the project), run this command:

**python manage.py testserver user artist venue show note**

- --This loads the JSON data into their respective tables in a database named &quot; **test\_lmnop**&quot; and runs the Django server. When you stop the server the data is not unloaded. So, you could just run the server using: python manage.py runserver

- --The next time the &quot;testserver&quot; command is run, it will prompt you asking if you want to delete the database – type in &#39;yes&#39;

**I strongly suggest loading the JSON files and running the server**. It will give you a really good idea of how the program is structured and what the various links within the program do.



Information on the data:

- 100 shows
- 94 artists (6 artists have 2 shows each)
- 32 Venues
- 6 users have been predefined:
  - users: kevin, jane     password: asdfasdf
  - users: bob bill           password: zxcvzxcv
  - users: mary betty     password: qwerqwer
- Around 125 notes.  These have been generated with random ipsum losem text. Random note dates are all in the month of April (this means a lot of shows have notes even though they haven&#39;t taken place yet, our users are time travelers). All of the odd numbered (primary key) shows will have between 1 and 4 notes (determined randomly), the even numbered shows have none. Show ID order based on first show off the web site pk = 1, second show pk = 2
- Almost all the quantitative and random qualities can easily be adjusted to regenerate a different set of files. Please ask me if you need a different set of JSON files (or re-run webscrapper.py yourself).
- Gathering data from a different web site will take a lot more work if absolutely required…