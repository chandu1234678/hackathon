#!/usr/bin/env python
"""
Database initialization script - creates all tables and sets up the database.

Usage:
    python init_db.py        # Create tables (no delete)
    python init_db.py --fresh  # Drop and recreate tables
"""
import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from app.database import Base, engine
from app.models import User, Patient, PredictionLog, UlcerImage
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db(fresh: bool = False):
    """
    Initialize the database.
    
    Args:
        fresh: If True, drop all tables before creating them
    """
    try:
        if fresh:
            logger.info("Dropping all existing tables...")
            Base.metadata.drop_all(bind=engine)
            logger.info("✓ All tables dropped")
        
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("✓ Database tables created successfully")
        
        # Verify tables were created
        inspector_import = None
        try:
            from sqlalchemy import inspect
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            logger.info(f"✓ Tables created: {', '.join(tables)}")
        except Exception as e:
            logger.warning(f"Could not verify tables: {e}")
        
        logger.info("\n✓ Database initialization complete!")
        return True
    
    except Exception as e:
        logger.error(f"✗ Error initializing database: {str(e)}")
        return False


def create_sample_user():
    """Create a sample user for testing."""
    from app.database import SessionLocal
    from app.auth.password_utils import hash_password
    
    db = SessionLocal()
    try:
        # Check if user already exists
        existing = db.query(User).filter(User.email == "test@example.com").first()
        if existing:
            logger.info("✓ Sample user already exists (test@example.com)")
            return
        
        user = User(
            email="test@example.com",
            hashed_password=hash_password("password123")
        )
        db.add(user)
        db.commit()
        logger.info("✓ Sample user created (test@example.com / password123)")
    except Exception as e:
        logger.error(f"Could not create sample user: {e}")
    finally:
        db.close()


def verify_migration():
    """Verify database schema matches models."""
    try:
        from sqlalchemy import inspect
        inspector = inspect(engine)
        
        # Check required columns in PredictionLog
        prediction_log_cols = [col['name'] for col in inspector.get_columns('prediction_logs')]
        required_cols = ['id', 'user_id', 'patient_id', 'prediction', 'confidence', 
                        'risk_score', 'risk_level', 'severity', 'explanation_text', 
                        'image_url', 'created_at']
        
        missing = [col for col in required_cols if col not in prediction_log_cols]
        if missing:
            logger.warning(f"⚠ Missing columns in prediction_logs: {missing}")
            return False
        
        logger.info("✓ Database schema verification passed")
        return True
    except Exception as e:
        logger.error(f"Schema verification failed: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize database for MedVision AI")
    parser.add_argument("--fresh", action="store_true", help="Drop and recreate all tables")
    parser.add_argument("--sample-user", action="store_true", help="Create sample user for testing")
    parser.add_argument("--verify", action="store_true", help="Verify database schema only")
    
    args = parser.parse_args()
    
    if args.verify:
        logger.info("Verifying database schema...")
        success = verify_migration()
        sys.exit(0 if success else 1)
    
    success = init_db(fresh=args.fresh)
    
    if success and args.sample_user:
        create_sample_user()
    
    if success:
        verify_migration()
        sys.exit(0)
    else:
        sys.exit(1)
