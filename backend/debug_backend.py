#!/usr/bin/env python3
"""
Quick backend diagnostic script
"""

import sys
import os

print("🔍 Backend Diagnostic...")

# Check if we're in the right directory
print(f"Current directory: {os.getcwd()}")

# Check if config.py exists
if os.path.exists('config.py'):
    print("✅ config.py found")
else:
    print("❌ config.py missing")

# Check if app.py exists
if os.path.exists('app.py'):
    print("✅ app.py found")
else:
    print("❌ app.py missing")

# Try to import and test
try:
    from app import create_app
    print("✅ App imports successfully")
    
    app = create_app()
    print("✅ App created successfully")
    
    # Test database connection
    with app.app_context():
        from app import db
        with db.engine.connect() as conn:
            conn.execute(db.text("SELECT 1"))
        print("✅ Database connection works")
    
    print("\n🚀 Starting server on http://localhost:5000")
    print("Press Ctrl+C to stop")
    app.run(host='0.0.0.0', port=5000, debug=True)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
