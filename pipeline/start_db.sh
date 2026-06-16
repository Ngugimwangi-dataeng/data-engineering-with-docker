docker run -d \
  --name ny_taxi_db \
  -e POSTGRES_USER="alex" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="db1" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
  # to run on trminal type (bash start_db.sh)