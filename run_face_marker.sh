#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_face_marker..."
wine "run_face_marker" || ./"run_face_marker" "$@"
