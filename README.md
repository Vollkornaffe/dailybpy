# Daily bpy Builds

Automated daily builds of Blender as a Python module (bpy) for Linux, macOS (ARM64), and Windows.

## Requirements

- Python 3.11

## Installation

### Quick Install (Latest Release)

#### Using pip

```bash
# Linux
pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-manylinux_2_39_x86_64.whl

# macOS (Apple Silicon)
pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-macosx_11_0_arm64.whl

# Windows
pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-win_amd64.whl
```

#### Using uv

```bash
# Linux
uv pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-manylinux_2_39_x86_64.whl

# macOS (Apple Silicon)
uv pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-macosx_11_0_arm64.whl

# Windows
uv pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-win_amd64.whl
```

### Manual Download and Install

1. Go to [Releases](https://github.com/BradyAJohnston/dailybpy/releases)
2. Download the appropriate wheel file for your platform:
   - **Linux (x64)**: `bpy-*-manylinux_2_39_x86_64.whl`
   - **macOS (ARM64)**: `bpy-*-macosx_11_0_arm64.whl`
   - **Windows (x64)**: `bpy-*-win_amd64.whl`
3. Install the wheel:

```bash
# Using pip
pip install path/to/downloaded/bpy-*.whl

# Using uv
uv pip install path/to/downloaded/bpy-*.whl
```

### Automated Install Script

Use the provided install script to automatically detect your platform and install the latest build:

```bash
# Download and run the install script
curl -sSL https://raw.githubusercontent.com/BradyAJohnston/dailybpy/main/install.py | python3

# Or with uv
curl -sSL https://raw.githubusercontent.com/BradyAJohnston/dailybpy/main/install.py | python3 - --uv
```

Alternatively, download and run locally:

```bash
# Clone the repo
git clone https://github.com/BradyAJohnston/dailybpy.git
cd dailybpy

# Run the installer
python install.py

# Or with uv
python install.py --uv
```

## Testing Your Installation

After installation, test that bpy is working correctly:

```python
python -c "import bpy; print(f'Blender {bpy.app.version_string} loaded successfully')"
```

Or run a simple render test:

```python
python -c "import bpy; bpy.ops.render.render(write_still=True)"
```

## Version Information

These builds are generated from the latest Blender main branch and are versioned as `5.1.0a0` (alpha). Builds are created daily at 2 AM UTC.

## Platform Support

| Platform | Architecture | Status |
|----------|-------------|--------|
| Linux | x86_64 | ✅ Supported |
| macOS | ARM64 (Apple Silicon) | ✅ Supported |
| Windows | x64 | ✅ Supported |

## Using uv for Virtual Environment Management

If you're using [uv](https://github.com/astral-sh/uv) for faster package management:

```bash
# Create a new virtual environment with Python 3.11
uv venv --python 3.11

# Activate the environment
source .venv/bin/activate  # On Unix/macOS
# .venv\Scripts\activate  # On Windows

# Install bpy
uv pip install https://github.com/BradyAJohnston/dailybpy/releases/latest/download/bpy-5.1.0a0-cp311-cp311-manylinux_2_39_x86_64.whl
```

## Troubleshooting

### Python Version Mismatch

These builds require Python 3.11. If you have a different version:

```bash
# Check your Python version
python --version

# With uv, you can easily use Python 3.11
uv venv --python 3.11
source .venv/bin/activate
```

### Platform Detection Issues

If the automated install script fails to detect your platform, manually download and install the appropriate wheel from the [releases page](https://github.com/BradyAJohnston/dailybpy/releases).

## Build Information

- Builds run automatically via GitHub Actions daily
- Each build includes all dependencies and libraries needed to run Blender as a Python module
- Source: [Blender official repository](https://github.com/blender/blender)

## License

This repository contains build automation only. Blender itself is licensed under GPL v3. See the [Blender license](https://www.blender.org/about/license/) for details.
