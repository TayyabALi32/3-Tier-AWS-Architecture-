CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name) VALUES ('Deploy 3-Tier App on AWS');
INSERT INTO items (name) VALUES ('Master Docker Compose YAML');
#hi
