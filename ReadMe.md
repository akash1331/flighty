# Flighty - Book your Flight tickets online

This is a full stack web application where you can book your flight tickets.
As an administrator, flight ticket bookings can be monitored, flights can be added and as well as deleted.

TechStack used:
- Backend: Django - Python
- Frontend: HTML-CSS & Bootstrap
- Database: DbSQlite3

To run the project, run the following commands:
- create a virtual environment by "python -m venv (env name)"
- run the environment
- pip install -r requirements.txt 
- python manage.py makemigrations
- python manage.py migrate
- (optional) 'python manage.py createsuperuser' to signin as ADMIN
- python manage.py runserver

Login as user:
- view avaliable flights --> view its details and book the flight upto available limit.
- Search for a flight with date(as YYYY-MM-DD)
- view booked flights
- Note that the Admin portal dropdown doesnt work as its not needed for a user.. hence its disabled for user alone.

Login as Admin:
- view available flights --> view its details and book the flight.
- Remove a flight.
- Search a flight
- Add a new flight under 'Admin portal' dropdown menu.
- View all the bookings upto date
- As an admin, can create another admin.

Searching flights:
- To search by date ---> YYYY-MM-DD is the format to search

Note that logout for each type of user is given separately for their working in their specified dropdown menu.

Use the default django admin to view and understand more:
http://127.0.0.1:8000/admin/     ---> local
https://flighty-7iij.onrender.com/    ---> deployed on render