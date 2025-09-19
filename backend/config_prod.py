"""
Production configuration for the Contact Manager backend.
"""
import os

class ProductionConfig:
    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_V1eop0wBHikJ@ep-plain-brook-ad4wvfvy-pooler.c-2.us-east-1.aws.neon.tech/contactmanager?sslmode=require&channel_binding=require")
    
    # JWT Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-change-this-in-production")
    
    # CORS Configuration - Allow all origins in production for now
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*")
    
    # Server Configuration
    PORT = int(os.getenv("PORT", "5000"))
    
    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
