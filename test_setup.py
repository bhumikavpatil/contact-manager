#!/usr/bin/env python3
"""
Test script to verify your Contact Manager setup.
Run this to check if everything is working properly.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and return success status."""
    print(f"\n🔍 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False

def check_python():
    """Check if Python is installed."""
    return run_command("python --version", "Checking Python installation")

def check_pip():
    """Check if pip is installed."""
    return run_command("pip --version", "Checking pip installation")

def check_node():
    """Check if Node.js is installed."""
    return run_command("node --version", "Checking Node.js installation")

def check_npm():
    """Check if npm is installed."""
    return run_command("npm --version", "Checking npm installation")

def install_backend_deps():
    """Install backend dependencies."""
    os.chdir("backend")
    success = run_command("pip install -r requirements.txt", "Installing backend dependencies")
    os.chdir("..")
    return success

def test_database():
    """Test database connection."""
    os.chdir("backend")
    success = run_command("python test_db.py", "Testing database connection")
    os.chdir("..")
    return success

def install_frontend_deps():
    """Install frontend dependencies."""
    return run_command("npm install", "Installing frontend dependencies")

def main():
    print("🚀 Contact Manager Setup Test")
    print("=" * 40)
    
    # Check prerequisites
    python_ok = check_python()
    pip_ok = check_pip()
    node_ok = check_node()
    npm_ok = check_npm()
    
    if not all([python_ok, pip_ok, node_ok, npm_ok]):
        print("\n❌ Some prerequisites are missing. Please install them first.")
        return
    
    print("\n📦 Installing dependencies...")
    backend_ok = install_backend_deps()
    frontend_ok = install_frontend_deps()
    
    if not backend_ok:
        print("\n❌ Backend setup failed.")
        return
    
    print("\n🗄️ Testing database...")
    db_ok = test_database()
    
    if not db_ok:
        print("\n❌ Database connection failed.")
        return
    
    print("\n🎉 Setup Test Complete!")
    print("\nNext steps:")
    print("1. Start backend: python backend/app.py")
    print("2. Start frontend: npm start")
    print("3. Open http://localhost:3000 in your browser")

if __name__ == "__main__":
    main()
