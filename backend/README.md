# Backend (Flask) for Contact Manager

## Setup with Neon Database

This backend is configured to use **Neon PostgreSQL database** for production-ready data storage.

### Quick Setup

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Test database connection and create tables:**
   ```powershell
   python test_db.py
   ```

3. **Start the server:**
   ```powershell
   python app.py
   ```

The API will run on `http://localhost:5000` by default.

### Database Configuration

The application is pre-configured with your Neon database:
- **Database**: PostgreSQL on Neon
- **Connection**: Already configured in `config.py`
- **Tables**: `users` and `contacts` (created automatically)

### Manual Setup (Alternative)

If you need to customize the database configuration:

1. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Create a `.env` file or modify `config.py`
   - Set your `DATABASE_URL` to your Neon connection string
   - Update `SECRET_KEY` and `JWT_SECRET_KEY` for production

4. **Initialize database:**
   ```powershell
   python app.py --init-db
   ```

### Your Neon Database Details

- **Host**: ep-plain-brook-ad4wvfvy-pooler.c-2.us-east-1.aws.neon.tech
- **Database**: contactmanager
- **User**: neondb_owner
- **SSL**: Required

### Database Schema

- **users**: User accounts with authentication
- **contacts**: Contact information linked to users
- **Features**: Full CRUD operations, search, favorites, user isolation

## Endpoints

- Auth
  - POST `/api/auth/register` { name, email, password }
  - POST `/api/auth/login` { email, password }

- Contacts (JWT required via `Authorization: Bearer <token>`) 
  - GET `/api/contacts?search=&sort=name|favorites`
  - POST `/api/contacts` { name, email, phone?, company?, notes? }
  - PUT `/api/contacts/<id>`
  - DELETE `/api/contacts/<id>`
  - POST `/api/contacts/<id>/toggle-favorite`


