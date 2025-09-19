# Contact Manager Setup Guide

## Alternative Ways to Run (If PowerShell Not Working)

### Method 1: Using Command Prompt (cmd)
1. **Open Command Prompt** (cmd) as Administrator
2. **Navigate to your project folder:**
   ```
   cd C:\Users\vinod\Downloads\Finall\Finall\contact
   ```

3. **Start Backend:**
   - Double-click `start_backend.cmd` OR
   - Run: `start_backend.cmd`

4. **Start Frontend (in new Command Prompt):**
   - Double-click `start_frontend.cmd` OR
   - Run: `start_frontend.cmd`

### Method 2: Manual Commands in Command Prompt

**Backend Setup:**
```
cd C:\Users\vinod\Downloads\Finall\Finall\contact\backend
pip install -r requirements.txt
python test_db.py
python app.py
```

**Frontend Setup (in new Command Prompt):**
```
cd C:\Users\vinod\Downloads\Finall\Finall\contact
npm install
npm start
```

### Method 3: Using Windows Terminal
1. Open Windows Terminal
2. Use the same commands as Method 2

### Method 4: Using VS Code Terminal
1. Open VS Code
2. Open the `contact` folder
3. Open Terminal in VS Code (Ctrl + `)
4. Use the same commands as Method 2

## Troubleshooting

### If pip is not recognized:
```
python -m pip install -r requirements.txt
```

### If npm is not recognized:
- Install Node.js from https://nodejs.org
- Restart your computer
- Try again

### If python is not recognized:
- Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation
- Restart your computer
- Try again

## What to Expect

1. **Backend will run on:** http://localhost:5000
2. **Frontend will run on:** http://localhost:3000
3. **Database:** Your Neon PostgreSQL database

## Testing the Setup

1. Open http://localhost:3000 in your browser
2. Register a new account
3. Add some contacts
4. Your data will be stored in the Neon database!

## Need Help?

If you're still having issues, try:
1. Restart your computer
2. Run Command Prompt as Administrator
3. Check if Python and Node.js are installed properly
