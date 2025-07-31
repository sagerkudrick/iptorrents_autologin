# IPTorrents Auto Login Tool

## Overview

This tool automates the login process to [iptorrents.com](https://iptorrents.com) using an undetected Chrome driver. It’s designed to be used **locally**, as using a VPS or VPN will likely trigger Cloudflare’s bot protection, requiring you to manually prove you're human. While this can still happen on a trusted residential IP, it's much less frequent—reducing the time and effort you need to spend.

---

## How It Works

- The tool launches a Chromium browser instance controlled by the script.
- If Cloudflare’s "Are you human?" challenge appears, the script will **wait indefinitely** so you can solve the CAPTCHA manually.
- Once the login page is visible, it will:
  - Fill in your IPTorrents username and password.
  - Submit the login form.
- Upon successful login, it will:
  - Take a screenshot of the logged-in page (`loggedin.png`) so you can verify when it last ran successfully.
  - Wait 20 seconds before automatically closing the browser.
- You may also close the browser manually at any time.

---

## Usage Instructions

### Manual Use

1. Place `ipt_login.exe` and `config.json` in the same folder.
2. Edit the `config.json` file with your IPTorrents credentials:

    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

3. Double-click `ipt_login.exe` to start the login process manually.
4. If a Cloudflare check appears, complete it. The script will continue once it reaches the login form.

---

### Automatic Scheduled Run

You can set this up to run on a routine (e.g., every 14 days) so you don’t have to manually maintain activity:

1. Ensure the following files are in the same folder:
   - `ipt_login.exe`
   - `config.json`
   - `run_login.bat` (included batch script)

2. Confirm your credentials are correct in `config.json`.

3. Schedule the batch script to run periodically:
   - **Windows:** Use Task Scheduler to run `run_login.bat` every 14 days or on a custom interval.
   - **Linux/macOS:** Use a cron job to call a shell script that runs the `.exe` (via Wine if needed).

4. The script will run quietly, handle login, and save a `loggedin.png` screenshot of the result.

---

## Dependencies

- The `.exe` is bundled using [PyInstaller](https://www.pyinstaller.org/) with Python 3.9+.
- Uses the `undetected-chromedriver` Python package to bypass bot detection.
- Requires a local installation of the **Chrome** browser (any recent version).
- No need to have Python installed if you're using the `.exe`.

---

## Important Notes

- **Keep this tool and your `config.json` private and local.**
- The login automation relies on your **trusted local IP address**. Using this from a VPS or unknown IP will almost certainly result in Cloudflare prompts.
- Even locally, Cloudflare may still prompt you occasionally—this is expected and handled by the indefinite wait built into the tool.
- The `loggedin.png` file is overwritten each time and can be used as a quick log of successful logins.

---

## Security Disclaimer

- Your IPTorrents credentials are stored in plaintext in `config.json`. Do not share this file or sync it to cloud storage without encryption.
- This tool is for **personal use only** on accounts you own.
- No information is sent anywhere other than directly to the IPTorrents site through your browser.

---

## Support & Contributions

This project is simple by design. Feel free to suggest improvements or report bugs.

---

*Happy torrenting!* 🎉
