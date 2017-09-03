#!/usr/bin/env bash
coverage run -m unittest && coverage html
rm coverage.svg
coverage-badge -o coverage.svg
