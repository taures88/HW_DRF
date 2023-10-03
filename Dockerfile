FROM python:3

WORKDIR /project_docker/studies

COPY ./requirements.txt .

RUN pip install -r reqrequirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]