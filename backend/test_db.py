#!/usr/bin/env python3
"""
Test script to verify Neon database connection and create tables.
"""

from app import create_app, init_db, db
from config import Config

def test_connection():
    """Test database connection and create tables."""
    print("Testing Neon database connection...")
    print(f"Database URL: {Config.DATABASE_URL}")
    
    try:
        # Create Flask app
        app = create_app()
        
        with app.app_context():
            # Test connection
            db.engine.execute("SELECT 1")
            print("✅ Database connection successful!")
            
            # Create tables
            print("Creating database tables...")
            init_db(app)
            print("✅ Tables created successfully!")
            
            # Test table creation
            from app import User, Contact
            print(f"✅ User table: {User.__tablename__}")
            print(f"✅ Contact table: {Contact.__tablename__}")
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_connection()
    if success:
        print("\n🎉 Your Neon database is ready to use!")
        print("You can now start your Flask server with: python app.py")
    else:
        print("\n❌ Database setup failed. Please check your connection string.")
