FROM mcr.microsoft.com/playwright/python:v1.55.0

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DOCKER_RUN=1

CMD ["pytest", "-m", "T1"]
