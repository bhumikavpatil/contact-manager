# 🔧 Contact Manager - Troubleshooting Guide

## Issue: App Deployed but Not Working

### Quick Fixes Applied:

1. **✅ Fixed CORS Configuration** - Now allows all origins in production
2. **✅ Fixed API Endpoints** - Frontend now uses relative URLs instead of localhost
3. **✅ Fixed Database Connection** - Updated to psycopg2-binary

### Steps to Fix:

#### 1. **Commit and Push the Fixes:**
```bash
git add .
git commit -m "Fix CORS and API endpoints for production"
git push origin main
```

#### 2. **Redeploy on Render:**
- Go to your Render dashboard
- Click "Manual Deploy" → "Deploy latest commit"

#### 3. **Test Your App:**

**Test API Health:**
```
https://your-app-name.onrender.com/api/health
```
Should return: `{"status": "ok", "time": "..."}`

**Test API Root:**
```
https://your-app-name.onrender.com/api
```
Should return: `{"message": "Contact Manager API", "status": "running", ...}`

**Test Frontend:**
```
https://your-app-name.onrender.com/
```
Should load the React app

### Common Issues & Solutions:

#### ❌ **"Network error" when trying to sign in**
- **Cause**: Frontend trying to connect to localhost instead of deployed backend
- **Fix**: ✅ Applied - Now uses relative URLs

#### ❌ **CORS errors in browser console**
- **Cause**: Backend not allowing frontend requests
- **Fix**: ✅ Applied - CORS now allows all origins in production

#### ❌ **"Failed to fetch" errors**
- **Cause**: API endpoints not accessible
- **Fix**: ✅ Applied - API endpoints now use correct URLs

#### ❌ **Database connection errors**
- **Cause**: Missing psycopg2 module
- **Fix**: ✅ Applied - Updated to psycopg2-binary

### Testing Your App:

1. **Open your app URL** in browser
2. **Try to register** a new account
3. **Try to login** with the account
4. **Try to add a contact**
5. **Check browser console** for any errors

### If Still Not Working:

#### Check Render Logs:
1. Go to Render dashboard
2. Click on your service
3. Go to "Logs" tab
4. Look for error messages

#### Test API Manually:
```bash
# Test health endpoint
curl https://your-app-name.onrender.com/api/health

# Test registration
curl -X POST https://your-app-name.onrender.com/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","password":"test123"}'
```

### Expected Behavior After Fix:

✅ **Frontend loads** - React app displays properly
✅ **Registration works** - Can create new accounts
✅ **Login works** - Can sign in with accounts
✅ **Contacts work** - Can add, edit, delete contacts
✅ **No CORS errors** - Browser console clean
✅ **Database connected** - Data persists between sessions

### Still Having Issues?

1. **Check browser console** for JavaScript errors
2. **Check Render logs** for backend errors
3. **Test API endpoints** manually with curl/Postman
4. **Verify environment variables** are set correctly in Render

The fixes I've applied should resolve the most common deployment issues. After pushing and redeploying, your Contact Manager should work perfectly! 🚀
