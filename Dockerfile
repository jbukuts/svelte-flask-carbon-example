# syntax=docker/dockerfile:1
FROM python:3.9.13

# Create app directory
WORKDIR /base

# setup env vars for container
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=5000
ENV ENV='production'

# Move required items into working directory
COPY /client/dist /base/client/dist
COPY /server/ /base/server
COPY requirements.txt /base/requirements.txt

# Instal python dependencies
RUN pip install -r requirements.txt

# Expose port and start server
EXPOSE 5000

CMD [ "python", "./server/server.py" ]
