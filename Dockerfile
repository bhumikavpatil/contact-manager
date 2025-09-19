# Multi-stage build for React + Flask application
FROM node:18-alpine AS frontend-build

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy source code
COPY src/ ./src/
COPY public/ ./public/
COPY tailwind.config.js postcss.config.js ./

# Build the React app
RUN npm run build

# Python backend stage
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

# Copy built frontend
COPY --from=frontend-build /app/build ./backend/static

# Set environment variables
ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Set the working directory to backend
WORKDIR /app/backend

# Expose port
EXPOSE 10000

# Start the application
CMD ["python", "app.py"]
