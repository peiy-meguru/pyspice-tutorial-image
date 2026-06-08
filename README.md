# PySpice Tutorial Container Image

This repository builds an OCI container image for running the PySpice tutorial examples.

## What's inside

- Ubuntu 24.04
- Python 3 + pip
- ngspice 42 + libngspice0
- PySpice 1.5 (with RawFile.py patch for ngspice 42+)
- numpy < 2 (required by PySpice 1.5)
- matplotlib (plotting)
- schemdraw (circuit diagrams)

## Usage

```bash
podman pull ghcr.io/peiy-meguru/pyspice-tutorial

podman run --rm --memory=1g --userns=keep-id \
  -v $(pwd)/docs:/workspace:Z \
  ghcr.io/peiy-meguru/pyspice-tutorial \
  /workspace/tutorial/scripts/college/ch04_first_order.py
```

## Build locally

```bash
podman build -f Containerfile -t pyspice-tutorial .
```

## CI

On push to `main` or new tags, GitHub Actions builds the image and publishes to `ghcr.io`.
