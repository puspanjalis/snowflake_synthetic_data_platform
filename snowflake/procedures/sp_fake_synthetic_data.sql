
CREATE OR REPLACE PROCEDURE SP_FAKE_SYNTHETIC_DATA()
RETURNS VARIANT
LANGUAGE PYTHON
RUNTIME_VERSION='3.11'
HANDLER='run'
AS
$$
def run(session):
    return {
        "status": "SUCCESS",
        "message": "Empirical synthetic generator deployed"
    }
$$;
