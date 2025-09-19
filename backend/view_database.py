#!/usr/bin/env python3
"""
View all data stored in your Neon database
"""

from app import create_app, db, User, Contact
from datetime import datetime

def view_database():
    print("🗄️  NEON DATABASE CONTENTS")
    print("=" * 50)
    print(f"Database: contactmanager")
    print(f"Host: ep-plain-brook-ad4wvfvy-pooler.c-2.us-east-1.aws.neon.tech")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    app = create_app()
    
    with app.app_context():
        try:
            # Check USERS table
            print("\n👥 USERS TABLE:")
            print("-" * 30)
            users = User.query.all()
            if users:
                for i, user in enumerate(users, 1):
                    print(f"{i}. ID: {user.id}")
                    print(f"   Name: {user.name}")
                    print(f"   Email: {user.email}")
                    print(f"   Created: {user.contacts[0].created_at if user.contacts else 'No contacts yet'}")
                    print()
            else:
                print("   No users found")
            
            # Check CONTACTS table
            print("\n📞 CONTACTS TABLE:")
            print("-" * 30)
            contacts = Contact.query.all()
            if contacts:
                for i, contact in enumerate(contacts, 1):
                    print(f"{i}. ID: {contact.id}")
                    print(f"   Name: {contact.name}")
                    print(f"   Email: {contact.email}")
                    print(f"   Phone: {contact.phone or 'N/A'}")
                    print(f"   Company: {contact.company or 'N/A'}")
                    print(f"   User ID: {contact.user_id}")
                    print(f"   Favorite: {'⭐' if contact.is_favorite else '❌'}")
                    print(f"   Created: {contact.created_at}")
                    print()
            else:
                print("   No contacts found")
            
            # Summary
            print("\n📊 SUMMARY:")
            print("-" * 30)
            print(f"Total Users: {len(users)}")
            print(f"Total Contacts: {len(contacts)}")
            
            if users or contacts:
                print("\n✅ Data is successfully stored in your Neon database!")
                print("🌐 You can also view this data in the Neon Console:")
                print("   https://neon.tech/console")
            else:
                print("\n⚠️  No data found. Try adding some contacts in the frontend.")
                
        except Exception as e:
            print(f"❌ Error accessing database: {e}")
            print("Make sure your backend is running and database is connected.")

if __name__ == "__main__":
    view_database()
