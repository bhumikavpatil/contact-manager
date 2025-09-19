#!/usr/bin/env python3
"""
Debug script to test deployed Contact Manager
"""
import requests
import json

def test_deployment(base_url):
    print(f"🔍 Testing deployment at: {base_url}")
    print("=" * 50)
    
    # Test 1: Health check
    try:
        response = requests.get(f"{base_url}/api/health", timeout=10)
        print(f"✅ Health Check: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Health Check Failed: {e}")
    
    # Test 2: API root
    try:
        response = requests.get(f"{base_url}/api", timeout=10)
        print(f"✅ API Root: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ API Root Failed: {e}")
    
    # Test 3: Frontend (should return HTML)
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"✅ Frontend: {response.status_code}")
        print(f"   Content-Type: {response.headers.get('content-type', 'unknown')}")
        if 'text/html' in response.headers.get('content-type', ''):
            print("   ✅ Serving HTML (React app)")
        else:
            print("   ❌ Not serving HTML")
    except Exception as e:
        print(f"❌ Frontend Failed: {e}")
    
    # Test 4: Test registration endpoint
    try:
        test_data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = requests.post(f"{base_url}/api/auth/register", 
                               json=test_data, 
                               headers={'Content-Type': 'application/json'},
                               timeout=10)
        print(f"✅ Registration Test: {response.status_code}")
        if response.status_code == 201:
            print("   ✅ Registration endpoint working")
        elif response.status_code == 409:
            print("   ⚠️  User already exists (expected)")
        else:
            print(f"   ❌ Registration failed: {response.text}")
    except Exception as e:
        print(f"❌ Registration Test Failed: {e}")

if __name__ == "__main__":
    # Replace with your actual Render URL
    base_url = input("Enter your Render app URL (e.g., https://contact-manager.onrender.com): ").strip()
    if not base_url.startswith('http'):
        base_url = f"https://{base_url}"
    
    test_deployment(base_url)
