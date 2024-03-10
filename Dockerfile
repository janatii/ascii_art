FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip libgl1-mesa-glx libglib2.0-0


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt .

RUN . $VIRTUAL_ENV/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8001", "app:app"]
