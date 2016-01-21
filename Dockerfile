FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install flask redis
#RUN pip install -r requirements.txt
CMD python app.py
