# Copilot Instructions for Jay Sands Site

## Project Overview
- This is a static website for Jay Sands, with all content managed via HTML, CSS, and static assets.
- The main site structure is duplicated across several folders: `feature/`, `Main/`, `site-backup/`, and the root. Each contains similar HTML files for different site versions or backups.
- The `feature/` directory is used for staging or previewing new/experimental site features before merging into the main site.
- The `site/` and root folders contain the live/production version of the site.

## Key Files & Directories
- `index.html`, `home.html`, `shows.html`, etc.: Main site pages. Duplicated in several folders for backup/versioning.
- `style.css`: Main stylesheet, also duplicated per folder.
- `images/`, `tracks/`: Static assets (images, audio, etc.).
- `site-backup/`, `testfolder/`, `testfoldeer/`: Used for manual backups and testing.
- `WORKFLOW.md`, `SITE-WORKFLOW.txt`: Human-readable notes on site update processes.

## Developer Workflow
- **No build step**: All files are static. Deploy by copying HTML/CSS/assets to the appropriate folder.
- **Manual versioning**: Backups are made by copying files/folders (e.g., `index-backup.html`, `christmas-backup-2025-11-11.html`).
- **Preview features**: Develop in `feature/` first, then copy to root or `site/` when ready.
- **No automated tests or CI/CD**: All updates are manual.

## Project Conventions
- Keep file/folder names lowercase and hyphenated (e.g., `promotional-banner.html`).
- When updating a page, update all relevant copies (root, `site/`, `feature/`, etc.) to keep versions in sync.
- Use clear backup naming: `*-backup.html` or with date suffixes.
- Do not introduce frameworks, build tools, or dynamic scripting unless explicitly requested.

## Examples
- To update the "shows" page: edit `shows.html` in `feature/`, test, then copy to root and `site/`.
- To add a new image: place it in all relevant `images/` folders.

## Integration Points
- No external APIs or dynamic integrations. All content is static.

## References
- See `WORKFLOW.md` and `SITE-WORKFLOW.txt` for additional manual process notes.

---
For questions or unclear conventions, consult the workflow files or ask the project maintainer.
