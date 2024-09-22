#!/usr/bin/env python3

import asyncio
import contextlib
import logging

from config import config
from fastapi import FastAPI

@contextlib.asynccontextmanager
async def lifespan(app):
    # Save for later.
    app.config = config
    app.logger = logging.getLogger(app.config.app_name)

    yield

app = FastAPI(
    title=config.app_name,
    version=config.version,

    docs_url="/api/docs",
    # Disable ReDoc when we have Swagger.
    redoc_url=None,
    openapi_url="/api/openapi.json",

    # Don't redirect `/hello` to `/hello/`
    redirect_slashes=False,

    # Lifecycle hooks.
    lifespan=lifespan,
)

