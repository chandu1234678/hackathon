#!/usr/bin/env python
"""
Quick database reset for external PostgreSQL databases.
Works with any PostgreSQL database URL (not just Render).

Usage:
    python reset_external_db.py          # Interactive mode
    python reset_external_db.py --auto   # Use DATABASE_URL from env
"""
import os
import sys
import argparse
from urllib.parse import urlparse

def get_database_url():
    """Get DATABASE_URL from environment variable."""
    url = os.getenv("DATABASE_URL")
    if not url:
        print("❌ DATABASE_URL not found in environment variables")
        print("\nTo set it, add to your .env file in backend folder:")
        print("  DATABASE_URL=postgresql://user:password@host:5432/dbname")
        return None
    return url

def parse_database_url(url):
    """Parse PostgreSQL connection string."""
    try:
        parsed = urlparse(url)
        return {
            "user": parsed.username,
            "password": parsed.password,
            "host": parsed.hostname,
            "port": parsed.port or 5432,
            "database": parsed.path.lstrip("/"),
            "full_url": url
        }
    except Exception as e:
        print(f"❌ Error parsing database URL: {e}")
        return None

def reset_external_database(db_config):
    """Reset external PostgreSQL database."""
    try:
        import psycopg2
        from psycopg2 import extras
    except ImportError:
        print("❌ psycopg2 not installed")
        print("\nInstall it with:")
        print("  pip install psycopg2-binary")
        return False
    
    print("\n" + "=" * 60)
    print("EXTERNAL DATABASE RESET")
    print("=" * 60)
    print(f"\nDatabase: {db_config['database']}")
    print(f"Host: {db_config['host']}")
    print(f"User: {db_config['user']}")
    print(f"Port: {db_config['port']}")
    
    confirm = input("\n⚠️  This will DELETE ALL DATA. Type 'RESET' to confirm: ").strip()
    if confirm != "RESET":
        print("❌ Reset cancelled")
        return False
    
    try:
        print("\n🔌 Connecting to database...")
        conn = psycopg2.connect(
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"],
            database=db_config["database"]
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        print("✓ Connected")
        
        # Delete data in order (respecting foreign keys)
        tables = [
            "prediction_logs",
            "ulcer_images", 
            "patients",
            "health_metrics",
            "users"
        ]
        
        for table in tables:
            try:
                cursor.execute(f"DELETE FROM {table} CASCADE;")
                count = cursor.rowcount
                print(f"✓ Cleared {table} ({count} rows deleted)")
            except Exception as e:
                print(f"⚠️  {table}: {str(e)}")
        
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 60)
        print("✓ DATABASE RESET COMPLETE")
        print("=" * 60)
        print("\nYou can now create a new account:")
        print("  Email: your-email@example.com")
        print("  Password: at least 8 characters")
        print("\nNext: Deploy to Render with 'git push'")
        return True
        
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")
        print("\nCommon causes:")
        print("  - Invalid DATABASE_URL format")
        print("  - Host/port incorrect")
        print("  - Username/password wrong")
        print("  - Database doesn't exist")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Reset external PostgreSQL database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python reset_external_db.py              # Interactive (uses .env)
  python reset_external_db.py --auto       # Auto mode (uses environment)
        """
    )
    parser.add_argument("--auto", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()
    
    # Get DATABASE_URL
    database_url = get_database_url()
    if not database_url:
        sys.exit(1)
    
    # Parse it
    db_config = parse_database_url(database_url)
    if not db_config:
        sys.exit(1)
    
    # Reset
    if reset_external_database(db_config):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
