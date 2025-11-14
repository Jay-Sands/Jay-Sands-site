# Jay Sands Site - Workflow Documentation

## Repository Structure


### Development Repo
- **Location**: `c:\Users\jsang\OneDrive\Desktop\Jay-Sands-site\feature`
- **Branch**: `main` (or your active branch)
- **Purpose**: All active development and edits happen here


### Staging/Test Repo
- **Location**: `c:\jay-sands-site-test`
- **Branch**: `main`
- **Purpose**: After committing in the development repo, push to this test repo to verify all changes transfer correctly before going live


## Workflow Steps

1. **Development**: Work and edit files in `feature/` folder (not feature/feature/)
2. **Commit**: Commit your changes in the `feature/` folder
3. **Push to Test**: Push your changes to the `jay-sands-site-test` repo to verify everything transfers correctly
4. **Test**: Open and test the site in `jay-sands-site-test` to ensure all changes are present and working
5. **Deploy to Live**: Once verified, push from test repo to the main (live) repo/branch for deployment (Netlify auto-deploys from main)

## Why This Setup

- Feature repo can't push directly to main (branch mismatch: `master` vs `main`)
- **This accidental setup actually works better** - adds multiple safety layers
- Test repo acts as staging environment before going live
- Prevents accidental breaking of live site
- Netlify auto-deploys from the main branch


## Folder Structure

- **`feature/`** = Active workspace (where you edit and commit files)
- **`jay-sands-site-test`** = Staging/test repo for verification before going live

**Important:** Do all work in `feature/` (not in `feature/feature/`).

## Tech Stack

- **Hosting**: Netlify
- **Forms**: Netlify Forms (`data-netlify="true"`)
- **Auto-deploy**: Enabled from main branch
- **Domain**: jsands.net

## Notes

- The nested `feature/feature/` folder is intentional and part of the workflow
- Always copy files to `feature/` before committing (git doesn't track `feature/feature/`)
- Test in `jay-sands-site-test` before pushing to main/live

---

**Status**: Working as designed ✅
**Last Updated**: November 11, 2025
