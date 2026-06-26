--- app_user data access
GRANT SELECT, INSERT, UPDATE ON documents TO app_user;
GRANT SELECT ON users TO app_user;

-- migration full perms
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO migrations;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO migrations;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;
