import pytest
import asyncpg

async def get_conn():
    return await asyncpg.connect(
        "postgresql://app_user:changeme@localhost/datagate"
    )

@pytest.mark.asyncio
async def test_sqli_in_title():
    conn = await get_conn()

    # set user context
    await conn.execute("SET app.user_id = '1'")

    # classic sqli attempt
    malicious = "' OR '1'='1"
    docs = await conn.fetch(
        "SELECT * FROM documents WHERE title = $1",
        malicious
    )

    # nothing returned- injection didnt work
    assert len(docs) == 0

    await conn.close()
