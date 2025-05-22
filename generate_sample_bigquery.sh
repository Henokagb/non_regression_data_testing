#!/bin/bash


PROJECT_ID="$1"
TABLE1="$2"
TABLE2="$3"
# The projet must to have billing enabled otherwise you'll get
#BigQuery error in query operation: Error processing job 'test-460520:bqjob_r2715ddc4eed0fe57_00000196f4b361e9_1': Billing has not been enabled for this project. Enable billing at
# In my case, it's not



bq query --project_id=$PROJECT_ID --use_legacy_sql=false "
INSERT INTO \`$TABLE1\` (id, last_seen_at, alumnized_at, email_stop, updated_at, reset_password_token, reset_password_sent_at)
VALUES
(1, '2023-10-01 12:00:00', '2024-01-01 09:30:00', TRUE,  '2024-05-10 17:15:00', 'token123', '2024-05-10 17:20:00'),
(2, '2023-11-05 14:45:00', NULL,                  FALSE, '2024-05-11 12:00:00', NULL,       NULL),
(3, NULL,                  '2024-02-03 08:00:00', TRUE,  '2024-05-12 10:00:00', 'token789', NULL),
(4, '2024-01-15 18:30:00', '2024-04-01 07:15:00', TRUE,  '2024-05-13 11:00:00', 'token000', '2024-05-13 11:10:00'),
(5, '2024-02-10 09:10:00', NULL,                  FALSE, '2024-05-14 14:00:00', NULL,       NULL),
(6, '2024-03-10 10:00:00', '2024-04-15 15:00:00', TRUE,  '2024-05-15 16:00:00', 'tokenXYZ', '2024-05-15 16:10:00');
"


bq query --project_id=$PROJECT_ID --use_legacy_sql=false "
INSERT INTO \`$TABLE1` (id, last_seen_at, alumnized_at, email_stop, updated_at, reset_password_token, reset_password_sent_at)
VALUES
(1, '2023-10-01 12:00:00', '2024-01-01 09:30:00', TRUE,  '2024-05-10 17:15:00', 'token123', '2024-05-10 17:20:00'),
(2, '2023-11-05 14:45:00', '2024-03-01 10:00:00', FALSE, '2024-05-11 12:00:00', 'token456', '2024-05-11 12:10:00'),
(3, NULL,                  '2024-02-03 08:00:00', TRUE,  '2024-05-12 10:00:00', NULL,       NULL),
(4, '2024-01-15 18:30:00', NULL,                  TRUE,  '2024-05-13 11:00:00', 'token000', NULL),
(5, '2024-02-10 09:00:00', NULL,                  FALSE, '2024-05-14 14:00:00', NULL,       NULL),
(6, '2024-03-10 10:00:00', '2024-04-15 15:00:00', TRUE,  '2024-05-15 16:00:00', 'tokenXYZ', '2024-05-15 16:10:00');
"
