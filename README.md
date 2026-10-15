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
