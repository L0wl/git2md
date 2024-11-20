import os
import sys
import subprocess
from pathlib import Path
import sysconfig


def is_admin():
    """Check if the script is running with administrative privileges."""
    return os.geteuid() == 0


def install_package():
    """Install the package and determine the scripts path."""
    print("Installing the package...")
    try:
        # Determine the directory where install.py is located
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Absolute path to the package directory
        package_dir = script_dir

        # Ensure pip is available in the current Python interpreter
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "--version"],
                check=True,
                stdout=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            print("pip is not available in the current Python environment.")
            print(
                "Please install pip or use a Python interpreter that has pip installed."
            )
            sys.exit(1)

        # Install the package in editable mode
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", package_dir], check=True
        )
        print("Package installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing the package: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    # Determine the scripts path where binaries are installed
    scripts_path = sysconfig.get_path("scripts")
    if not scripts_path:
        print("Warning: Could not determine the scripts directory.")
        return None

    scripts_path = os.path.abspath(scripts_path)
    return scripts_path


def check_and_create_symlink_unix(scripts_path):
    """Check and create a symlink to git2md in /usr/local/bin on Unix-based systems."""
    git2md_script = os.path.join(scripts_path, "git2md")
    target_path = "/usr/local/bin/git2md"

    if os.path.exists(target_path):
        print(f"{target_path} already exists.")
        return

    print(f"{target_path} does not exist.")
    choice = (
        input("Do you want to create a symlink to git2md in /usr/local/bin? [y/N]: ")
        .strip()
        .lower()
    )
    if choice != "y":
        print("No changes were made.")
        return

    if not is_admin():
        print("Root privileges are required to create a symlink in /usr/local/bin.")
        subprocess.check_call(["sudo", "ln", "-s", git2md_script, target_path])
    else:
        try:
            if os.path.islink(target_path) or os.path.exists(target_path):
                overwrite = (
                    input(
                        f"A file already exists at {
                            target_path}. Do you want to overwrite it? [y/N]: "
                    )
                    .strip()
                    .lower()
                )
                if overwrite != "y":
                    print("No changes were made.")
                    return
                else:
                    os.remove(target_path)
            os.symlink(git2md_script, target_path)
            print(f"Successfully created symlink to git2md at {target_path}")
        except Exception as e:
            print(f"An error occurred while creating symlink: {e}")


def main():
    # Detect if running in a virtual environment
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        in_virtual_env = True
    else:
        in_virtual_env = False

    if in_virtual_env:
        print(
            "\nWarning: You are about to install git2md inside a virtual environment."
        )
        print(
            "The git2md CLI tool will not be available globally once the virtual environment is deactivated."
        )
        choice = (
            input("Do you want to continue with the installation? [y/N]: ")
            .strip()
            .lower()
        )
        if choice != "y":
            print("Installation aborted by user.")
            sys.exit(0)

    scripts_path = install_package()
    if scripts_path is None:
        sys.exit(1)

    print(f"Python Scripts path: {scripts_path}")

    check_and_create_symlink_unix(scripts_path)


if __name__ == "__main__":
    main()
