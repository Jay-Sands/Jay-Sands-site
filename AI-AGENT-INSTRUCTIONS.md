# AI Agent Instructions for Jay-Sands-site Codebase

## Critical Rules - ALWAYS Follow These

### 1. **ALWAYS Work on the `site-updates` Git Branch**
- All code changes, edits, and feature development MUST be done on the `site-updates` branch
- Never make changes directly on the `main` branch
- When starting work, ensure you are on the `site-updates` branch first
- To verify your current branch, use: `git branch` or `git status`
- To switch to the correct branch, use: `git checkout site-updates`

## Workflow Overview

This codebase follows the **SITE-WORKFLOW-2026-01-19** process:

1. **Development:** All work happens on `site-updates` branch
2. **Experimental Features:** Use temporary `feature/...` branches for experimental changes (optional)
3. **Approval:** Changes are reviewed before merging back to `site-updates`
4. **Deployment:** When ready, `site-updates` is merged into `main`
5. **Live Deployment:** `main` branch is pushed to remote, triggering automatic Cloudflare deployment
6. **Return to Development:** After deployment, switch back to `site-updates`

## Project Structure

### Key Directories
- **`site/`** - Main site files (your working location)
- **`Main/`** - Backup/archive structure
- **`images/`** - Image assets
- **`tracks/`** - Track-related files

### Key Files
- **`style.css`** - Main stylesheet
- **`index.html`** - Home page
- **`scripts.js`** - JavaScript functionality
- **`live.html`** - Live stream page with chat functionality
- **`SITE-WORKFLOW-2026-01-19.txt`** - The workflow process (refer to this for deployment steps)

## Project-Specific Configuration

### Live Stream Page (live.html)
1. **Stream Status:** A stream is already operational and ready to integrate
2. **Listener Capacity:** Design for 100+ concurrent listeners (planned for scalability/growth)
3. **Chat Functionality:** Browser-based chat only (no persistent backend needed at this time)
4. **Firebase Setup:** Firebase project already created and ready. User has credentials available.
5. **CRITICAL: Moderation Features** - Essential for show success:
   - User ban/eject functionality
   - Username tracking for moderation
   - Firebase integration required for persistence
   - Admin panel for moderator controls
   - **Status:** Ready to implement - User will provide Firebase config credentials when needed
   - **Next Step:** When persistent chat is needed, ask user for Firebase config (apiKey, projectId, etc.) and integrate

## Communication Guidelines

**ALWAYS number questions, steps, and checklist items** when presenting them to the user. This enables quick and efficient reference.

Example:
- ❌ Bad: "Do you have a stream URL, need a backend, and how many listeners?"
- ✅ Good:
  1. Do you have a stream URL set up?
  2. Do you need backend/server support for chat?
  3. How many concurrent listeners do you expect?

## Before Starting Any Task

1. ✅ Confirm you're on the `site-updates` git branch
2. ✅ Review the current task requirements
3. ✅ Check existing code style and conventions in the codebase

## When Making Changes

- Edit files on the `site-updates` git branch only
- Maintain consistency with existing code style
- If creating new files, add them to the appropriate folder in the current structure
- Make sure you're on `site-updates` before committing any changes

## When Experimental Changes Are Needed

- Create a temporary `feature/experiment-name` branch from `site-updates`
- Make experimental changes there
- Once approved, merge back to `site-updates` and delete the temporary branch

## Deployment Checklist (NOT YOUR RESPONSIBILITY, but FYI)

1. Switch to `main` branch
2. Merge `site-updates` into `main`
3. Push `main` to remote (triggers Netlify deployment)
4. Switch back to `site-updates` for next development cycle

---

**Remember:** When in doubt, ensure you're on the `site-updates` git branch before making any changes!
---

## Future Features (Planned/Requested)

### Multi-DJ Support for Live Streaming
**Status:** User indicated interest (January 24, 2026)

**Three Options to Implement:**

1. **Option A: Different Stream URLs per DJ**
   - Add a dropdown selector on live.html to choose which DJ's stream to connect to
   - Each DJ has their own stream URL (e.g., `http://stream-dj1.com`, `http://stream-dj2.com`)
   - Single shared chat for all DJs OR separate chats per DJ (TBD with user)
   - Shared moderator panel

2. **Option B: Separate Pages per DJ**
   - Create `/live-dj2.html`, `/live-dj3.html` etc. (copies of live.html with different stream URLs)
   - Each page has its own independent chat (filtered by show name or separate collection)
   - Each DJ manages their own chat moderation

3. **Option C: Multiple Moderator Passwords**
   - Keep single live.html page
   - Each DJ gets their own unique moderator password
   - DJs can only moderate messages during their own show time

**Questions to Ask User Before Implementation:**
1. Do the other DJs have their own stream URLs?
2. Should they each moderate their own show independently?
3. Do you want one shared chat or separate chats per DJ?
4. Should listeners see chat messages from other DJs' shows?

**Related Files to Modify:**
- `live.html` - Add DJ selection logic
- `style.css` - May need adjustments for new UI elements
- Firebase collections - May need to organize differently