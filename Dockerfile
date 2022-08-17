FROM python:3.10

# The base image sets LANG=C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONHASHSEED 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

COPY ./pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install

COPY ./src /src 

WORKDIR /src

CMD python manage.py runserver --noreload 0.0.0.0:8000
