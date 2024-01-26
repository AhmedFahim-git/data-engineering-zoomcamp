import pandas as pd
from sqlalchemy import create_engine

trip_data = pd.read_csv("green_tripdata_2019-09.csv.gz", parse_dates=["lpep_pickup_datetime","lpep_dropoff_datetime"])

location = pd.read_csv("taxi+_zone_lookup.csv")

engine = create_engine("postgresql+psycopg2://admin:admin@localhost/de_db")

trip_data.to_sql("trips", engine, if_exists="replace")

location.to_sql("locations", engine, if_exists="replace")
