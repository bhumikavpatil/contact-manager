#!/usr/bin/env python3
"""
Production startup script for Contact Manager
"""
import os
import sys
from backend.app import create_app, init_db

def main():
    # Set production environment
    os.environ['FLASK_ENV'] = 'production'
    
    # Create app
    app = create_app()
    
    # Initialize database
    with app.app_context():
        init_db(app)
        print("Database initialized successfully")
    
    # Get port from environment
    port = int(os.getenv('PORT', 5000))
    
    # Run the app
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    main()
