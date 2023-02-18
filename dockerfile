FROM python:3.7.10
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py

