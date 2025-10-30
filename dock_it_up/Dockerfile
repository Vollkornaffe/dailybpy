# Build bpy wheel on Ubuntu and output to /dist
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /opt

# 1) System deps (incl. Git LFS + Subversion for Blender's libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git git-lfs subversion ninja-build pkg-config \
    python3 python3-pip ca-certificates \
    libx11-dev libxxf86vm-dev libxcursor-dev libxi-dev \
    libxrandr-dev libxinerama-dev libegl-dev \
    libwayland-dev wayland-protocols libxkbcommon-dev libdbus-1-dev \
 && git lfs install --system --skip-smudge \
 && rm -rf /var/lib/apt/lists/*

# 2) Get Blender (shallow, with submodules)
RUN git clone --depth=1 --recursive https://projects.blender.org/Lars-Helge-Scheel/blender some_path_with_py_in_it
WORKDIR /opt/some_path_with_py_in_it

# 3) Pull Blender precompiled libraries (uses Subversion)
RUN make update

# 4) Build the bpy module (use all CPUs)
RUN make -j"$(nproc)" bpy

# 5) Create a wheel from the built bpy and copy to /dist
RUN python3 -m pip install --upgrade pip wheel setuptools \
 && python3 ./build_files/utils/make_bpy_wheel.py ../build_linux_bpy/bin/ \
 && mkdir -p /dist \
 && cp ../build_linux_bpy/bin/bpy-*.whl /dist/

# Show what we made by default
CMD ["/bin/bash", "-lc", "ls -lh /dist"]
