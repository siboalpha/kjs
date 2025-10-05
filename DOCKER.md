# KJS Django Application - Docker Deployment

## 🚀 Quick Start

### Development Environment
```bash
./deploy.sh dev
```
Visit: http://localhost:8000

### Production Environment
```bash
./deploy.sh prod
```
Visit: http://localhost:8000

### Other Commands
```bash
./deploy.sh logs    # View application logs
./deploy.sh stop    # Stop all services
```

## 📁 Docker Files

- **`Dockerfile`** - Development container with Django dev server
- **`Dockerfile.prod`** - Production container with Gunicorn WSGI server
- **`docker-compose.yml`** - Development environment setup
- **`docker-compose.prod.yml`** - Production environment setup
- **`.env.docker`** - Environment variables for containers
- **`.dockerignore`** - Files excluded from Docker build context

## 🔧 Configuration

### Environment Variables
Edit `.env.docker` to customize:
```bash
SECRET_KEY=your-secret-key-here
```

### Production Settings
The application automatically runs with:
- `DEBUG=False`
- Static files served via WhiteNoise
- Gunicorn WSGI server (3 workers)
- Non-root user for security

## 📋 Requirements

- Docker & Docker Compose
- No Python installation required on host

## 🔒 Security Features

- Non-root user inside container
- Static files properly configured for production
- Environment-based configuration
- Latest security updates from Python 3.11 slim image

## 🏗️ Manual Docker Commands

### Development
```bash
docker-compose up --build -d
```

### Production
```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

### View Logs
```bash
docker-compose logs -f web
```

### Stop Services
```bash
docker-compose down
```

## 📊 Container Status

Check if containers are running:
```bash
docker-compose ps
```

## 🎯 Package Versions

- Django 5.2.7
- Python 3.11
- Gunicorn (production)
- WhiteNoise (static files)

Your Django application is now fully containerized and production-ready! 🎉