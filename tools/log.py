import subprocess



def show_logs(flags: list[str] | None = None) -> str:
    """Show recent Linux journal logs. Pass journalctl flags such as ["-n", "50", "-u", "ssh"] separately."""
    print('show_logs has been called')
    command = ["journalctl", *(flags or [])]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout or "No log entries found."
    except subprocess.CalledProcessError as error:
        return error.stderr or f"Command failed with exit code {error.returncode}."
    except FileNotFoundError:
        return "journalctl is not installed."
