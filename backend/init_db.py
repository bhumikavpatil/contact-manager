#!/usr/bin/env python3
"""
Database initialization script for Neon PostgreSQL database.
Run this script to create all tables in your Neon database.
"""

import os
from dotenv import load_dotenv
from app import create_app, init_db

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Create Flask app
    app = create_app()
    
    print("Initializing database...")
    print(f"Database URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # Initialize database tables
    init_db(app)
    
    print("✅ Database initialized successfully!")
    print("Tables created:")
    print("- users")
    print("- contacts")

if __name__ == "__main__":
    main()
