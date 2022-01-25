FROM python:3

WORKDIR /usr/src/app/bin/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy required files from current directory into the container
COPY runserver.sh /usr/src/app/bin/
COPY conf /usr/src/app/bin/conf/
COPY config.py wsgi.py /usr/src/app/bin/
COPY fr /usr/src/app/bin/fr/

CMD [ "bash", "runserver.sh" ]