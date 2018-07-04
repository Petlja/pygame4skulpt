#!/bin/bash

venv/bin/python -m http.server 8000 --bind 127.0.0.1 &
open http://127.0.0.1:8000/example/naslovnica.html
