CREATE TABLE IF NOT EXISTS yellow_tripdata (
    vendor_id TEXT,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count INT,
    trip_distance FLOAT,
    rate_code TEXT,
    payment_type TEXT,
    total_amount FLOAT
);
