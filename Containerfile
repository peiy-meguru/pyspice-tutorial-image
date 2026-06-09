FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv ngspice libngspice0 \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/lib/x86_64-linux-gnu/libngspice.so.0 /usr/lib/x86_64-linux-gnu/libngspice.so

RUN pip3 install --no-cache-dir --break-system-packages \
    "numpy<2" matplotlib skidl

COPY image/patch_skidl_logger.py /tmp/patch_skidl_logger.py
RUN python3 /tmp/patch_skidl_logger.py && rm /tmp/patch_skidl_logger.py

WORKDIR /workspace
ENTRYPOINT ["python3"]
