## Digital-Hive

For Docker Run:

# Build the images
docker compose --env-file .env.docker build

# Run migrations inside Docker
docker compose --env-file .env.docker run backend python manage.py migrate

# Create superuser inside Docker
docker compose --env-file .env.docker run backend python manage.py createsuperuser

# Start everything
docker compose --env-file .env.docker up