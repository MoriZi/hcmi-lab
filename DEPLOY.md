# 🚀 Manual Deployment Guide for HCMI Website

This guide explains how to deploy the HCMI website to the server using rsync (recommended) or SFTP.

## Prerequisites

- Hugo installed locally
- SSH/rsync access to the server
- TMU account credentials

## Deployment Steps

### 1. Build the site locally

```bash
hugo
```

This generates the site in the `public/` folder.

### 2. Deploy using rsync (Recommended)

```bash
rsync -avz --delete public/ yourusername@pascal.ee.torontomu.ca:/home/courses/hcmi/
```

Replace `yourusername` with your TMU account username.

**What this does:**
- `-a`: Archive mode (preserves permissions, timestamps, etc.)
- `-v`: Verbose output
- `-z`: Compress data during transfer
- `--delete`: Removes files on the server that don't exist locally (keeps the site in sync)
- `public/`: Source directory (trailing slash copies contents, not the folder itself)
- `/home/courses/hcmi/`: Destination directory on the server

**Optional: Dry run to preview changes**

```bash
rsync -avz --delete --dry-run public/ yourusername@pascal.ee.torontomu.ca:/home/courses/hcmi/
```

---

## Alternative: Deploy using SFTP

If rsync is not available, you can use SFTP:

### 1. Connect to the server via SFTP

```bash
sftp yourusername@pascal.ee.torontomu.ca
```

Replace `yourusername` with your TMU account username.

### 2. Change into the web directory

```bash
cd /home/courses/hcmi
```

### 3. Remove all old files

```bash
rm -r *
```

⚠️ **Warning**: This clears the existing site to avoid stale files.

### 4. Upload the new build

From inside the SFTP session:

```bash
put -r public/*
```

This copies everything from your local `public/` folder to the server.

### 5. Exit SFTP

```bash
bye
```

## ✅ Verification

Your site should now be live at:
**http://hcmi.ee.torontomu.ca**

## Troubleshooting

### Common Issues

1. **Permission denied**: Make sure you have write access to `/home/courses/hcmi`
2. **Connection timeout**: Check your internet connection and server availability
3. **Files not updating**: Clear browser cache or try a hard refresh (Ctrl+F5)

### File Structure

After deployment, your server should contain:
```
/home/courses/hcmi/
├── index.html
├── css/
├── js/
├── media/
├── images/
├── author/
├── authors/
├── publication/
├── people/
└── contact/
```

## Development Workflow

1. Make changes to the site locally
2. Test with `hugo server` (http://localhost:1313)
3. Build with `hugo`
4. Deploy using this guide
5. Verify the live site

## Notes

- Always test locally before deploying
- Keep backups of important content
- The `public/` folder is generated and can be safely deleted after deployment
- Hugo configuration is in `hugo.toml` and `config/_default/`

---

**Last updated**: February 2025
**Maintainer**: HCMI Lab
