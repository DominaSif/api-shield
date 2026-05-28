CREATE ROLE app_user WITH LOGIN PASSWORD 'changeme';
-- app role for fastApi, real/write only
CREATE ROLE migrations WITH LOGIN PASSWORD 'changeme';
-- migrations role, schema changes only
