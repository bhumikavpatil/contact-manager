#!/usr/bin/env python3
"""
Quick script to check if data is being stored in Neon database
"""

from app import create_app, db, User, Contact
from datetime import datetime

def check_database():
    print("🔍 Checking Neon Database...")
    
    app = create_app()
    
    with app.app_context():
        try:
            # Check users
            users = User.query.all()
            print(f"👥 Users in database: {len(users)}")
            for user in users:
                print(f"   - {user.name} ({user.email})")
            
            # Check contacts
            contacts = Contact.query.all()
            print(f"📞 Contacts in database: {len(contacts)}")
            for contact in contacts:
                print(f"   - {contact.name} ({contact.email}) - User ID: {contact.user_id}")
            
            if users or contacts:
                print("\n✅ Data is being stored in Neon database!")
            else:
                print("\n⚠️  No data found. Try adding some contacts in the frontend.")
                
        except Exception as e:
            print(f"❌ Error checking database: {e}")

if __name__ == "__main__":
    check_database()
