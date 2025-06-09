from faker import Faker
import datetime
import random

fake = Faker()
start_time = datetime.datetime(2025, 1, 1, 0, 0, 0)
num_records = 100

table_name = "sensor_readings"

f = open("./sensorFakeData.sql", "w")

for i in range(num_records):
    timestamp = fake.date_time_between(start_date=start_time, end_date='now')
    device_id = random.choice(["hub_alpha", "hub_beta", "hub_gamma"])
    sensor_index = random.randint(0, 3) # Например, 0-температура, 1-влажность
    value = round(random.uniform(0.0, 100.0), 2) # Произвольное значение


    f.write(f"Insert into {table_name} Values({timestamp},{device_id},{sensor_index}, {value})\n")

f.close()