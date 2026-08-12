# HH Goa 2026 Builder ID Generator

This is a web application for generating, viewing, and sharing Builder IDs for HH Goa 2026.

## Features
- Solo and Crew modes
- Builder ID generation with customizable themes and roles
- Offline fallback and cross-device sharing via QR codes
- Image capture and compression

## Deployment

The application is deployment-ready and relies on a Python backend server that serves the static assets and provides a persistence API for sharing badges across devices.

### Environment Variables
Configure the following environment variables in your deployment environment (see `.env.example`):
- `PORT`: The port on which the server should listen (default: `8000`).
- `API_KEY`: The application key used for cloud persistence (default: `9ogy9ct9`).

### Running the Server
The application uses only the standard Python library.
```bash
python serve.py
```
The server binds to `0.0.0.0` and listens on the configured `PORT`.

### Health Check
A health check endpoint is available at `/health`, which returns `{"status": "ok"}`.

## Local Development
Run `python serve.py` to start the local development server. Ensure your devices are on the same LAN to test cross-device QR scanning.
