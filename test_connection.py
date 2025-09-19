#!/usr/bin/env python3
"""
Test script to verify frontend-backend-database connection
"""

import requests
import json

def test_backend():
    print("🔍 Testing Backend Connection...")
    
    try:
        # Test root endpoint
        response = requests.get('http://localhost:5000/')
        print(f"✅ Root endpoint: {response.status_code}")
        print(f"   Response: {response.json()}")
        
        # Test health endpoint
        response = requests.get('http://localhost:5000/api/health')
        print(f"✅ Health endpoint: {response.status_code}")
        print(f"   Response: {response.json()}")
        
        # Test registration
        test_user = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpass123"
        }
        
        response = requests.post('http://localhost:5000/api/auth/register', 
                               json=test_user,
                               headers={'Content-Type': 'application/json'})
        print(f"✅ Registration test: {response.status_code}")
        if response.status_code == 201:
            data = response.json()
            print(f"   User created: {data['user']['name']}")
            print(f"   Token: {data['token'][:20]}...")
            return data['token']
        else:
            print(f"   Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Make sure it's running on http://localhost:5000")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_contact_creation(token):
    if not token:
        print("❌ No token available for contact test")
        return
        
    print("\n🔍 Testing Contact Creation...")
    
    try:
        test_contact = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "company": "Test Company"
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        
        response = requests.post('http://localhost:5000/api/contacts', 
                               json=test_contact,
                               headers=headers)
        print(f"✅ Contact creation: {response.status_code}")
        if response.status_code == 201:
            data = response.json()
            print(f"   Contact created: {data['name']} ({data['email']})")
            print("✅ Data successfully stored in Neon database!")
        else:
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error creating contact: {e}")

if __name__ == "__main__":
    print("🚀 Testing Frontend-Backend-Database Connection")
    print("=" * 50)
    
    token = test_backend()
    test_contact_creation(token)
    
    print("\n" + "=" * 50)
    print("If all tests pass, your setup is working correctly!")
    print("If not, check the error messages above.")
