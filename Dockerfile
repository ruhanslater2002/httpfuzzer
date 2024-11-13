FROM python:latest
LABEL authors="ruhan"
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY /src .
ENTRYPOINT ["python", "main.py"]