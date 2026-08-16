Walmart dataset loader

Purpose

This folder contains CSV data and a small loader script (load_data.py) that imports the CSV files into the database tables under the `raw` schema.

Prerequisites

- Python 3.8+ installed
- pip available (to install dependencies)
- Network access to the PostgreSQL server that will host the data

Dependencies

Install the Python DB driver before running the loader:

Windows / PowerShell:

    python -m pip install psycopg2-binary

Usage

The loader reads the database connection from the POSTGRES_CONNECTION_STRING environment variable. Do NOT hardcode secrets into the script.

Examples (PowerShell):

Temporarily set the variable for the current shell and run the loader:

    $env:POSTGRES_CONNECTION_STRING = "postgresql://<user>:<password>@<host>:5432/tsdb?sslmode=require"
    python .\load_data.py

Make the variable permanent for your Windows user (applies to new terminals):

    setx POSTGRES_CONNECTION_STRING "postgresql://<user>:<password>@<host>:5432/tsdb?sslmode=require"

Run from repository root (PowerShell):

    python .\walmart_dataset\load_data.py

Notes about the included .env file

A .env file exists in this folder for convenience, but load_data.py only reads the POSTGRES_CONNECTION_STRING environment variable. If you prefer auto-loading .env files, install python-dotenv and add `from dotenv import load_dotenv; load_dotenv()` at the top of load_data.py, or run with a dotenv runner.

Verification

After a successful run you can verify row counts with psql or a Python query. Example psql command:

    psql "postgresql://<user>:<password>@<host>:5432/tsdb?sslmode=require" -c "SELECT table_name, COUNT(*) FROM information_schema.tables t JOIN pg_catalog.pg_class c ON t.table_name=c.relname WHERE table_schema='raw' GROUP BY table_name;"

(Or use simple SELECT count(*) FROM raw.customers; etc.)

Security

- Do NOT commit the .env file or any files containing secrets. Add the following line to your repository's .gitignore if it is not already ignored:

    /walmart_dataset/.env

- Consider using a secrets manager for production credentials (Azure Key Vault, AWS Secrets Manager, Windows Credential Manager, GitHub Actions secrets, etc.).

Troubleshooting

- If psycopg2 fails to install on Windows, install the precompiled wheel `psycopg2-binary` as shown above.
- If the loader fails with authentication/permission errors, verify the connection string and that the target user has rights to INSERT into the `raw` schema tables.

If you want, I can add a small README entry to the repository root linking to this file or add .env to .gitignore for you.