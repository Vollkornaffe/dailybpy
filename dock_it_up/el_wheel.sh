docker build -t bpy-wheel .

# 1) Create a container without mounting over /dist
cid=$(docker create bpy-wheel)

# 2) Copy the wheel(s) out to ./dist on the host
mkdir -p dist
docker cp "$cid":/dist/. ./dist/

# 3) Clean up
docker rm "$cid"

# Check
ls -lh dist/
