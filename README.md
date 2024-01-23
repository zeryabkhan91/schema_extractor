# schema_extractor
A Python-based REST API for database schema extraction using Django and PostgreSQL.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Usage

### Storing Credentials

Use this endpoint to provide database credentials.*

**REST Endpoint:**
```http
POST http://localhost:8000/api/v1/credentials/
```

### Fetching Schema of Tables

**REST Endpoint**
This endpoint retrieves database schema information.

```http
GET http://localhost:8000/api/v1/schema/
```
 
### Get Detail of a Table

**Search Table Endpoint**
This endpoint searches for a specific table within the database.

```http
GET http://localhost:8000/api/v1/search/your-table-name/
```


### Docker Deployment
The services can be containerized using Docker. Use the following commands for local deployment:

- Build and start the containers:

```Code
docker-compose up -d --build
```

- To Stop the containers:

```Code
docker-compose down
```

- To View logs:

```Code
docker-compose logs
```

## Video Explanation

Watch a detailed explanation of the project, including the code walkthrough, system diagram, data model, and challenges/solutions in the following video:

[Link to Video Explanation](https://www.loom.com/share/4c2cd7faa4764e2890e299a814090b04?sid=2c46c06c-260c-462b-83ec-4aaae236fbcd)