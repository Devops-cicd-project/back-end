FROM python:3.11-slim
# put COPY commands as late as possible

# prevents python from writing .pyc files into the disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents python from buffering stdout and std errors
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www/api

# install postgres psycopg dependencies
RUN apt update && apt install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    && apt-get purge -y \
    --auto-remove -o \
    APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Install Dependencies
RUN pip install --upgrade pip pipenv flake8
COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile
# --deploy faster and for production skips Pipfile and only installs .lock

COPY . .

# creat tabel in postgres


# lint
RUN flake8 --ignore=E501,F401 ./api/api/settings.py

# copy entrypoint.sh
# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /var/www/api/entrypoint.sh
# RUN chmod +x /var/www/api/entrypoint.sh
# ENTRYPOINT ["/var/www/api/entrypoint.sh"]

# Set the default command
# CMD ["python", "manage.py", "runserver"]
