import pyodbc
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Connect to SQL Server
server = 'tcp:sqlserver.database.windows.net,0000'  # or 'localhost\\SQLEXPRESS' for local
database = '****'
username = '***'
password = '****'

# DB Connection
conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )

cursor = conn.cursor()

# Weather types to randomize
weather_types = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Thunderstorm', 'Windy', 'Foggy']

# Insert 1000 rows
for _ in range(1000):
    city = fake.city()
    country = fake.country()
    temp = round(random.uniform(-10.0, 45.0), 2)
    humidity = random.randint(10, 100)
    pressure = random.randint(950, 1050)
    weather = random.choice(weather_types)
    obs_time = fake.date_time_between(start_date='-30d', end_date='now')

    cursor.execute("""
        INSERT INTO WeatherData (
            City, Country, Temperature, Humidity, Pressure, WeatherDescription, ObservationTime
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, city, country, temp, humidity, pressure, weather, obs_time)

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Inserted 1000 rows into WeatherData")
