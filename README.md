# Muxon

Self-hosted video processing service based on Python and FFmpeg.

## Goals

- Process video according to predefined templates
- Support self-hosted deployment
- Keep formats, presets, and render jobs reproducible
- Facilitate automation for multiple output variants

## Branch strategy

- main: stable release branch
- develop: integration branch for active development
- feature/*: new functionality
- fix/*: bug fixes
- ops/*: infra and deployment
- docs/*: documentation updates

## Stack

- Python
- FFmpeg
- Docker / systemd / reverse proxy optional

## Project structure

```text
.
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   ├── ffmpeg_service.py
│   │   └── template_repository.py
│   ├── schemas/
│   │   └── template.py
│   ├── services/
│   │   └── job_service.py
│   ├── templates/
│   │   ├── social_landscape.json
│   │   └── social_vertical.json
│   ├── __init__.py
│   ├── config.py
│   └── main.py
├── data/
├── outputs/
├── scripts/
├── .env.example
├── .gitignore
├── .python-version
├── Dockerfile
├── README.md
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
└── .dockerignore
```

## Quick start

Use CPython 3.14, matching the Docker image and pinned dependencies.

Windows PowerShell:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS / Linux:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

On Windows, start the service with `python -m uvicorn app.main:app --reload`.

Then open http://localhost:8000/docs
