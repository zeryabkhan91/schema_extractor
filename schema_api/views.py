import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sqlalchemy import MetaData

from .middleware import _thread_locals


@csrf_exempt
def credentials(request):
  if request.method == "POST":

    if _thread_locals.engine:
      return JsonResponse({"message": "Credentials processed successfully"})
    else:
      return JsonResponse(
        {"error": "Required Database credentials not provided"}, status=400
      )

  return JsonResponse({"error": "Invalid request method"}, status=405)

def schema(request):
  db_engine = _thread_locals.engine
  credentials = _thread_locals.credentials

  if not db_engine:
    return JsonResponse({"error": "Database credentials not provided"}, status=400)

  try:
      metadata = MetaData()
      metadata.reflect(bind = db_engine)

      schema_info = {
          "database_name": credentials["NAME"],
          "tables": [
              {
                  "name": table.name,
                  "schema": table.schema,
                  "columns": [
                      {"name": column.name, "type": str(column.type)}
                      for column in table.columns
                  ],
              }
              for table in metadata.sorted_tables
          ],
      }

      return JsonResponse(schema_info)

  except Exception as e:
      return JsonResponse(
          {"error": f"Error retrieving schema information: {str(e)}"}, status=500
      )

def search_table(request, table_name):
  credentials = _thread_locals.credentials
  db_engine = _thread_locals.engine
    
  if not db_engine:
      return JsonResponse({"error": "Database credentials not provided"}, status=400)

  try:
      metadata = MetaData()
      metadata.reflect(bind=db_engine)

      if table_name in metadata.tables:
          table = metadata.tables[table_name]

          table_info = {
              "name": table.name,
              "schema": table.schema,
              "columns": [
                  {"name": column.name, "type": str(column.type)}
                  for column in table.columns
              ],
          }

          return JsonResponse(table_info)
      else:
          return JsonResponse({"error": f"Table '{table_name}' not found in database '{credentials['NAME']}"}, status=404)
  except Exception as e:
    return JsonResponse(
      {"error": f"Error retrieving table information: {str(e)}"}, status=500
    )