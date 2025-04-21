FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
# Match the port used in app.py
EXPOSE 80
# CMD ["flask", "run"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
