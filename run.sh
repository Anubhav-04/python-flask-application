#!bin/bash

nohup python3 -m flask --app app run --host 0.0.0.0 --port 5000 2>&1 &
