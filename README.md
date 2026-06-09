# SkiDL Tutorial Container Image

OCI container image for running SkiDL tutorial examples.

## What's inside

- Ubuntu 24.04
- Python 3 + pip
- ngspice + libngspice0
- numpy < 2 + matplotlib
- SkiDL 2.2.3 + InSpice 1.7.0.3
- Python 3.12 compat patch

## Usage

```bash
podman pull ghcr.io/peiy-meguru/pyspice-skidl

podman run --rm --memory=512m \
  -v $(pwd)/docs/tutorial/scripts/skidl:/scripts:Z \
  ghcr.io/peiy-meguru/pyspice-skidl \
  /scripts/middle-school/ch03_ohms_law.py
```

## Build locally

```bash
podman build -t pyspice-skidl .
```

## CI

On push to `main` or new tags, GitHub Actions builds and publishes to `ghcr.io`.
