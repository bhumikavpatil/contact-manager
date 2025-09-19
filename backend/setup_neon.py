#!/usr/bin/env python3
"""
Setup script to configure Neon database for the contact manager project.
This script will create the .env file and initialize the database.
"""

import os

def create_env_file():
    """Create .env file with Neon database configuration."""
    env_content = """# Database Configuration
DATABASE_URL=postgresql://neondb_owner:npg_V1eop0wBHikJ@ep-plain-brook-ad4wvfvy-pooler.c-2.us-east-1.aws.neon.tech/contactmanager?sslmode=require&channel_binding=require

# JWT Configuration
SECRET_KEY=your-secret-key-change-this-in-production
JWT_SECRET_KEY=your-jwt-secret-key-change-this-in-production

# CORS Configuration
ALLOW_ORIGINS=http://localhost:3000

# Server Configuration
PORT=5000
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file with Neon database configuration")

def main():
    print("Setting up Neon database for Contact Manager...")
    
    # Create .env file
    create_env_file()
    
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Initialize database: python init_db.py")
    print("3. Start the server: python app.py")
    print("\nYour Neon database is ready to use!")

if __name__ == "__main__":
    main()
