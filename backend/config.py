"""
Configuration file for the Contact Manager backend.
Set your environment variables or modify this file for production.
"""

import os

class Config:
    # Database Configuration
    DATABASE_URL = "postgresql://neondb_owner:npg_V1eop0wBHikJ@ep-plain-brook-ad4wvfvy-pooler.c-2.us-east-1.aws.neon.tech/contactmanager?sslmode=require&channel_binding=require"
    
    # JWT Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-change-this-in-production")
    
    # CORS Configuration
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
    
    # Server Configuration
    PORT = int(os.getenv("PORT", "5000"))
    
    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
