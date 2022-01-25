# flask-test

### How to start the app?
## Via docker-compose
1. Run ```docker-compose build```
2. Run ```docker-compose up```

This starts the flask web app with gunicorn, as a docker container with exposed port 8000.

## Via local shell script
1. Run ```bash runserver.sh```

This starts the flask web app with gunicorn locally with port 8000 exposed.


Endpoints:
http://127.0.0.1:8000/api/v1/show_file

Additional GET parameters can be added to the url:
http://127.0.0.1:8000/api/v1/show_file?file=file4.txt
http://127.0.0.1:8000/api/v1/show_file?file=file4.txt&start_ln=1&end_ln=3

