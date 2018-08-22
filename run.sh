#!/usr/bin/env bash

# NOT FOR PRODUCTION

# This script is here to support development mode.

export FLASK_ENV=development
export FLASK_APP=qcweb
flask run --without-threads "$@"
