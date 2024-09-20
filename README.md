# Django Project Dockerized

This project runs a Django application using Docker.

## Prerequisites

- Python 3.10.x
- Docker
- Docker Compose

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/<replace with your git repo>.git
   cd <replace with your git repo>
   ```

2. Add the csv files to the `dataset` folder

3. Build the Docker containers:

    ```bash
    docker-compose build
    ``````

4. Run the containers:

    ```bash
    docker-compose up
    ```

5. Run migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

6. Create a superuser (optional):

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

7. Insert the data into the database:

    ```bash
    docker-compose exec web python manage.py load_data dataset/<filename.csv> --limit <optional>
    ```

8. Access the app at `http://localhost:8000`.

9. Access the admin at `http://localhost:8000/admin`.

10. Press `Ctrl + C` to stop the server.