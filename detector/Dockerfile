# Base Image
FROM python:3.11.5
LABEL maintainer="Shilpa"

WORKDIR /usr/app
ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./
CMD ["python3", "app.py"]