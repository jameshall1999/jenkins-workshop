#!/bin/bash

docker run -p 5000:5000 flask-docker bash -c "./test.sh"
