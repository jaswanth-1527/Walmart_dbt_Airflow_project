import os

try:
    import psycopg2 # pyright: ignore[reportMissingModuleSource]
except ImportError:
    raise ImportError(
        "psycopg2 module is not installed. "
        "Install it with: pip install psycopg2-binary"
    )

# Database connection string comes from the environment for safety.
conn_string = os.getenv("POSTGRES_CONNECTION_STRING")
if not conn_string:
    raise ValueError(
        "POSTGRES_CONNECTION_STRING environment variable is required."
        " Example: postgresql://tsdbadmin:password@host:5432/tsdb?sslmode=require"
    )

# CSV files mapping to tables
csv_files = {
    "customers.csv": "raw.customers",
    "stores.csv": "raw.stores",
    "products.csv": "raw.products",
    "employees.csv": "raw.employees",
    "orders.csv": "raw.orders",
    "order_items.csv": "raw.order_items",
}

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")

try:
    # Connect to the database
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    # Load each CSV file into its corresponding table
    for csv_file, table_name in csv_files.items():
        csv_path = os.path.join(data_dir, csv_file)
        
        if os.path.exists(csv_path):
            print(f"Loading {csv_file} into {table_name}...")
            
            with open(csv_path, 'r') as f:
                cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, HEADER TRUE)", f)
            
            conn.commit()
            print(f"✓ Successfully loaded {csv_file}")
        else:
            print(f"✗ File not found: {csv_path}")
    
    cursor.close()
    conn.close()
    print("\n✓ All data loaded successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    if conn:
        conn.rollback()
        conn.close()
