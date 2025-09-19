# Contact Manager - Render Deployment Guide

This guide will help you deploy your Contact Manager application to Render without errors.

## Prerequisites

1. A GitHub account
2. A Render account (free tier available)
3. Your code pushed to a GitHub repository

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure your project structure looks like this:
```
contact/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── config_prod.py
│   └── requirements.txt
├── src/
│   └── (React components)
├── package.json
├── build.sh
├── start_prod.py
├── render.yaml
└── Procfile
```

### 2. Push to GitHub

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 3. Deploy on Render

#### Option A: Using render.yaml (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file
5. Click "Apply" to use the configuration

#### Option B: Manual Configuration

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `contact-manager`
   - **Environment**: `Python 3`
   - **Build Command**: `chmod +x build.sh && ./build.sh`
   - **Start Command**: `python start_prod.py`
   - **Plan**: Free

### 4. Set Environment Variables

In your Render service dashboard, go to "Environment" tab and add:

```
FLASK_ENV=production
DATABASE_URL=your_neon_database_url
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
ALLOW_ORIGINS=*
PORT=10000
```

### 5. Database Setup

Your application is already configured to use Neon PostgreSQL. The database URL is already set in your config files.

### 6. Deploy

Click "Deploy" and wait for the build to complete. The deployment process will:

1. Install Node.js dependencies
2. Build the React frontend
3. Install Python dependencies
4. Copy frontend build to backend static folder
5. Start the application

## Troubleshooting

### Common Issues

1. **Build Fails**: Check the build logs in Render dashboard
2. **Database Connection**: Verify your DATABASE_URL is correct
3. **Static Files**: Ensure the build process copies files to the correct location
4. **CORS Issues**: Check ALLOW_ORIGINS environment variable

### Build Logs

If deployment fails, check the build logs:
1. Go to your service in Render dashboard
2. Click on "Logs" tab
3. Look for error messages

### Health Check

Your app includes a health check endpoint at `/api/health`. Render will use this to verify the service is running.

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `FLASK_ENV` | Flask environment | `production` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host:port/db` |
| `SECRET_KEY` | Flask secret key | `your-secret-key` |
| `JWT_SECRET_KEY` | JWT signing key | `your-jwt-secret` |
| `ALLOW_ORIGINS` | CORS allowed origins | `*` or `https://yourdomain.com` |
| `PORT` | Server port | `10000` |

## Post-Deployment

After successful deployment:

1. Your app will be available at `https://your-app-name.onrender.com`
2. The React frontend will be served from the root URL
3. API endpoints are available at `/api/*`
4. Database will be automatically initialized

## Monitoring

- Check the "Metrics" tab for performance data
- Use "Logs" tab to monitor application logs
- Set up alerts in the "Alerts" section

## Scaling

- Free tier includes 750 hours/month
- Upgrade to paid plans for more resources
- Consider upgrading if you exceed free tier limits

## Support

If you encounter issues:
1. Check Render's documentation
2. Review build logs
3. Verify environment variables
4. Test locally with production settings
