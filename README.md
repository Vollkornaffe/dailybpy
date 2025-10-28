[![Building bpy](https://github.com/BradyAJohnston/dailybpy/actions/workflows/build-bpy-module.yml/badge.svg)](https://github.com/BradyAJohnston/dailybpy/actions/workflows/build-bpy-module.yml)
[![Publish Package Index](https://github.com/BradyAJohnston/dailybpy/actions/workflows/publish-index.yml/badge.svg)](https://github.com/BradyAJohnston/dailybpy/actions/workflows/publish-index.yml)

# Daily bpy Builds

Automated daily builds of Blender as a Python module (bpy) for Linux, macOS (ARM64), and Windows. These builds are run daily from the `main` branch of the [Blender](https://github.com/Blender/blender) repo which is an official mirror of the [Gitea](https://projects.blender.org/Blender/blender) development.

A repo for these builds is hosted at `bradyajohnston.github.io/dailybpy` so you can install using `uv` or `pip` from a custom repo to get the latest daily build as below.

## Requirements

- Python 3.11

## Installation

Install bpy using our custom package index, which automatically selects the correct platform:

#### `uv`
```bash
uv pip install bpy --extra-index-url https://bradyajohnston.github.io/dailybpy/
```
#### `pip`
```bash
pip install bpy --extra-index-url https://bradyajohnston.github.io/dailybpy/
```

### Project Configuration

For a cleaner experience, configure the index once in your `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "dailybpy"
url = "https://bradyajohnston.github.io/dailybpy/"

[project]
dependencies = [
    "bpy",
]
```

Then install with:

```bash
uv pip install bpy
# or
uv sync
```

## Testing Your Installation

After installation, test that bpy is working correctly:

```python
python -c "import bpy; print(f'Blender {bpy.app.version_string} loaded successfully')"
```

## About

- **Version**: `5.1.0a0` (alpha) - built from the latest Blender main branch
- **Build Schedule**: Daily at 2 AM UTC
- **Source**: [Blender official repository](https://github.com/blender/blender)

### Supported Platforms

| Platform | Architecture | Status |
|----------|-------------|--------|
| Linux | x86_64 | ✅ |
| macOS | ARM64 (Apple Silicon) | ✅ |
| Windows | x64 | ✅ |

## Alternative Installation Methods

<details>
<summary>Direct wheel download from GitHub Releases</summary>

Download the appropriate wheel file for your platform from the [latest release](https://github.com/BradyAJohnston/dailybpy/releases/latest):

- **Linux (x64)**: `bpy-*-manylinux_2_39_x86_64.whl`
- **macOS (ARM64)**: `bpy-*-macosx_11_0_arm64.whl`
- **Windows (x64)**: `bpy-*-win_amd64.whl`

Then install:

```bash
pip install path/to/downloaded/bpy-*.whl
```

</details>

<details>
<summary>Automated install script</summary>

Use the provided script to automatically detect your platform:

```bash
# Download and run
curl -sSL https://raw.githubusercontent.com/BradyAJohnston/dailybpy/main/install.py | python3

# Or locally
git clone https://github.com/BradyAJohnston/dailybpy.git
cd dailybpy
python install.py
```

</details>

## Troubleshooting

**Python version mismatch?** These builds require Python 3.11. With uv, you can easily create a Python 3.11 environment:

```bash
uv venv --python 3.11
source .venv/bin/activate  # On Unix/macOS
```

## License

This repository contains build automation only. Blender is licensed under GPL v3. See the [Blender license](https://www.blender.org/about/license/) for details.
