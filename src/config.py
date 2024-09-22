#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; tab-width: 4 -*-
# vim: ft=python fenc=utf-8

from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    app_name: str = "Kantele"
    version: str = "0.0.1"

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        case_sensitive=False,
    )

config = Config()
