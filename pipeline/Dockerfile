#FROM python:3.13-slim

#ENV PYTHONDONTWRITEBYTECODE=1 \
    #PYTHONUNBUFFERED=1 \
   # UV_LINK_MODE=copy

#WORKDIR /app

#RUN pip install --no-cache-dir uv

#COPY pyproject.toml README.md ./
#RUN uv sync --no-dev

#COPY . .

#ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]
#CMD ["--pg-user=alex", "--pg-pass=root", "--pg-host=postgres", "--pg-port=5432", "--pg-db=db1", "--target-table=yellow_taxi_data", "--year=2021", "--month=1", "--chunksize=100000"]


# Start with slim Python 3.13 image
FROM python:3.13.10-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./
# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Copy application code
COPY ingest_data.py ./

# Set entry point
ENTRYPOINT ["python", "ingest_data.py"]

# Commands to manage the PostgreSQL container
 docker run -d \
   --name ny_taxi_db \
   -e POSTGRES_USER="alex" \
   -e POSTGRES_PASSWORD="root" \
   -e POSTGRES_DB="db1" \
   -v ny_taxi_postgres_data:/var/lib/postgresql \
   -p 5432:5432 \
   --network=pg-network \
   postgres:18
#   docker-compose up -d run this first
#   python ingest_data.py followed
#   # to start docker start ny_taxi_db
#   # to stop docker stop ny_taxi_db
#  uv run pgcli -h localhost -p 5432 -U alex -d db1 run this first

docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --pg-user=alex \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=db1 \
    --target-table=yellow_taxi_trips