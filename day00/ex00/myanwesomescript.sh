#!/bin/sh
curl -s $1 | grep -o 'href="[^"]*"' | cut -d '"' -f2