#!/usr/bin/env bash
flake8 .
coverage run -m unittest
coverage html
coverage-badge -fo coverage.svg
