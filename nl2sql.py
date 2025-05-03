import os
import pyodbc
import requests
from dotenv import load_dotenv

load_dotenv()

# Load DB credentials
server = os.getenv("SERVER")
database = os.getenv("DATABASE")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Connect to Azure SQL
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
cursor = conn.cursor()

# Ask user for a natural language question
nl_question = input("Ask a question about your weather data: ")

# Send to Ollama (LLaMA 2)
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama2",
        "prompt": f"Convert this natural language query to SQL: {nl_question}",
        "stream": False
    }
)

generated_sql = response.json()['response']
print(f"Generated SQL: {generated_sql}")

# Execute SQL and fetch results
try:
    cursor.execute(generated_sql)
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print("❌ Error executing SQL:", e)

conn.close()
