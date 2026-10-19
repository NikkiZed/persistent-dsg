"""
This is the runner.py file already on the RPL desktop in /home/audio-sg/openlex3d/runner.py
"""

import viser
import numpy as np
from plyfile import PlyData
import time
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "data/scene_rgb.ply"
vertices = PlyData.read(path)["vertex"]

# Limit displayed points to keep browser interaction responsive.
stride = max(1, int(np.ceil(len(vertices) / 500_000)))
points = np.column_stack([
    vertices["x"][::stride],
    vertices["y"][::stride],
    vertices["z"][::stride],
]).astype(np.float32)

if {"red", "green", "blue"}.issubset(vertices.data.dtype.names):
    colors = np.column_stack([
        vertices["red"][::stride],
        vertices["green"][::stride],
        vertices["blue"][::stride],
    ]).astype(np.uint8)
else:
    colors = np.full(points.shape, 180, dtype=np.uint8)

valid = np.isfinite(points).all(axis=1)
points, colors = points[valid], colors[valid]
if len(points) == 0:
    raise ValueError("No valid points found.")

points -= (points.min(axis=0) + points.max(axis=0)) / 2
radius = max(float(np.linalg.norm(np.ptp(points, axis=0))) / 2, 1.0)

server = viser.ViserServer(host="127.0.0.1", port=8080)
server.scene.add_point_cloud(
    "/scene", points=points, colors=colors, point_size=0.025
)

@server.on_client_connect
def setup_camera(client):
    client.camera.position = (radius, radius, radius)
    client.camera.look_at = (0.0, 0.0, 0.0)

print(f"Displaying {len(points):,} points from {path}", flush=True)
print("Viewer running. Keep this terminal open; Ctrl+C stops it.", flush=True)
while True:
    time.sleep(1)
