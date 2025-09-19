#!/bin/bash

# Build script for Render deployment
echo "Building Contact Manager for production..."

# Install frontend dependencies
echo "Installing frontend dependencies..."
npm install --legacy-peer-deps

# Build frontend
echo "Building React frontend..."
npm run build

# Install backend dependencies
echo "Installing backend dependencies..."
cd backend
pip install -r requirements.txt

# Create static directory and copy built frontend
echo "Setting up static files..."
mkdir -p static
cp -r ../build/* static/

echo "Build completed successfully!"
