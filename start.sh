#!/bin/sh

uvicorn \
    --host 127.0.0.1 \
    --port 8000 \
    --app-dir src \
    --workers 1 \
    --log-level debug \
    --reload \
    main:app
