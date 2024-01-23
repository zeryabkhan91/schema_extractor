# API Documentation

## 1. Provide Database Credentials

### Endpoint:
- `POST /api/v1/credentials/`

### Request Payload:
```json
{
  "host": "your_host",
  "username": "your_username",
  "password": "your_password",
  "database": "your_database_name"
}
```

### Response:
- Success (200 OK):

```json
{
  "message": "Credentials processed successfully"
}
```

- Error (400 Bad Request):

```json
{
  "error": "Required Database credentials not provided"
}
```


## 2. Retrieve Database Schema Information

### Endpoint:
- `GET /api/v1/schema/`

### Description:
 Retrieves the database schema information, including tables and their columns.

### Request:
 No request parameters are required.

### Response:
- Success (200 OK):

```json
{
  "database_name": "your_database_name",
  "tables": [
    {
      "name": "your_table_name",
      "schema": "your_table_schema",
      "columns": [
        {"name": "column1", "type": "your_data_type"},
        {"name": "column2", "type": "your_data_type"}
        // ... More columns
      ]
    },
    // ... More tables
  ]
}
```

- Error (400 Bad Request):

```json
{
  "error": "Required Database credentials not provided"
}
```

- Error (500 Internal Server Error):

```json
{
  "error": "Error retrieving schema information: error_message"
}
```


## 3. Search Table View

### Endpoint:
- `GET /api/v1/search/<str:table_name>/`

### Description:
 Searches for a specific table in the database and retrieves its information.

### Request:
 <str:table_name>: The name of the table to search for.

### Response:
- Success (200 OK):

```json
{
  "name": "your_table_name",
  "schema": "your_table_schema",
  "columns": [
    {"name": "column1", "type": "your_data_type"},
    {"name": "column2", "type": "your_data_type"}
    // ... More columns
  ]
}
```

- Error (400 Bad Request):

```json
{
  "error": "Table 'your_table_name' not found in database 'your_database_name'"
}
```

- Error (400 Bad Request):

```json
{
  "error": "Database credentials not provided"
}
```

- Error (500 Internal Server Error):

```json
{
  "error": "Error retrieving table information: error_message"
}
```