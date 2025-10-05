#!/bin/bash

# Simple deployment script for KJS Django application

echo "🚀 Deploying KJS Django Application"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Build and start for development
if [ "$1" = "dev" ]; then
    echo "📦 Building and starting development environment..."
    docker-compose down
    docker-compose up --build -d
    echo "✅ Development server is running at http://localhost:8000"

# Build and start for production
elif [ "$1" = "prod" ]; then
    echo "📦 Building and starting production environment..."
    docker-compose -f docker-compose.prod.yml down
    docker-compose -f docker-compose.prod.yml up --build -d
    echo "✅ Production server is running at http://localhost:8000"

# Show logs
elif [ "$1" = "logs" ]; then
    echo "📋 Showing application logs..."
    docker-compose logs -f web

# Stop services
elif [ "$1" = "stop" ]; then
    echo "🛑 Stopping services..."
    docker-compose down
    docker-compose -f docker-compose.prod.yml down
    echo "✅ All services stopped"

# Show help
else
    echo "Usage: ./deploy.sh [dev|prod|logs|stop]"
    echo "  dev   - Start development environment"
    echo "  prod  - Start production environment with Gunicorn"
    echo "  logs  - Show application logs"
    echo "  stop  - Stop all services"
fi