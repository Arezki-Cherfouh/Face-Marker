#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_face_marker_gui..."
wine "run_face_marker_gui" || ./"run_face_marker_gui" "$@"
