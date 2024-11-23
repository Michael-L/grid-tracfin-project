FROM python:3.13-alpine

WORKDIR /usr/src/app

COPY dockerfile/grid_tracfin_python/app/ .

RUN apk update && apk --update add postgresql-dev

# Should be execute before all other pip commands
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD [ "python", "-u", "dev_app.py" ]
