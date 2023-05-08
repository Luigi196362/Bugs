FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /Bugs
WORKDIR /Bugs
COPY requirements.txt /Bugs/
RUN pip install -r requirements.txt
COPY . /Bugs/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
