#!/bin/bash

DB_FILE="example.duckdb"
rm -f "$DB_FILE"

echo "creating database $DB_FILE....."

duckdb "$DB_FILE" <<EOF

CREATE TABLE table1 (
    id INTEGER,
    last_seen_at TIMESTAMP,
    alumnized_at TIMESTAMP,
    email_stop BOOLEAN,
    updated_at TIMESTAMP,
    reset_password_token TEXT,
    reset_password_sent_at TIMESTAMP,
    year_pool INTEGER
);

CREATE TABLE table2 (
    id INTEGER,
    last_seen_at TIMESTAMP,
    alumnized_at TIMESTAMP,
    email_stop BOOLEAN,
    updated_at TIMESTAMP,
    reset_password_token TEXT,
    reset_password_sent_at TIMESTAMP,
);

INSERT INTO table1 VALUES
(1, '2023-10-01 12:00:00', '2024-01-01 09:30:00', TRUE,  '2024-05-10 17:15:00', 'token123', '2024-05-10 17:20:00', 2025),
(2, '2023-11-05 14:45:00', NULL,                  FALSE, '2024-05-11 12:00:00', NULL,       NULL, 2025),
(3, NULL,                  '2024-02-03 08:00:00', TRUE,  '2024-05-12 10:00:00', 'token789', NULL, 2025),
(4, '2024-01-15 18:30:00', '2024-04-01 07:15:00', TRUE,  '2024-05-13 11:00:00', 'token000', '2024-05-13 11:10:00', 2025),
(5, '2024-02-10 09:10:00',                  NULL,                  FALSE, '2024-05-14 14:00:00', NULL,       NULL, 2025),
(6, '2024-03-10 10:00:00', '2024-04-15 15:00:00', TRUE,  '2024-05-15 16:00:00', 'tokenXYZ', '2024-05-15 16:10:00', 2025);

INSERT INTO table2 VALUES
(1, '2023-10-01 12:00:00', '2024-01-01 09:30:00', TRUE,  '2024-05-10 17:15:00', 'token123', '2024-05-10 17:20:00'),
(2, '2023-11-05 14:45:00', '2024-03-01 10:00:00', FALSE, '2024-05-11 12:00:00', 'token456', '2024-05-11 12:10:00'),
(3, NULL,                  '2024-02-03 08:00:00', TRUE,  '2024-05-12 10:00:00', NULL,       NULL),
(4, '2024-01-15 18:30:00', NULL,                  TRUE,  '2024-05-13 11:00:00', 'token000', NULL),
(5, '2024-02-10 09:00:00', NULL,                  FALSE, '2024-05-14 14:00:00', NULL,       NULL),
(6, '2024-03-10 10:00:00', '2024-04-15 15:00:00', TRUE,  '2024-05-15 16:00:00', 'tokenXYZ', '2024-05-15 16:10:00');

EOF

echo "Database $DB_FILE created with sample data."
