CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS sensors (
    sensor_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
    sensor_type TEXT
);

CREATE TABLE IF NOT EXISTS sensor_readings (
    id BIGSERIAL PRIMARY KEY,
    sensor_id TEXT NOT NULL REFERENCES sensors(sensor_id),
    timestamp TIMESTAMPTZ NOT NULL,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    pressure DOUBLE PRECISION,
    battery DOUBLE PRECISION
);

CREATE TABLE sensor_documents (
    id BIGSERIAL PRIMARY KEY,
    sensor_id TEXT REFERENCES sensors(sensor_id),
    content TEXT NOT NULL,
    embedding VECTOR(384),
    created_at TIMESTAMPTZ DEFAULT NOW()
);


CREATE INDEX IF NOT EXISTS idx_sensor_readings_sensor_time
ON sensor_readings(sensor_id, timestamp);

