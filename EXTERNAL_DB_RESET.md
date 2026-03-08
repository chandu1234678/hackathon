# External Database Reset - Quick Reference

## You Have External PostgreSQL (Not Render Managed)

Your setup:
- ✅ Backend on Render  
- ✅ Database on external host (AWS RDS, Azure, DigitalOcean, etc.)
- ✅ DATABASE_URL set as environment variable

---

## Reset Database in 3 Commands

```bash
# 1. Go to backend folder
cd backend

# 2. Activate Python environment
venv\Scripts\activate

# 3. Run reset script
python reset_external_db.py
```

When prompted: Type `RESET` to confirm

---

## What This Does

Deletes old test data that's blocking new signups:
- ❌ Removes all users
- ❌ Removes all patient records
- ❌ Removes all analysis history
- ❌ Removes all health metrics

Then you can create fresh account!

---

## After Reset

```bash
# Deploy new version to Render
git add -A
git commit -m "Backend updated after database reset"
git push
```

Wait for Render deployment to complete, then:
- ✅ Create new account with your email
- ✅ Login with same credentials
- ✅ System should work!

---

## Troubleshooting

### "DATABASE_URL not found"
Add to your `.env` file:
```
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

### "psycopg2 not installed"
Install it:
```bash
pip install psycopg2-binary
```

### "Connection refused"
- Check host/port are correct
- Check username/password
- Check network access to database server
- Try from command line first: `psql postgresql://user:pass@host:5432/db`

### Still seeing old data after reset?
- Frontend cache issue: Clear browser cookies/storage
- Or: Logout → Clear LocalStorage manually → Try again

---

## Alternative: Manual SQL Reset

If Python script doesn't work, connect directly:

```bash
# Install psql if needed (from PostgreSQL)
psql "postgresql://user:password@host:5432/dbname"
```

Then in psql:
```sql
DELETE FROM users CASCADE;
DELETE FROM patients CASCADE;
DELETE FROM prediction_logs CASCADE;
DELETE FROM ulcer_images CASCADE;
DELETE FROM health_metrics CASCADE;
\q
```

---

## Diagnostic Endpoints

Check your database without resetting:

```
https://medvision-backend.onrender.com/diagnostics/health
https://medvision-backend.onrender.com/diagnostics/users
https://medvision-backend.onrender.com/diagnostics/info
```

---

## Next Steps

1. ✅ Run reset_external_db.py
2. ✅ Confirm with "RESET"
3. ✅ Git commit and push
4. ✅ Wait for Render deployment
5. ✅ Try creating account
6. ✅ Test full workflow

**You're done!** 🎉

---
