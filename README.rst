----------------
Polls
----------------
Polls is a django web app to conduct web_based polls. for each question , a Voter can choose from one of the many 
number of answers.

----------------
Quick start
---------------------------------------
1 Add "polls" to your project by configuring INSTALLED APPS setting like this:: 
INSTALLED APPS -[ 
                 -------------
				 'polls'
				]
				
2. include the polls URLconl in your project urls.py like this::

path('polls/' , include('polls,urls')),

3. Run "python manage.py  to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a poll.
(you will need the admin app enabled.)

5. visit http://127.0.0.1:8001/polls/ to participate in poll.