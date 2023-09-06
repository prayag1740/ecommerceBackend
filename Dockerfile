FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /ecommerce

WORKDIR /ecommerce

COPY . /ecommerce/

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]





