# Auth Issues - Quick Troubleshooting

## Your Problem
- ❌ "Email already registered" when creating account
- ❌ "Invalid credentials" when trying to login
- ✅ Using external PostgreSQL database (not Render managed)
- ✅ DATABASE_URL set as environment variable

---

## Quick Fixes (Try in Order)

### Fix #1: Check Database Status (No Damage)
```bash
# Check if database is accessible
No need to run anything locally - just visit your API:

https://medvision-backend.onrender.com/diagnostics/health
```
This will show:
- ✓ If database is connected
- ✓ How many users exist

### Fix #2: List All Users (Read-Only)
```bash
# See what emails are in the database
https://medvision-backend.onrender.com/diagnostics/users
```
If you see test emails like "test@example.com", that's the problem!

### Fix #3: Check If Email Exists (Debugging)
```bash
# Replace YOUR_EMAIL with the email you want to try
https://medvision-backend.onrender.com/diagnostics/check-email/YOUR_EMAIL
```

---

## Nuclear Option: Reset Database

### Option 1: Via Python Script (FASTEST - LOCAL)

```bash
# From your computer terminal
cd backend

# Activate environment
venv\Scripts\activate

# Run reset
python fix_database.py --reset

# When prompted, type: RESET (to confirm)
# All data will be deleted
```

Then deploy to Render:
```bash
git add -A
git commit -m "Database reset - cleaning old test data"
git push
```

### Option 2: Via PostgreSQL Client (Direct)

If you have `psql` installed locally:

```bash
# Find your DATABASE_URL in Render > medvision-backend > Environment
# It looks like: postgresql://user:pass@host:5432/dbname

# Connect directly to your external database
psql "postgresql://user:password@your-db-host:5432/your-db-name"

# In psql prompt, run:
DELETE FROM users CASCADE;
DELETE FROM patients CASCADE;
DELETE FROM prediction_logs CASCADE;
DELETE FROM ulcer_images CASCADE;
DELETE FROM health_metrics CASCADE;

# Exit
\q
```

Then deploy new version:
```bash
git add -A
git commit -m "Database reset - cleaned test data"
git push
```

### Option 3: Via pgAdmin (GUI)

If you have pgAdmin installed:

1. Create connection to your external PostgreSQL
2. Right-click **users** table > **Delete/Truncate**
3. Repeat for: patients, prediction_logs, ulcer_images, health_metrics
4. Refresh Render deployment

---

## After Database Reset

1. **Create your first account**:
   - Email: `your-email@example.com`
   - Password: `At least 8 characters`

2. **Login with same credentials**

3. **Test the system**:
   - Go to Account Settings
   - Add Health Metrics Defaults
   - Upload a foot image
   - Verify it auto-fills with saved metrics

---

## Diagnostic Endpoints (Development Only)

These are available at `https://medvision-backend.onrender.com`:

| Endpoint | Purpose | Safe? |
|----------|---------|-------|
| `/diagnostics/health` | Check database connection | ✅ Yes |
| `/diagnostics/users` | List all users | ⚠️ Shows emails |
| `/diagnostics/check-email/{email}` | Check if email exists | ⚠️ Leaks info |
| `/diagnostics/info` | Database statistics | ⚠️ Shows details |
| `/diagnostics/reset-warning` | What reset would do | ✅ Yes |

---

## Common Causes of Auth Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Email already exists | Duplicate in DB | Delete via diagnostics or reset |
| Invalid credentials | Wrong password or bad hash | Reset and recreate account |
| Database connection error | Render DB down | Check Render dashboard |
| Can't login after signup | Session/token issue | Clear cache, try new email |

---

## Prevention Going Forward

To **avoid this in future**:

1. ✅ Always test locally before pushing to Render
2. ✅ Use fresh email each time during development
3. ✅ Don't keep test data in production DB
4. ✅ Set up automated backups on Render
5. ✅ Use database migrations (Alembic) for schema changes

---

## Still Stuck?

Check these files for more details:
- `DB_RESET_GUIDE.md` - Detailed reset instructions
- `backend/fix_database.py` - Full diagnostic tool
- `backend/app/routes/diagnostics.py` - API endpoints

Or check Render logs:
1. Dashboard > medvision-backend > Logs
2. Look for errors about database connection
3. Check environment variables are set correctly

---

## Next Steps

After fixing auth, you're ready to:
- ✅ Test health metrics form (just added!)
- ✅ Verify auto-fill on upload page
- ✅ Test full analysis workflow
- ✅ Deploy to production when ready

Good luck! 🚀
