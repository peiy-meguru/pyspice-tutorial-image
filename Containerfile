FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    ngspice \
    libngspice0 \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/lib/x86_64-linux-gnu/libngspice.so.0 /usr/lib/x86_64-linux-gnu/libngspice.so

RUN pip3 install --no-cache-dir --break-system-packages \
    "numpy<2" \
    PySpice \
    matplotlib \
    schemdraw

COPY patch_rawfile.py /tmp/patch_rawfile.py
RUN python3 /tmp/patch_rawfile.py && rm /tmp/patch_rawfile.py

WORKDIR /workspace
ENTRYPOINT ["python3"]
