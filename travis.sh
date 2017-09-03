#!/usr/bin/env bash
coverage run -m unittest && coverage html
coverage-badge -o coverage.svg
