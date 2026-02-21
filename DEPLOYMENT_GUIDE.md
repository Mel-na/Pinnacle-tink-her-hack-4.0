# Deployment Guide for Astrashe on Render

## Prerequisites
- GitHub account (to host your code)
- Render account (free at render.com)

## Step 1: Push Code to GitHub

1. Initialize Git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - ready for deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/pinnacle-astrashe.git
   git push -u origin main
   ```

## Step 2: Deploy on Render

1. Go to [render.com](https://render.com) and sign in with GitHub
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Select the repository: `pinnacle-astrashe` (or your repo name)
5. Configure the service:
   - **Name**: astrashe (or any name you prefer)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: Already configured in Procfile
   - **Plan**: Free tier for testing

6. Click "Create Web Service"

## Step 3: Monitor Deployment

- Render will automatically build and deploy your app
- Check the logs in the Render dashboard to ensure everything runs smoothly
- Once live, your app will be available at: `https://astrashe.onrender.com`

## Important Notes

**Security Improvements Needed:**
- Change the hardcoded credentials in `app.py` (currently: admin@gmail.com / 1234)
- Use a proper database instead of hardcoded login
- Generate a new, strong `app.secret_key` before deployment
- Use environment variables for sensitive data

**API Keys:**
- Ensure your Leaflet.js, OSRM, and Nominatim APIs are properly configured
- Check if they support CORS from your Render domain

**Environment Variables** (if needed later):
1. Go to Environment in Render Dashboard
2. Add variables like `FLASK_ENV=production`

## Files Created/Modified:

✅ `Procfile` - Instructions for Render to run the app
✅ `runtime.txt` - Python version specification
✅ `requirements.txt` - Updated with gunicorn
✅ `app.py` - Updated to use PORT environment variable

Your app is now ready for deployment!
