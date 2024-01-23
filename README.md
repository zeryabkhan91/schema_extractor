# schema_extractor
A Python-based REST API for database schema extraction using Django and PostgreSQL.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Usage

### Credentials Endpoint

Use this endpoint to provide database credentials.

```code
curl -X POST -H "Content-Type: application/json" -d '{"host": "your-host", "username": "your-username", "password": "your-password", "database": "your-database"}' http://localhost:8000/api/v1/credentials/
```

Schema Endpoint
This endpoint retrieves database schema information.

```Code
curl http://localhost:8000/api/v1/schema/
```

Search Table Endpoint
This endpoint searches for a specific table within the database.

```Code
curl http://localhost:8000/api/v1/search/your-table-name/
```

### Docker Deployment
The services can be containerized using Docker. Use the following commands for local deployment:

Build and start the containers:

```Code
docker-compose up -d --build
```

Stop the containers:

```Code
docker-compose down
```

View logs:

```Code
docker-compose logs
```