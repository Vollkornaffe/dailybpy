#!/usr/bin/env python3
"""
Automated installer for daily bpy builds.
Detects platform and installs the appropriate wheel from the latest GitHub release.
"""

import sys
import platform
import subprocess
import argparse


def get_platform_wheel_name():
    """Detect the current platform and return the appropriate wheel filename pattern."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Base wheel name pattern
    wheel_base = "bpy-5.1.0a0-cp311-cp311"

    if system == "linux":
        if machine in ["x86_64", "amd64"]:
            return f"{wheel_base}-manylinux_2_39_x86_64.whl"
        else:
            raise ValueError(f"Unsupported Linux architecture: {machine}")

    elif system == "darwin":
        if machine in ["arm64", "aarch64"]:
            return f"{wheel_base}-macosx_11_0_arm64.whl"
        else:
            raise ValueError(f"Unsupported macOS architecture: {machine}. Only Apple Silicon (ARM64) is supported.")

    elif system == "windows":
        if machine in ["amd64", "x86_64"]:
            return f"{wheel_base}-win_amd64.whl"
        else:
            raise ValueError(f"Unsupported Windows architecture: {machine}")

    else:
        raise ValueError(f"Unsupported operating system: {system}")


def check_python_version():
    """Check if Python version is 3.11."""
    version = sys.version_info
    if version.major != 3 or version.minor != 11:
        print(f"Warning: Python 3.11 is required, but you are using Python {version.major}.{version.minor}")
        print("The installation may fail or bpy may not work correctly.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)


def install_wheel(wheel_url, use_uv=False):
    """Install the wheel using pip or uv."""
    if use_uv:
        cmd = ["uv", "pip", "install", wheel_url]
    else:
        cmd = [sys.executable, "-m", "pip", "install", wheel_url]

    print(f"Installing bpy from: {wheel_url}")
    print(f"Running: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
        print("\nInstallation successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nInstallation failed with error code {e.returncode}")
        return False
    except FileNotFoundError:
        if use_uv:
            print("\nError: 'uv' command not found. Please install uv first:")
            print("  pip install uv")
            print("  OR visit: https://github.com/astral-sh/uv")
        else:
            print("\nError: pip not found")
        return False


def test_installation():
    """Test if bpy was installed correctly."""
    print("\nTesting bpy installation...")
    try:
        result = subprocess.run(
            [sys.executable, "-c", "import bpy; print(f'Blender {bpy.app.version_string} loaded successfully')"],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout.strip())
        return True
    except subprocess.CalledProcessError:
        print("Warning: bpy import test failed. The module may not be correctly installed.")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Install the latest daily bpy build for your platform"
    )
    parser.add_argument(
        "--uv",
        action="store_true",
        help="Use uv instead of pip for installation"
    )
    parser.add_argument(
        "--skip-test",
        action="store_true",
        help="Skip the post-installation test"
    )
    parser.add_argument(
        "--repo",
        default="BradyAJohnston/dailybpy",
        help="GitHub repository (default: BradyAJohnston/dailybpy)"
    )

    args = parser.parse_args()

    print("Daily bpy Installer")
    print("=" * 50)

    # Check Python version
    check_python_version()

    # Detect platform
    try:
        wheel_name = get_platform_wheel_name()
        print(f"\nDetected platform: {platform.system()} {platform.machine()}")
        print(f"Target wheel: {wheel_name}")
    except ValueError as e:
        print(f"\nError: {e}")
        print("\nSupported platforms:")
        print("  - Linux x86_64")
        print("  - macOS ARM64 (Apple Silicon)")
        print("  - Windows x64")
        sys.exit(1)

    # Construct wheel URL
    wheel_url = f"https://github.com/{args.repo}/releases/latest/download/{wheel_name}"

    # Install
    success = install_wheel(wheel_url, use_uv=args.uv)

    if not success:
        print("\nTroubleshooting:")
        print("  1. Check your internet connection")
        print("  2. Verify the latest release exists at:")
        print(f"     https://github.com/{args.repo}/releases")
        print("  3. Try downloading and installing manually:")
        print(f"     pip install {wheel_url}")
        sys.exit(1)

    # Test installation
    if not args.skip_test:
        test_installation()

    print("\nInstallation complete! You can now use bpy in Python:")
    print("  python -c 'import bpy; print(bpy.app.version_string)'")


if __name__ == "__main__":
    main()
