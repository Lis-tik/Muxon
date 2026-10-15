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
├── Dockerfile
├── README.md
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
└── .dockerignore
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://localhost:8000/docs
