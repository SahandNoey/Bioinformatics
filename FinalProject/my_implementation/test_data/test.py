import subprocess
import sys

# Run the command to list Python installations
result = subprocess.run(['where', 'python'] if sys.platform == 'win32' else ['which', 'python'], capture_output=True, text=True)

if result.returncode == 0:
    print("Installed Python versions:")
    print(result.stdout)
else:
    print("No Python versions found.")
