# Render the 3D model remotely with `runner.py`

Run the renderer on the RPL desktop and view it in a browser on your own computer using SSH port forwarding.

## 1. Connect to the RPL desktop

On your own computer, open a terminal and run:

```bash
ssh -L 8080:127.0.0.1:8080 audio-sg@130.237.67.205
```

This opens an SSH session and forwards your computer’s port `8080` to port `8080` on the RPL desktop. Keep this session open while viewing the model.

## 2. Open the project directory

Navigate to the `openlex3d` directory on the RPL desktop:

```bash
cd /openlex3d
```

## 3. Activate the Python environment

If the project’s `.venv` already exists:

```bash
source .venv/bin/activate
```

If it does not exist, create and activate it:

```bash
uv venv
source .venv/bin/activate
```

Dependencies are already installed.

## 4. Start the renderer

From the `openlex3d` directory, run:

```bash
python runner.py data/scene_rgb.ply
```

Replace `data/scene_rgb.ply` with the path to the model you want to view (or just use data/scene_rgb.ply). This path refers to a file on the RPL desktop.

Leave the renderer running.

## 5. View the model

On your own computer, open a browser and go to:

http://localhost:8080/

The SSH tunnel connects your browser to the renderer running on the RPL desktop.

## Troubleshooting

- **The browser cannot connect:**

Check that the renderer is running on port `8080` and the SSH session is still open.

- **Local port `8080` is already in use:**

Reconnect using

`ssh -L 8081:127.0.0.1:8080 audio-sg@130.237.67.205`,

then open http://localhost:8081/

- **Model file not found:** Run `pwd` and `ls data` to check your current directory and the model’s filename.
- **Missing Python module:** Confirm that the environment is activated and the project’s dependencies are installed.
