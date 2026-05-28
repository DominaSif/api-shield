-- enable RLS
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents FORCE ROW LEVEL SECURITY;

-- filter by owner
CREATE POLICY documents_select ON documents
    FOR SELECT
    USING (user_id = current_setting('app.user_id')::integer);

-- restrict inserts to owner
CREATE POLICY documents_insert ON documents
    FOR INSERT
    WITH CHECK (user_id = current_setting('app.user_id')::integer);
