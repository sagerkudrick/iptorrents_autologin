# IPTorrents Auto Login Tool

## Overview

This tool automates the login process to iptorrents.com using an undetected Chrome driver. It’s designed to be used locally because using a VPS or VPN will likely trigger Cloudflare’s bot protection, requiring you to verify that you are human. While manual verification can still occasionally happen locally, being on a “trusted” IP address greatly reduces these prompts and minimizes your involvement.

---

## How It Works

- The tool launches a Chromium browser instance controlled by the script.
- If Cloudflare’s "Are you human?" challenge appears, the script will **pause indefinitely**, allowing you to manually solve the CAPTCHA.
- Once the challenge is cleared and the login form appears, the tool automatically fills in your username and password and logs you in.
- After logging in, the browser stays open for 20 seconds before closing automatically.
- If you wish, you can close the browser manually at any time to end the session early.

---

## Usage Instructions

### Manual Use

- Make sure `ipt_login.exe` and `config.json` are in the same folder.
- Edit the `config.json` file to add your IPTorrents username and password:

    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

- Double-click `ipt_login.exe` to run the login process manually.
- You can manually solve Cloudflare challenges if prompted during execution.

---

### Automatic Scheduled Run

You can set this tool to run automatically on a schedule (e.g., every 14 days) to reduce manual involvement:

1. Ensure `ipt_login.exe`, `config.json`, and `run_login.bat` (batch script) are in the same folder.

2. Edit `config.json` with your credentials as shown above.

3. Use your operating system’s task scheduler to run `run_login.bat` at your desired interval:

   - **Windows:** Use Task Scheduler to create a basic task that runs `run_login.bat` every 14 days (or your preferred schedule).
   - **Linux/macOS:** Use `cron` jobs to execute a shell script that calls the executable.

4. The batch script will launch the executable, which opens the browser for login and lets you complete Cloudflare challenges manually if needed.

---

## Important Notes

- **Keep this tool and your `config.json` file local and secure.**
- The script depends on your **local IP address**. Using it on an untrusted or changing IP may trigger Cloudflare more frequently, requiring manual intervention.
- Running it from your usual location reduces Cloudflare challenges, but some manual interaction may still occasionally be necessary.

---

## Dependencies

- The `.exe` is built using [PyInstaller](https://www.pyinstaller.org/) and bundles Python 3.9+.
- Uses the `undetected-chromedriver` Python library to avoid bot detection.
- Requires Chrome browser installed on the machine.
- No need to have Python installed separately if you run the `.exe` file.

---

## Security Disclaimer

- Your IPTorrents credentials are stored in plaintext in `config.json`. Keep this file private.
- Use this tool responsibly and only on accounts you own.

---

## Support & Contributions

Feel free to open issues or contribute improvements to this project.

---

*Happy torrenting!* 🎉
