from faker import Faker
import datetime
import random

fake = Faker()
start_time = datetime.datetime(2025, 6, 1, 0, 0, 0)
num_records = 100

table_name = "sensor_readings"

f = open("./sensorFakeData.sql", "w")

for i in range(num_records):
    timestamp = fake.date_time_between(start_date=start_time, end_date='now').isoformat()
    device_id = random.choice(["temp1", "temp2", "temp3"])
    sensor_index = random.randint(0, 3) 
    value = round(random.uniform(-10.0, 10.0), 2) 

    if i == 0: f.write(f"Insert into {table_name} Values('{timestamp}', '{device_id}', {sensor_index}, {value}),\n")
    elif i == num_records-1: f.write(f"('{timestamp}', '{device_id}', {sensor_index}, {value})\n")
    else: f.write(f"('{timestamp}', '{device_id}', {sensor_index}, {value}),\n")

f.close()
