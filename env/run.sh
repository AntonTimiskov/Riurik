#!/bin/bash
# coding: utf-8

# Running WaferSlim websocket server using python and django.

ENVDIR="$(pwd)"
SERVERDIR="$(dirname $ENVDIR)"
SRCDIR="$SERVERDIR/src"
# activating virtual environment
"$ENVDIR/linux/bin/activate"
# running server
"$ENVDIR/linux/bin/python" "$SRCDIR/manage.py" runserver localhost:8000 --multithreaded