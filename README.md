# The Pursuit OTH
An OTH (Online Treasure Hunt) app based on Python/Django. It is forked from [this](https://github.com/code-haven/Django-treasurehunt-demo) project. It was used to host The Pursuit 2016 organised by [PESITSouth ACM](http://pesitsouthacm.org), that saw participation from over 400 users from 20+ countries.

## Features
- Any number of questions can be added using a web-based GUI (Django admin), no coding required.
- Uses randomly generated image names so users can't see other level images by guessing the URL.
- User can only view the current level.
- Supports three types of questions/hints - text, image and hidden text (HTML comment).
- In-built support for login, registration and session management.
- A leaderboard that takes both the level, and completed time into account.
- Winners are separately indicated in the leaderboard.
- A start page with rules, and a finish page for the users who complete the OTH.

## Instructions
1. Set up a virtual environment and switch to it. (Optional, but recommended.) Following command can be used with `virtualenv` and `virtualenvwrapper` installed.<br>
  ```
  $ mkvirtualenv oth
  ```
2. Install development or production dependencies, based on the environment.<br>
  ```
  $ pip install -r [ requirements-dev.txt | requirements-prod.txt]
  ```
3. Create super-user for Django admin site.<br>
  ```
  $ python manage.py createsuperuser
  ```
4. Run the app locally<br>
  ```
  $ python manage.py runserver
  ```
5. Open `localhost:8000/admin` and login using previously generated credentials to add questions.

### Credits
Thanks to [code-haven](https://github.com/code-haven) for the original project.

### Author
Built by [Amjad Ali](https://github.com/amjd) for [inGenius 2016](https://github.com/ingeniushack) on behalf of [PESITSouth ACM](https://github.com/pesitsouthacm).
